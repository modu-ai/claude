# router.md — moai 라우팅 프로토콜 (개발 프로젝트 초기화)

## 개요

사용자의 자연어 요청을 분석해 개발-프로젝트 초기화 요청을 moai 스킬로 라우팅하는 프로토콜이다. 비개발 요청(사업·콘텐츠·디자인 등)은 `goose`(`/goose --project`)로 안내한다.

---

## 1. 모드 판정 키워드

| 키워드 | 라우팅 |
|--------|------|
| 개발환경 셋업, MoAI-ADK, SPEC, EARS/GEARS, DDD, TDD, 리팩토링, 품질 게이트, 백엔드, 프론트엔드, API, 코딩 | `/moai --project` → moai 스킬 |
| 그 외 전부(사업·콘텐츠·창작·커머스·문서·법무·재무·채용·교육·디자인) | `/goose --project` 안내 |

---

## 2. moai 자체 관리 도메인

| 도메인 | 키워드 |
|--------|--------|
| 초기화·라우팅 | 개발 프로젝트 초기화, /moai --project, CLAUDE.md 생성(dev-init) |
| 관리 | /moai resume, catalog, status, apikey, doctor |
| 코더 실행 위임 | `/moai project`(공백 서브커맨드) — 코더 플러그인 소유, moai 스킬은 라우팅만 수행 |

---

## 3. 모호성 해소

모드 자체(goose/moai)가 불명확할 때만 `AskUserQuestion` 2옵션(goose 권장 / moai)을 제시한다. 개발 관련 키워드가 명시되면 즉시 moai로 진입한다.

---

## 4. 검증 깊이 연동

moai가 생성하는 산출물은 코더 정본의 품질 게이트(plan: LSP baseline 캡처, run: 0 errors, sync: sync-auditor 4차원 평가)를 따른다 — 상세는 `execution-protocol.md` 참조. Desktop의 QUICK/NORMAL/DEEP 검증 깊이 사다리는 moai 분기에 적용되지 않는다(개발 산출물은 코더 정본 품질 게이트가 별도로 관장).
