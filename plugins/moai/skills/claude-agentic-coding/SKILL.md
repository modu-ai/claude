---
name: claude-agentic-coding
description: 개발자용 Claude agentic 코딩 — tool use, sub-agents, MCP 연동으로 자율 코딩 워크플로우 구성. Claude 공식 tool-use/sub-agents 문서 기반. "Claude로 자율 코딩 에이전트 만들고 싶어" 질문에 즉시 활용.
version: "3.1.0"
metadata:
  category: coder
  status: active
  updated: 2026-07-09
  tags: "agentic, tool-use, sub-agents, mcp, coding"
  source: "https://code.claude.com/docs/en/tool-use, https://code.claude.com/docs/en/sub-agents"
---

# claude-agentic-coding — 개발자용 Agentic 코딩

> coder 플러그인 스킬 — coder는 무설치 harness 정본(D4)으로 `moai-adk-go` 템플릿과의 무설치 완전 패리티를 위해 `commands/`·`skills/`·`agents/`·`hooks/`·`output-styles/`·`rules/`·`mcp` 전 카테고리를 사용합니다.

## 핵심 3축 (Claude 공식)

### 1. Tool Use — Claude가 행동하게
- **명시적 동사로 트리거**: "이 함수 수정해줘" (수행) vs "어떻게 수정하면 좋을까?" (제안만).
- **과도한 tool 프롬프트 금지**: "CRITICAL: 반드시 이 도구 써" → 오히려 과트리거. "이 도구는 ~할 때 써" 수준이 4.5+에선 적절.
- **병렬 tool 호출**: 독립 호출은 한 턴에 병렬로. 의존성 있을 때만 순차.

### 2. Sub-Agents — 분업으로 컨텍스트 분리
- **독립 작업은 서브에이전트로 위임**: 코드 조사, 리서치 등은 메인 컨텍스트를 차지하지 않게 서브에이전트로. 결과만 반환.
- **서브에이전트는 사용자 프롬프트 불가**: blocker report 구조로 반환 → 메인 오케스트레이터가 사용자 응답 후 재위임.
- **용도별 역할 부여**: "코드 조사 에이전트", "테스트 작성 에이전트" 등 단일 책임.
- 본 스킬의 `agents/code-investigator.md`가 예시 서브에이전트.

### 3. MCP — 외부 도구 연동
- **MCP 서버로 확장**: DB, API, 브라우저 자동화 등을 Claude 도구로 노출.
- **권한 최소화**: MCP 서버는 필요 도구만 노출 (보안).
- 구성: `.mcp.json` 또는 Claude Desktop 설정.

## Agentic 워크플로우 패턴

```
[사용자 요청]
    ↓
[메인 오케스트레이터 — 계획·승인 게이트]
    ↓ (병렬 위임)
[code-investigator]  [tester]  [reviewer]
    ↓                   ↓          ↓
    └─────── 결과 취합 ──────────┘
                ↓
        [구현 · 검증 · 보고]
```

## 실전 원칙 (Claude 4.8+)

- **Literal instruction following**: 한 항목에 대한 지시를 다른 항목에 자동 일반화 안 함. "모든 섹션에 적용"처럼 범위 명시.
- **Subagent 스폰 조절**: 4.8은 기본적으로 서브에이전트를 적게 스폰. fan-out 필요 시 "여러 서브에이전트를 한 턴에 병렬 스폰" 명시.
- **Adaptive thinking**: `thinking: {type: "adaptive"}`. `budget_tokens` 금지 (HTTP 400). 노력은 `effort`로 (xhigh 코딩).
- **안전 vs 자율**: 로컬 가역(파일 편집, 테스트)은 자유롭게; 하드-리버서블(강제 push, rm -rf, 배포)은 확인.

## 구성

- `commands/claude-agentic-coding.md` — `/claude-agentic-coding` 진입 (thin wrapper)
- `agents/code-investigator.md` — 코드 조사 서브에이전트 예시
- 본 SKILL.md — 가이드

## 참고

- Claude 공식 tool use: https://code.claude.com/docs/en/tool-use
- Claude 공식 sub-agents: https://code.claude.com/docs/en/sub-agents
- MCP: https://modelcontextprotocol.io
- 본 스킬은 `/harness:plugin` 하네스(skill-builder)가 Claude 공식 문서 기반으로 생성한 coder 플러그인 스킬입니다.
