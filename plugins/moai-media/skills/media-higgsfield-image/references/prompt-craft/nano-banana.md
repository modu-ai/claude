# nano-banana.md — Nano Banana 계열 크래프트 (Google)

> 대상 모델(라이브 카탈로그 기준): `nano_banana_pro`, `nano_banana_2`, `nano_banana_2_lite`, `nano_banana`
> 파라미터·aspect·media role은 `models_explore(action:'get')`로 라이브 조회.

**Evidence tier:** 1차 (Google Cloud Blog · blog.google · ai.google.dev)
출처: https://ai.google.dev · https://blog.google

---

## 공식 구조 (1차)

`[Subject] + [Action] + [Location/context] + [Composition] + [Style]`
참조 구동 변형: `[Reference images] + [Relationship instruction] + [New scenario]`

사실적 템플릿(verbatim): *"A photorealistic [shot type] of a [subject] in a [setting]. [Light description]. Shot from a [angle] with a [lens type]."*

## 모델-세대 매핑 (1차, ai.google.dev)

- `nano_banana` = Gemini 2.5 Flash Image (레거시; Google은 이전 권장)
- `nano_banana_2` = Gemini 3.1 Flash Image
- `nano_banana_2_lite` = Gemini 3.1 Flash Lite Image
- `nano_banana_pro` = Gemini 3 Pro Image (프리미엄, "Thinking", 최고 텍스트 정확도)

## Creative Director 어휘 (verbatim)

- 조명: `three-point softbox setup` · `Chiaroscuro lighting with harsh, high contrast` · `Golden hour backlighting creating long shadows`
- 카메라: `low-angle shot with shallow depth of field (f/1.8)` · `wide-angle lens` · `macro lens`
- 하드웨어 에뮬레이션: GoPro(몰입/왜곡) · Fujifilm(정직한 색) · disposable camera(향수 플래시)
- 필름스톡: `1980s color film, slightly grainy` · `Cinematic color grading with muted teal tones`

## 텍스트 렌더링 (헤드라인 역량, R3)

리터럴 텍스트는 따옴표로, 폰트를 라인별로 지정한다. **"Text-first hack"**: 먼저 대화로 텍스트 내용을 확정한 뒤, 그 확정된 텍스트가 담긴 이미지를 요청한다.

## 파라미터 spelling caveat

Higgsfield의 `nano_banana_2_lite`는 `thinking[MINIMAL|HIGH]`로 노출되지만 Google 자체 enum은 `low`/`high`다. 개념은 전이되나 토큰 spelling은 다르다. 실제 허용 값은 언제나 `models_explore`로 확인한다.

## Google 자체 명시 한계 (verbatim)

*"Be aware of current limitations: text rendering, factual accuracy, and complex edits may need improvement."*
검색 그라운딩: Nano Banana Pro는 `google_search`를 호출해 인포그래픽을 실데이터로 근거화할 수 있다 — *"particularly valuable for weather visualizations, current events, or data-driven infographics."*
