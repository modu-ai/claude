# claudemd-generator.md — CLAUDE.md 생성 원칙 (moai 개발 변형)

## 개요

moai 분기의 `CLAUDE.md`는 goose Desktop 변형(`skills/goose/references/claudemd-generator.md`)과 **완전히 분리된 소스**를 갖는다. 이 문서는 그 분리 원칙과, moai 분기가 실제 생성을 누구에게 위임하는지를 정의한다.

---

## 1. 두-템플릿 분리 (HARD)

PM 공통 템플릿(`skills/goose/references/templates/CLAUDE.md.tmpl` — 코워커 체인용)은 moai 분기에 **적용하지 않는다**. 코워커용 체인 템플릿(산출물 체인·office 스킬 우선·ai-slop 종료)과 개발용 오케스트레이터 지침(MoAI 위임·품질 게이트·SPEC 워크플로우)은 목적이 근본적으로 달라, 혼합하면 양쪽 모두 오염된다.

이 원칙은 `coder-setup.md` §Phase 3-1의 HARD 규칙과 쌍이다 — 셋업 시점(본 파일)과 생성 시점(coder-setup.md) 양쪽에서 같은 규칙이 적용된다.

---

## 2. CLAUDE.md 생성 소스 — 코더 플러그인 설치 시

코더 플러그인이 설치되어 있으면, moai 분기는 자체 템플릿을 갖지 않는다. `moai:moai-workflow-project` 정본이 대상 프로젝트의 `CLAUDE.md`를 생성하는 **유일한 소스**다. moai-pm의 moai 스킬은 인터뷰 결과(프로젝트 유형·스택·문서 언어·품질 게이트 깊이)를 코더 정본에 전달하는 어드바이저 역할만 수행한다.

---

## 3. CLAUDE.md 생성 소스 — 코더 플러그인 미설치 시 (가이던스 전용)

코더 플러그인이 없으면 moai 스킬은 `CLAUDE.md`를 직접 생성하지 않는다. 대신:

1. 설치 안내(`/plugin install moai@moai-cowork`)를 표시한다.
2. 임베디드 카탈로그 요약(`references/mcp-fallback-summary.md`)으로 어떤 MCP 서버·LSP 언어가 지원되는지 안내한다.
3. `product.md`/`structure.md`/`tech.md` 같은 문서 스캐폴드도 생성하지 않는다 — 이들 역시 코더 정본 소유다.

가이던스 전용 모드는 어떤 경우에도 실행 라우팅을 시도하지 않는다(moai SKILL.md §Namespace & Routing).

---

## 4. 사용자 요구 충돌 시 안내

사용자가 moai 분기에서 "코워커식 체인 CLAUDE.md"(산출물 체인·office 스킬 매핑 등)를 요구하면, 두-템플릿 분리를 설명하고 필요 시 같은 프로젝트에서 `/goose --project`를 병행 실행하도록 제안한다. 두 산출물(개발용 `CLAUDE.md` + 코워크용 워크플로우)은 서로 다른 관심사이므로 병행이 자연스럽다.

---

## 5. 참조 경로

- 코더 정본 위임 절차: `coder-setup.md` §Phase 3
- 임베디드 폴백 요약: `references/mcp-fallback-summary.md`
- goose Desktop 변형(참고, 이 스킬에는 적용 안 됨): `../../goose/references/claudemd-generator.md`
