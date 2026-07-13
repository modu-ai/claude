# moai references — 전체 인덱스

`plugins/moai-pm/skills/moai/references/`의 레퍼런스 파일 인덱스. moai는 개발-프로젝트 초기화 어드바이저다 — moai-adk v3.0 철학(SPEC plan/run/sync, TRUST 5, DDD/TDD)을 담당한다.

## 진입점

- 진입점은 `/moai --project <지시>`. 소크라테스 인터뷰 + 스택 감지 → 코더 플러그인 설치 확인 → MoAI-ADK 3.0 baseline 설치(또는 가이던스 전용 축소 모드) → SPEC 워크플로우 안내.
- 코더 플러그인의 `/moai project`(공백 서브커맨드, product/structure/tech.md 생성)와는 별개 진입점이다(SKILL.md §Namespace & Routing 참조).

## 파일 인덱스

| 파일 | 역할 |
|------|------|
| `router.md` | 자연어 → moai 스킬 라우팅(개발 키워드 매핑) |
| `coder-setup.md` | 5-Phase 정본(유형 인터뷰 → 설치 확인 → 정본 스캐폴드 → 언어·MCP → SPEC 안내) |
| `init-protocol.md` | 인터뷰 스키마·설치 확인·재개(Re-entry) 상세(dev-init 섹션) |
| `execution-protocol.md` | 초기화 실행 핸드오프·품질 게이트 소비 |
| `claudemd-generator.md` | 두-템플릿 분리(HARD) · CLAUDE.md 생성 위임 원칙 |
| `mcp-fallback-summary.md` | 코더 플러그인 부재 시 임베디드 카탈로그 폴백 요약(REQ-M-006) |

## 소유권 원칙

moai 스킬은 **어드바이저**다 — 실제 SPEC plan/run/sync 워크플로우·품질 게이트·LSP/MCP 카탈로그는 코더 플러그인(`plugins/moai`, SPEC-MOC-CODER-LSP-MCP-001)이 소유한다. 이 인덱스의 각 문서는 코더 정본을 **소비**하는 방법을 설명하며, 내용을 복제하지 않는다.
