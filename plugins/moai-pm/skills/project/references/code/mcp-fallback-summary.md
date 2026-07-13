# mcp-fallback-summary.md — 임베디드 카탈로그 폴백 요약 (REQ-M-006)

## 개요

코더 플러그인(`plugins/moai`)이 설치되어 있지 않을 때, moai 스킬은 `plugins/moai/references/dev-mcp-catalog.json`(SPEC-MOC-CODER-LSP-MCP-001 소유)을 읽을 수 없다. 이 문서는 그 카탈로그의 **정적 스냅샷 요약**을 임베드하여, 가이던스 전용 축소 모드에서도 사용자에게 "설치하면 무엇을 얻는지"를 안내할 수 있게 한다.

**중요**: 이 요약은 카탈로그와 **드리프트 가능한 사본**이다(plan.md 열린 위험 #1 — sync 메커니즘 미지정). moai 스킬은 이 요약을 실제 `.mcp.json` 생성에 절대 사용하지 않는다 — 코더 플러그인 미설치 상태에서는 `.mcp.json` 자체를 생성하지 않는다(안내 전용).

---

## 카탈로그 스냅샷 (참고용, 2026-07-11 관측)

| 서버 | entry_type | transport | 용도 |
|---|---|---|---|
| `playwright` | server | (카탈로그 참조) | 브라우저 자동화(코드 기반) |
| `supabase` | server | (카탈로그 참조) | Supabase 프로젝트 연동 |
| `vercel` | server | (카탈로그 참조) | Vercel 배포 연동 |
| `neon` | server | (카탈로그 참조) | Neon Postgres 연동 |
| `railway` | server | (카탈로그 참조) | Railway 배포 연동 |
| `claude-in-chrome` | **guidance-only** | none | Claude Code 내장 브라우저 자동화 — `.mcp.json` 서버 항목 생성 대상 아님, 확장/설정으로 활성화 |

`entry_type: "guidance-only"` 서버는 `.mcp.json`에 서버 항목이 생성되지 않는다(moai SKILL.md §MCP Survey 참조) — 이 규칙은 카탈로그 소비 시점과 이 폴백 요약 양쪽에서 동일하게 적용된다.

---

## 안내 문구 (가이던스 전용 모드에서 표시)

```
코더 플러그인(moai)이 설치되어 있지 않아, MCP 서버 자동 구성을 진행할 수 없습니다.

설치 후 사용 가능한 MCP 서버(참고 스냅샷): playwright, supabase, vercel, neon, railway
(claude-in-chrome은 서버 설정 없이 내장 기능으로 활성화됩니다.)

설치: /plugin install moai@moai-claude
설치 후: /moai resume
```

---

## 갱신 정책

이 파일은 SPEC-MOC-CODER-LSP-MCP-001의 카탈로그가 변경될 때 수동으로 재동기화해야 한다. 자동 동기화 메커니즘은 정의되어 있지 않다(plan.md 열린 위험 #1, 아직 미해결). 카탈로그와의 드리프트가 의심되면 `plugins/moai/references/dev-mcp-catalog.json`을 정본으로 재확인한다.
