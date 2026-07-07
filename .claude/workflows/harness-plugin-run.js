// harness-plugin-run.js — Runner for /harness:plugin
// Reads manifest.json (SSOT) and dispatches 4 specialists across the 6-Phase pipeline.
// Patterns: Pipeline (stage N feeds N+1) + Producer-Reviewer (curator evaluates).
//
// This is the generated dynamic-workflow Runner that executes INSIDE /harness:plugin.
// The Builder (creation) was orchestrator-direct; execution runs here.

export const meta = {
  name: 'harness-plugin-run',
  description: 'Runner for /harness:plugin — 6-Phase desktop plugin (cowork/code) skill generator with 3-Layer research',
  phases: [
    { title: 'Discovery', detail: 'intent-parser: natural-language → plugin + topic + intent' },
    { title: '3-Layer Research', detail: 'research-collector: qmd vault → Claude docs → web' },
    { title: 'Curation', detail: 'plugin-curator: 4-dimension rubric, top-5' },
    { title: 'Selection', detail: 'orchestrator AskUserQuestion gate' },
    { title: 'Build', detail: 'skill-builder: plugin skill under category constraints' },
    { title: 'Report', detail: 'test + final summary' },
  ],
}

const INTENT_SCHEMA = {
  type: 'object',
  properties: {
    target_plugin: { type: 'string', enum: ['cowork', 'code'] },
    skill_topic: { type: 'string' },
    intent: { type: 'string' },
    keywords: { type: 'array', items: { type: 'string' } },
    constraints: { type: 'array', items: { type: 'string' } },
  },
  required: ['target_plugin', 'skill_topic', 'keywords'],
}

const CURATION_SCHEMA = {
  type: 'object',
  properties: {
    top5: {
      type: 'array',
      items: {
        type: 'object',
        properties: {
          source: { type: 'string' },
          layer: { type: 'string', enum: ['qmd', 'docs', 'web'] },
          scores: {
            type: 'object',
            properties: {
              relevance: { type: 'number' },
              specificity: { type: 'number' },
              practicality: { type: 'number' },
              reusability: { type: 'number' },
            },
          },
          excerpt: { type: 'string' },
          value: { type: 'string' },
        },
      },
    },
  },
}

// Phase 1 — Discovery
phase('Discovery')
const intent = await agent(
  [
    'You are the intent-parser specialist for /harness:plugin.',
    'Parse the natural-language directive into a structured intent: target plugin (cowork or code), skill topic, intent, research keywords, and any constraints.',
    'The directive is NOT positional — it is free-form natural language. Infer target_plugin from domain cues (cowork = copy/content/business/non-dev; code = coding/dev/agentic).',
    'Return the structured object only.',
  ].join(' '),
  { label: 'intent-parser', phase: 'Discovery', schema: INTENT_SCHEMA, effort: 'medium' }
)
if (!intent) throw new Error('intent-parser returned no result')
log(`target=${intent.target_plugin} topic="${intent.skill_topic}"`)

// Phase 2 — 3-Layer Research
phase('3-Layer Research')
const research = await parallel([
  () => agent(
    [
      'You are the research-collector (Layer 1: qmd vault).',
      `Run: bash .claude/skills/harness-plugin/scripts/qmd-search.sh "${intent.keywords.join(' ')}" 10`,
      'Return the raw qmd output (markdown matches). If qmd is unavailable the script falls back to ripgrep automatically.',
    ].join(' '),
    { label: 'research:qmd', phase: '3-Layer Research', effort: 'medium' }
  ),
  () => agent(
    [
      'You are the research-collector (Layer 2: Claude official docs + best practices).',
      `Fetch code.claude.com/docs and docs.claude.com for content relevant to: ${intent.skill_topic} (${intent.target_plugin} plugin context).`,
      'Return structured excerpts with source URLs.',
    ].join(' '),
    { label: 'research:docs', phase: '3-Layer Research', effort: 'medium' }
  ),
  () => agent(
    [
      'You are the research-collector (Layer 3: web search, supplementary).',
      `Search the web for supplementary best practices on: ${intent.skill_topic}.`,
      'Return top results with URLs and one-line relevance.',
    ].join(' '),
    { label: 'research:web', phase: '3-Layer Research', effort: 'low' }
  ),
])
const layerResults = research.filter(Boolean)

// Phase 3 — Curation
phase('Curation')
const curation = await agent(
  [
    'You are the plugin-curator specialist (Producer-Reviewer evaluator).',
    'Score the collected research (3 layers) on 4 dimensions (Relevance / Specificity / Practicality / Reusability, 0–5 each).',
    'Weighted average = (R + S + P + U) / 4. Select top-5 by weighted average.',
    `Target plugin: ${intent.target_plugin}. Skill topic: ${intent.skill_topic}.`,
    'Return the top-5 structured object with scores + excerpts + one-paragraph value each.',
  ].join(' '),
  { label: 'plugin-curator', phase: 'Curation', schema: CURATION_SCHEMA, effort: 'medium' }
)

// Phase 4 — Selection (orchestrator-side AskUserQuestion gate; Runner emits the candidate list)
phase('Selection')
log(`top-5 curated for ${intent.target_plugin}/${intent.skill_topic} — orchestrator surfaces AskUserQuestion`)

// Phase 5 — Build
phase('Build')
const constraints = intent.target_plugin === 'code'
  ? 'ALLOWED categories: commands/, skills/, agents/. FORBIDDEN: hooks/, output-styles/, rules/, mcp-servers/.'
  : 'ALLOWED category: skills/ ONLY. FORBIDDEN: commands/, agents/, hooks/, output-styles/, rules/, mcp-servers/.'
const skill = await agent(
  [
    'You are the skill-builder specialist (opus/high).',
    `Build a ${intent.target_plugin} plugin skill for: ${intent.skill_topic}.`,
    `Category constraints — ${constraints}`,
    'Use the curated top-5 research as source material. Emit SKILL.md (+ references/ + allowed category dirs) under the target plugin path.',
    'Return the file paths created.',
  ].join(' '),
  { label: 'skill-builder', phase: 'Build', effort: 'high', model: 'opus' }
)

// Phase 6 — Report
phase('Report')
return {
  intent,
  layers_collected: layerResults.length,
  top5: curation?.top5?.length || 0,
  skill_built: skill,
}
