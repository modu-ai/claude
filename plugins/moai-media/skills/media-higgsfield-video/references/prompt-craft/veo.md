# veo.md — Veo 계열 크래프트 (Google)

> 대상 모델(라이브 카탈로그 기준): `veo3`, `veo3_1`, `veo3_1_lite`
> 파라미터·aspect·duration·media role은 `models_explore(action:'get')`로 라이브 조회.

**Evidence tier:** 1차 (Google Cloud Blog · DeepMind Veo guide · ai.google.dev)
출처: https://cloud.google.com · https://ai.google.dev

---

## 공식 (1차, "Core Prompt Formula")

`[Cinematography] + [Subject] + [Action] + [Context] + [Style & Ambiance]`

레거시 Veo 3(DeepMind 가이드)는 **7요소**로 조직: shot framing & motion, style, lighting, character descriptions, location, action, dialogue.

## 오디오 문법 — 이 리서치 최고 가치 발견 (1차, verbatim)

| 채널 | 컨벤션 | 예시 |
|---|---|---|
| Dialogue | 큰따옴표 | `A woman says, "We have to leave now."` |
| Sound effects | `SFX:` 접두 | `SFX: thunder cracks in the distance` |
| Ambient | `Ambient noise:` 접두 | `Ambient noise: the quiet hum of a starship bridge` |

DeepMind 레거시 Veo 3 가이드는 독립 `Audio:` 블록(`Audio: Crunchy, sugary typing sounds, delighted giggles.`)과 `Character: "line"` 축약도 쓴다.

## 제외 표현 (R1)

verbatim: *"specify 'a desolate landscape with no buildings or roads' instead of 'no man-made structures'."* 부정 파라미터는 내보내지 않는다.

## 참조 일관성·프레임

"Ingredients to Video": 참조 이미지 최대 3장, *"Preserve the subject's appearance in the output video."* 참조 사용 시 Google API에서 길이가 8s로 강제된다.
first/last frame: start image + last frame으로 시작·끝 구성 제어 — MCP의 `start_image` / `end_image` role에 매핑(`veo3_1_lite`).
timestamp 세그먼트 멀티비트(`[00:00-00:02] ...`)는 각 비트가 자체 `SFX:`/`Emotion:` 태그를 갖는다.

## 주의 — Veo 3.1 컨벤션을 veo3에 역이식 금지

DeepMind Veo 3 가이드는 negative prompting이나 참조 이미지를 아예 다루지 않으며 오디오도 단일 일반 `Audio:` 블록뿐이다. **Veo 3.1의 풍부한 컨벤션을 `veo3`에 backfill하지 않는다.** 실제 파라미터·duration·role은 `models_explore`로 확인한다.
