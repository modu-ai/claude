---
title: "설치하기"
weight: 10
description: "Claude Code 설치 방법 — macOS/Windows 단계별 가이드."
geekdocBreadcrumb: true
aliases: ["/code/install/"]
---

## 준비물

Claude Code를 설치하기 전에 다음을 준비하세요:

| 항목 | 확인 |
|---|---|
| **Node.js 18 이상** | `node --version`으로 확인 (버전 18+ 필요) |
| **npm** | Node.js와 함께 설치됨 (`npm --version`으로 확인) |
| **Anthropic API 키** | [console.anthropic.com](https://console.anthropic.com)에서 발급 |
| **터미널** | Terminal (macOS) 또는 PowerShell (Windows) |

## 설치 단계

### 1단계: Node.js 버전 확인

터미널을 열고 다음을 입력하세요:

```bash
node --version
npm --version
```

**Node.js 18 이상**이 설치되어 있으면 다음 단계로 이동하세요.

Node.js가 설치되지 않았다면 [nodejs.org](https://nodejs.org/)에서 다운로드하세요 (LTS 버전 권장).

### 2단계: Claude Code 설치

다음 명령어를 실행하세요:

```bash
npm install -g @anthropic-ai/claude-code
```

### 3단계: 설치 확인

설치가 완료되었는지 확인하세요:

```bash
claude --version
```

버전 번호가 표시되면 설치 완료입니다.

### 4단계: Anthropic API 키 설정

Anthropic API 키를 환경변수로 설정해야 합니다.

{{< terminal title="터미널에서 (macOS/Linux)" >}}
export ANTHROPIC_AUTH_TOKEN="sk-ant-..."
{{< /terminal >}}

API 키는 [console.anthropic.com/account/keys](https://console.anthropic.com/account/keys)에서 생성할 수 있습니다.

**Windows PowerShell 사용자:**

```powershell
$env:ANTHROPIC_AUTH_TOKEN="sk-ant-..."
```

## Claude Code 시작하기

설치가 완료되었으면 다음 명령어로 시작하세요:

```bash
claude
```

Claude Code 터미널이 열립니다. 이제 [첫 작업 실행](./first-task.md)으로 이동하세요.

## 플랫폼별 추가 설정

### macOS

특별한 추가 설정은 필요하지 않습니다. Terminal 앱에서 위 단계를 따르면 됩니다.

### Windows

PowerShell을 **관리자 권한으로** 실행하고 위 단계를 따르세요.

**Git Bash 사용자:** 아래와 같이 설정하세요:

```bash
export ANTHROPIC_AUTH_TOKEN="sk-ant-..."
```

## 문제 해결

| 문제 | 원인 | 해결 방법 |
|---|---|---|
| `command not found: claude` | Claude Code 경로가 PATH에 없음 | npm install -g를 다시 실행 |
| `API key not found` | ANTHROPIC_AUTH_TOKEN이 설정되지 않음 | 위 4단계 재확인 |
| `node: command not found` | Node.js 미설치 | nodejs.org에서 설치 |

---

### 다음 단계

- **[첫 작업 실행](./first-task.md)** — Claude Code에서 첫 번째 프로젝트 시작
