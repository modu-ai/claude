#!/usr/bin/env node
// check-links.mjs — dedicated internal-link checker for AC-IA-023 (SPEC-MOC-SITE-IA-001)
//
// Scans rendered Hugo HTML under <public-root> and verifies every internal
// <a href="..."> resolves to an existing on-disk page. Resolution implements
// Hugo pretty-URL + markdown-source-link semantics:
//
//   href=/cli/start/             -> <root>/cli/start/index.html        (pretty URL)
//   href=/cli/                   -> <root>/cli/index.html               (section root)
//   href=/                       -> <root>/index.html
//   href=./install.md            -> <sourcedir>/install/index.html      (.md -> rendered leaf)
//   href=../daily/_index.md      -> <sourcedir>/../daily/index.html     (_index.md -> section root)
//   href=./first-spec.md         -> <sourcedir>/first-spec/index.html
//   href=../../code/             -> clamps at root -> <root>/code/index.html
//
// Because Hugo markdown relative links are relative to the SOURCE .md file's
// directory (not the rendered page's own directory), relative hrefs from a
// leaf page are resolved against BOTH the page's own directory AND its parent
// directory — covering section-root sources (own dir) and leaf-page sources
// (parent dir) without false positives.
//
// Skipped (not internal page links): external (http(s):, //, mailto:, tel:,
// ftp:, data:), anchor-only (#...), and JS-template (${...}) hrefs; also
// <link rel=...> resource tags (only <a> navigation/content links checked).
//
// Usage:  node www/scripts/check-links.mjs [public-root]
//   default public-root = www/public
// Exit:   0 when "broken internal links: 0", 1 when >=1 broken, 2 on usage error.

import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));

const publicRoot = process.argv[2]
  ? path.resolve(process.argv[2])
  : path.resolve(__dirname, '..', 'public');

if (!fs.existsSync(publicRoot) || !fs.statSync(publicRoot).isDirectory()) {
  console.error(`error: public root not found or not a directory: ${publicRoot}`);
  console.error(`usage: node www/scripts/check-links.mjs [public-root]`);
  process.exit(2);
}

function collectHtml(dir, acc) {
  for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
    const full = path.join(dir, entry.name);
    if (entry.isDirectory()) {
      collectHtml(full, acc);
    } else if (entry.isFile() && entry.name.endsWith('.html')) {
      acc.push(full);
    }
  }
  return acc;
}

const htmlFiles = collectHtml(publicRoot, []);
if (htmlFiles.length === 0) {
  console.error(`error: no .html files under ${publicRoot} — run "hugo" first`);
  process.exit(2);
}

// Match <a ...> opening tags, then extract href value (double-quoted,
// single-quoted, or unquoted). Unquoted values terminate at whitespace, quote,
// <, >, }, or end-of-tag.
const anchorRe = /<a\b[^>]*?\shref=(?:"([^"]*)"|'([^']*)'|([^\s"'<>}]+))/gi;

function shouldSkip(rawHref) {
  if (!rawHref) return true;
  const h = rawHref.trim();
  if (h === '') return true;
  if (/^(https?:|mailto:|tel:|ftp:|file:|data:|\/\/)/i.test(h)) return true;
  if (h.startsWith('#')) return true;
  if (/^[${]/.test(h)) return true;
  if (/^\{\{</.test(h)) return true;
  return false;
}

function stripFragQuery(h) {
  return h.split('#')[0].split('?')[0];
}

// Given a resolved URL segment list (relative to publicRoot, after .. clamping),
// push candidate on-disk HTML file paths applying Hugo pretty-URL + .md semantics.
function pushCandidatesForSegments(out, segs) {
  if (segs.length === 0) {
    out.push(path.join(publicRoot, 'index.html'));
    return;
  }
  const last = segs[segs.length - 1];
  const parents = segs.slice(0, -1);
  if (last.endsWith('.md')) {
    const stem = last.slice(0, -3);
    if (stem === '_index') {
      // _index.md renders to the section root: parents/index.html
      out.push(path.join(publicRoot, ...parents, 'index.html'));
    } else {
      // <stem>.md renders to a leaf page: parents/<stem>/index.html
      out.push(path.join(publicRoot, ...parents, stem, 'index.html'));
    }
  } else if (last.endsWith('.html')) {
    out.push(path.join(publicRoot, ...segs));
  } else {
    // No extension (pretty URL or bare path): prefer <segs>/index.html, then <segs>.html
    out.push(path.join(publicRoot, ...segs, 'index.html'));
    out.push(path.join(publicRoot, ...parents, last + '.html'));
  }
}

// Resolve a URL path against a base segment list, clamping .. at the root
// (publicRoot). Returns the resolved segment list.
function resolveUrlSegments(base, href) {
  const resolved = [...base];
  for (const p of href.split('/')) {
    if (p === '' || p === '.') continue;
    if (p === '..') {
      if (resolved.length > 0) resolved.pop();
      continue;
    }
    resolved.push(p);
  }
  return resolved;
}

function resolveHref(rawHref, sourceHtmlPath) {
  const h = stripFragQuery(rawHref.trim());
  if (h === '') return { skipped: true };

  // Source page's URL directory (relative to publicRoot).
  const sourceDir = path.dirname(sourceHtmlPath);
  const sourceRel = path.relative(publicRoot, sourceDir);
  const ownSegs = sourceRel ? sourceRel.split(path.sep).filter(Boolean) : [];
  const parentSegs = ownSegs.length > 0 ? ownSegs.slice(0, -1) : [];

  // Base interpretations to try. Root-relative hrefs use publicRoot as base.
  // Relative hrefs try BOTH the source's own dir (section-root interpretation)
  // and its parent dir (leaf-page interpretation, since Hugo resolves markdown
  // relative links against the source .md file's directory).
  const baseSets = h.startsWith('/') ? [[]] : [ownSegs, parentSegs];

  const candidates = [];
  for (const base of baseSets) {
    const resolved = resolveUrlSegments(base, h);
    pushCandidatesForSegments(candidates, resolved);
  }

  const seen = new Set();
  for (const cand of candidates) {
    if (seen.has(cand)) continue;
    seen.add(cand);
    try {
      if (fs.statSync(cand).isFile()) return { resolved: cand };
    } catch {
      // candidate doesn't exist — try next
    }
  }
  return { broken: true };
}

// Main scan.
let totalLinks = 0;
let skippedLinks = 0;
const broken = [];

for (const htmlFile of htmlFiles) {
  let content;
  try {
    content = fs.readFileSync(htmlFile, 'utf8');
  } catch {
    continue;
  }

  let match;
  anchorRe.lastIndex = 0;
  while ((match = anchorRe.exec(content)) !== null) {
    const rawHref = match[1] ?? match[2] ?? match[3] ?? '';
    totalLinks++;
    if (shouldSkip(rawHref)) {
      skippedLinks++;
      continue;
    }
    const result = resolveHref(rawHref, htmlFile);
    if (result.broken) {
      broken.push({
        source: path.relative(publicRoot, htmlFile),
        href: rawHref,
      });
    }
  }
}

console.log(`Scanned ${htmlFiles.length} HTML files, ${totalLinks} internal <a> links (${skippedLinks} skipped: external/anchor/js-template).`);

if (broken.length === 0) {
  console.log(`broken internal links: 0`);
  process.exit(0);
} else {
  console.log(`broken internal links: ${broken.length}`);
  for (const b of broken) {
    console.log(`  ${b.source}  ->  ${b.href}`);
  }
  process.exit(1);
}
