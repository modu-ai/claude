# LSP Server Install Guide

Per-language install commands for every server declared in `plugins/moai/.lsp.json`. Guidance is macOS-first (Homebrew, `brew install`) with cross-platform notes (apt/npm/pip/gem/dotnet) per language, following REQ-L-005. The plugin never installs binaries automatically — it detects absence and points here (REQ-L-006 SessionStart advisory + the `/moai --project` init-time consumer owned by SPEC-MOC-PM-ADVISORS-001).

Every command below was verified against official upstream documentation this session (see `.moai/specs/SPEC-MOC-CODER-LSP-MCP-001/progress.md` §E.2 M1 for the exact source URLs and verification method).

### Go

- Binary: `gopls`
- macOS/Linux (Homebrew): `brew install gopls` (or `go install golang.org/x/tools/gopls@latest` if Go is already installed)
- Windows: `go install golang.org/x/tools/gopls@latest`

### Python

- Binary: `pyright-langserver`
- macOS (Homebrew): `brew install pyright`
- Cross-platform (npm): `npm install -g pyright`
- Cross-platform (pip): `pip install pyright`

### Rust

- Binary: `rust-analyzer`
- macOS/Linux/Windows: `rustup component add rust-analyzer`
- macOS (Homebrew alternative): `brew install rust-analyzer`

### Swift

- Binary: `sourcekit-lsp`
- macOS: bundled with Xcode Command Line Tools — `xcode-select --install`
- Linux: bundled with the official Swift toolchain (swift.org)

### TypeScript / JavaScript

- Binary: `typescript-language-server` (also serves `.js`/`.jsx`/`.mjs`/`.cjs` via the `typescript` entry's `extensionToLanguage` map — no separate JavaScript entry needed)
- Cross-platform (npm): `npm install -g typescript-language-server typescript`

### Java

- Binary: `jdtls` (Eclipse JDT Language Server, wrapper script)
- macOS (Homebrew): `brew install jdtls`
- Linux: search your distro's package repositories for `jdtls`/`eclipse.jdt.ls`, or download a milestone/snapshot build from `http://download.eclipse.org/jdtls/milestones/`
- **Requirement**: Java 21 minimum. Export `JAVA_HOME` in your shell profile (e.g. `~/.zshrc`/`~/.bashrc`) before starting Claude Code — `jdtls` inherits it from the launching shell's environment; the plugin's `.lsp.json` does not set it explicitly.

### C / C++

- Binary: `clangd`
- macOS (Homebrew): `brew install llvm` then add `$(brew --prefix llvm)/bin` to your `PATH` (no standalone `clangd` formula exists)
- Linux (Debian/Ubuntu, apt): `apt install clangd`
- Windows: install via the LLVM installer (llvm.org) or the clangd VS Code extension's bundled binary

### C#

- Binary: `csharp-ls`
- Cross-platform (dotnet tool, requires .NET 10 SDK): `dotnet tool install --global csharp-ls`
- Chosen over OmniSharp for active maintenance and MIT licensing (see progress.md §E.2 for the verification trail)

### PHP

- Binary: `phpactor`
- Cross-platform (standalone phar): `curl -Lo phpactor.phar https://github.com/phpactor/phpactor/releases/latest/download/phpactor.phar && chmod a+x phpactor.phar && mv phpactor.phar ~/.local/bin/phpactor`
- Cross-platform (Composer, from a git clone): `git clone https://github.com/phpactor/phpactor.git && cd phpactor && composer install`
- No Homebrew formula exists for phpactor — use the phar or Composer install above

### Kotlin

- Binary: `kotlin-lsp` (official JetBrains Kotlin LSP)
- macOS (Homebrew tap): `brew install JetBrains/utils/kotlin-lsp`
- Linux/other: download the standalone zip from `https://github.com/Kotlin/kotlin-lsp/releases`, `chmod +x kotlin-lsp.sh`, and symlink it onto your `PATH` as `kotlin-lsp`
- Note: this server is currently in JetBrains' Alpha state; the previous community `kotlin-language-server` (fwcd) remains a fallback if you need a more mature (but less actively maintained) alternative

### Ruby

- Binary: `ruby-lsp`
- Cross-platform (gem): `gem install ruby-lsp`

### HTML

- Binary: `vscode-html-language-server`
- Cross-platform (npm): `npm install -g vscode-langservers-extracted`

### CSS

- Binary: `vscode-css-language-server`
- Cross-platform (npm): `npm install -g vscode-langservers-extracted` (same package as HTML — installs both `vscode-html-language-server` and `vscode-css-language-server`)

## Non-blocking discovery

When a session starts and a language declared in `.lsp.json` matches files in your project but its server binary is missing from `PATH`, the plugin's SessionStart advisory hook (`plugins/moai/hooks/gates/lsp-binary-advisory.sh`) prints a non-blocking notice naming the language, the missing binary, and this file. The hook always exits 0 and never blocks your session (REQ-L-006/REQ-L-007).
