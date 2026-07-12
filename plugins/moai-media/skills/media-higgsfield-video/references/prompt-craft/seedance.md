# seedance.md — Seedance 계열 크래프트 (ByteDance)

> 대상 모델(라이브 카탈로그 기준): `seedance_2_0`, `seedance_2_0_mini`, `seedance1_5`
> 파라미터·aspect·duration·media role은 `models_explore(action:'get')`로 라이브 조회.

**Evidence tier:** 1차 (BytePlus ModelArk EN + Volcengine ZH 교차 확인)
출처: https://docs.byteplus.com/en/docs/ModelArk/2222480

카탈로그에서 가장 풍부하게 문서화된 프롬프팅 시스템이자, **플랫폼 가이드가 틀린** 계열이다(→ Higgsfield 블로그는 타임스탬프를 권하지만 ByteDance는 반대).

---

## 공식 (1차)

`Precise subject + action details + scene/environment + lighting & color tone + camera movement + visual style + image quality + constraints`
가이드는 프롬프트를 **"engineering-style instructions"**로 규정한다(창작 글쓰기가 아님).
Seedance 1.5 Pro: `Subject + motion + environment + camera movement/cuts + aesthetic description + sound`(뒤 4개 선택).

## 타임스탬프는 unstable — 공식, verbatim

> *"The model's support for precise timing (such as 0–3 seconds) is unstable, and forcibly limiting duration may lead to abnormal generation results."*
> *"Do not impose strict limits on the duration of each segment; prioritize allowing the model to naturally generate the pacing."*

공식 멀티샷 컨벤션은 **단순 라벨 샷 리스트**(`Shot 1 / Shot 2 / Shot 3`)로, **타임스탬프 없음**, 고정 비트 수 없음, 총 길이/샷 수/비율 선언 헤더 없음. ("상단에 샷 수+길이+비율 선언" 규칙은 ByteDance가 아니라 Higgsfield 블로그 관행이다.) → 이것이 Wan과 정반대인 지점(`wan.md` 참조).

## @-mention 참조 시스템 (1차, verbatim)

- `Reference <Subject_N> in <Image_N> to generate...` / `Reference <Action/Camera_movement/Style/Sound_effect> in <Video_N>`
- 실무(공식 사례)에서 `@Image 1` / `@Video 1` / `@Audio 1`로 산문에 인라인, **각자 용도를 명시** — "use the girl in @Image 1 **as the main character**", "use @Image 2 **as the dormitory scene style reference**".
- 이는 API 필드가 아니라 프롬프트 TEXT다 — Higgsfield `prompt` 문자열로 직접 전이된다. `medias[]` role은 *어느 파일*이 Image 1/Video 1인지 바인딩하고, *용도 진술*은 산문에 남는다.

## 브래킷 컨벤션 (1차, "Special Formatting Standards")

| 채널 | 구분자 |
|---|---|
| Music | `（parentheses）` |
| Sound effects | `<angle brackets>` |
| Dialogue | `{curly braces}` |
| Subtitles | `【square brackets】` |

공식 예시: `{How did the exam go? Did you pass?}`.

## 캐릭터 드리프트 회피 (1차)

- *"Use 2–3 clear and stable static features … to describe the subject."*
- *"Too Many Reference Characters: Limit to 4; generate in groups if needed."*
- 권장 asset 예산: 캐릭터 1–2 + 씬 1 + 카메라 참조 영상 1 + 오디오 1. 슬롯을 다 채우면 *"feature prioritization confusion."*

**Gap(부재 확인)**: 널리 도는 오디오 품질 키워드(reverb/muffled/echo)는 ByteDance 소스 어디에도 없음 — 서드파티 전용. 지어내지 않는다. 실제 param·role은 `models_explore`로 확인한다.
