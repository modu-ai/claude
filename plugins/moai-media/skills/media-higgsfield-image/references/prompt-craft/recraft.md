# recraft.md — Recraft 계열 크래프트

> 대상 모델(라이브 카탈로그 기준): `recraft_v4_1`
> 파라미터·aspect·media role은 `models_explore(action:'get')`로 라이브 조회.

**Evidence tier:** 프롬프트 구조·벡터 컨벤션은 1차 (recraft.ai docs). 색 파라미터 스키마는 **unverified**(JS 렌더 Swagger).
출처: https://www.recraft.ai

---

## 공식 구조 (1차) — "global to local", 8단계

핵심 컨셉 → 배경/환경 → subject 프레이밍/포즈 → 물리적 속성 → 부차 subject & 공간 관계 → 조명 방향/거동 → 카메라/심도/대비 → 무드 & 구성 해상도.

**명시 원칙(verbatim):** *"Structured prompts don't make results 'better'. They make outcomes intentional, controllable, and repeatable."*

## 벡터 / 로고 / 아이콘 프롬프팅 (`model_type` 차별자, 1차)

- **벡터 작업에는 texture/material 언어를 아예 피한다.**
- 정의: graphic type, shape logic & silhouette clarity, 엄격한 컬러 팔레트, line discipline(*"consistent stroke, no texture"*), 레이아웃 구조, 명시 제약(*"no gradients, no shadows"*).
- **디자이너가 알아듣는 용어를 쓴다** — 모델이 그 위에 학습됨: `contained mark` · `horizontal lockup` · `lettermark` · `negative space cutout` · `monoline style` · `ornate decorative border` · `serif letterforms`.
- 벤더 경고(verbatim): *"general prompts like 'a logo for a coffee shop' will produce something, but it probably won't be what you want."*

## 예시 (verbatim)

- *"Minimalist [subject] logo centered in composition, circular icon with brand name integrated as negative space cutout"*
- *"Line art icon logo...simple outline..., consistent stroke width, monoline style, clean and minimal, works at small sizes"*

## 컬러 팔레트

프롬프트 + 명시 hex를 결합 — *"a cityscape using yellow and blue as the primary colors, with deep blue (#1b027c) as the background and bright yellow (#f3e804) as the building accents."*

**Gap**: Recraft의 정확한 색 파라미터 스키마는 벤더 페이지에서 확인 불가(JS 렌더 Swagger). MCP가 선언하는 `#RRGGBB` 문자열 형식이 실운영 계약이다 — "라이브 스키마를 신뢰하라"의 또 다른 사례. 실제 파라미터는 `models_explore`로 확인한다.
