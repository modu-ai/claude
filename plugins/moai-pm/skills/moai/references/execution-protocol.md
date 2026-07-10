# execution-protocol.md — 초기화 실행 핸드오프 (moai)

## 개요

moai 스킬이 초기화 산출물을 생성한 뒤, 실행을 코더 플러그인으로 핸드오프하거나(설치 시) 가이던스 전용으로 마무리하는(미설치 시) 프로토콜이다.

---

## 1. 실행 핸드오프 흐름

```
0. [Evaluate] 요청이 개발-프로젝트 초기화인지 판단(router.md)
1. [Interview] 소크라테스 인터뷰 + 스택 감지(moai SKILL.md §Socratic Interview & Stack Detection)
2. [Plan+Confirm] 생성 계획 제시 → AskUserQuestion으로 승인
3. [Generate] CLAUDE.md/agents/skills/settings.json/hooks/.mcp.json 생성
4. [Handoff] 코더 플러그인 설치 시 → 실행을 moai:moai로 라우팅
             코더 플러그인 미설치 시 → 가이던스 전용 안내로 종료(실행 라우팅 시도 안 함)
```

---

## 2. 품질 게이트 소비

moai 스킬 자체는 품질 게이트를 실행하지 않는다 — 코더 정본의 게이트를 **소비**한다:

- **plan**: LSP baseline 캡처(코더 정본이 실행)
- **run**: 0 errors / 0 type-errors / 0 lint-errors(코더 정본 quality.yaml)
- **sync**: sync-auditor 독립 4차원 평가(Functionality/Security/Craft/Consistency)

moai 스킬의 역할은 초기화 시점에 이 게이트가 정상 배선되도록 `.claude/hooks/`와 `.moai/config/sections/quality.yaml`을 생성하는 것으로 끝난다.

---

## 3. 재진입 확인 (S3, execution 관점)

이미 초기화된 프로젝트에서 `/moai --project`가 재실행되면, 기존 `.claude/`·`.moai/`·`CLAUDE.md`를 덮어쓰기 전에 `AskUserQuestion`으로 확인한다(재생성 / 부분 갱신 / 취소). 부분 갱신 선택 시 변경된 항목만 Edit로 갱신하고 나머지는 보존한다.

---

## 4. 에러 처리

초기화 중 코더 플러그인 위임이 실패하면(예: `moai-workflow-project` 스킬 로드 실패), 가이던스 전용 모드로 폴백하고 사용자에게 원인을 보고한다. 초기화 자체를 하드 실패시키지 않는다.
