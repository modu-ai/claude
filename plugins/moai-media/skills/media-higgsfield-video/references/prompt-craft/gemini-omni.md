# gemini-omni.md — Gemini Omni Flash 크래프트 (Google)

> 대상 모델(라이브 카탈로그 기준): `gemini_omni`
> 파라미터·aspect·duration·media role은 `models_explore(action:'get')`로 라이브 조회.

**Evidence tier:** 1차 (ai.google.dev)
출처: https://ai.google.dev

---

## Veo와 정반대 철학 (1차, verbatim)

편집: *"Simple prompts work best for video editing. Overly descriptive prompts can lead to unintended changes."* 생성(편집 아님)에서는 camera movement·lighting·mood를 서술한다. (Veo는 상세할수록 좋고, Omni는 편집에서 단순할수록 좋다 — 정반대. core R4의 역방향 경고.)

## 참조 문법 — 정확한 인라인 토큰 (1차)

`<FIRST_FRAME>`가 시작 프레임을 지정, `<IMAGE_REF_N>`(0-indexed)가 스타일/주제 참조를 산문에 인라인 표기:
> *"in the style of `<IMAGE_REF_0>` a woman `<IMAGE_REF_1>` is walking"*

## Google 자신이 명시한 known-broken 경고 (verbatim)

*"Video references up to 3 seconds in duration are accepted by the API schema but are not correctly processed by the model at this time."* MCP는 이 모델에 `video_references` role을 노출한다. **스킬은 이 사실을 반드시 경고한다** — API가 받아들여도 모델이 제대로 처리하지 못한다.

## 오디오·타임코드

오디오는 Veo의 태그 문법이 아니라 **평이한 서술 언어** — *"Include calm background music"*, *"The audio is a low tinny radio broadcast in the background."*
타임코드 구조 지원: `[0-3s] A person is walking / [3-6s] They stop and turn around / [6-10s] They start running`
길이 상한은 Google 기준 10s. 실제 duration·role은 `models_explore`로 확인한다.
