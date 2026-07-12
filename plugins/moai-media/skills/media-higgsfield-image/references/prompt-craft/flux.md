# flux.md — FLUX 계열 크래프트 (Black Forest Labs)

> 대상 모델(라이브 카탈로그 기준): `flux_2`, `flux_kontext`
> 파라미터·aspect·media role은 `models_explore(action:'get')`로 라이브 조회.

**Evidence tier:** 공식·텍스트·Kontext 편집은 1차 (docs.bfl.ai). pro/flex/max 기능 분화는 2차-adjacent.
출처: https://docs.bfl.ai

---

## 공식 (1차, docs.bfl.ai)

`Subject + Action + Style + Context`
풀 슬롯 템플릿: `[SUBJECT], [LOCATION], [STYLE], [CAMERA SETTINGS], [LIGHTING], [COLORS], [EFFECT], [ADDITIONAL ELEMENTS]` — 명시적으로 *"a prompt-building aid, not a rule."*

**어순이 load-bearing(verbatim):** *"FLUX.2 pays more attention to what comes first."* 우선순위: 주 subject → 핵심 action → 결정적 style → 필수 context → 부차 detail.

**길이**: 10–30 words(탐색) / **30–80 words(대개 이상적)** / 80–300+(복잡). 캡: 32K 토큰(FLUX.2), 512 토큰(레거시 Kontext).

## 텍스트 렌더링 (R3)

정확한 문구를 따옴표로(`The text "OPEN" appears in red neon letters`). 색을 객체에 **hex 코드**로 바인딩(`the car in color #0047AB`).

## R1 예외 주의 — FLUX.2는 부정 프롬프트를 지원하지 않는다

FLUX.2는 negative prompt를 아예 지원하지 않는다(공통 규칙 R1의 근거 벤더 중 하나). 제외는 긍정 장면 묘사로 표현한다 — "no blur" 대신 "sharp focus throughout", "no people" 대신 "an empty scene". 스킬은 어떤 호출에도 부정 파라미터를 내보내지 않는다.

## Kontext 편집 컨벤션 (1차, verbatim 예시, R4)

- `"Change the car color to red"` · `"Remove the object from her face"` · `"It's now snowing, everything is covered in snow"`
- 텍스트 편집: `Replace '[original text]' with '[new text]'`
- **동사 선택이 중요**: *"change"*는 정체성 보존; *"transform"*은 무자격 시 전면 정체성 교체 신호.
- 앵커링: *"Change the background to a beach while keeping the person in the exact same position, scale, and pose"* — 맨 지시는 의도치 않게 subject 위치/스케일/프레이밍을 이동시킨다.

## variant 가이드

`pro` = 프로덕션 범용 · `flex` = 타이포그래피/미세 디테일 특화 · `max` = 최고 편집 일관성 + 최강 프롬프트 준수. **프롬프트 크래프트는 variant별로 구조가 달라지지 않는다** — 품질 상한과 노출 knob만 다르다. 실제 variant 값은 `models_explore`로 확인한다.

**Do**: camera/lens/film stock 명시(*"Shot on Fujifilm X-T5, 35mm f/1.4"*); 대상 시장 모국어로 프롬프트; 각 참조 이미지의 역할 라벨링("subject from image 1, style from image 2").
