# cinema-studio.md — Cinema Studio 계열 크래프트 (Higgsfield)

> 대상 모델(라이브 카탈로그 기준): `cinematic_studio_3_0`, `cinematic_studio_video_v2`, `cinematic_studio_video`, `cinematic_studio_2_5`(이미지)
> 파라미터 enum·aspect·duration·media role은 `models_explore(action:'get')`로 라이브 조회.

**Evidence tier:** 구조·메커니즘·예시는 1차 (higgsfield.ai/blog/cinema-studio-3.0). 파라미터 enum은 none-found(벤더 설계상 부재).
출처: https://higgsfield.ai/blog/cinema-studio-3.0

---

## 참조 시스템 (1차) — 4계층

1. 참조 업로드에 `@image_1`, `@image_2`, `@video` 태그
2. 명시적 **번호 매긴 샷 분해**가 있는 씬 서술
3. 기술 스펙 블록(camera movement, lighting, composition)
4. 캐릭터/환경 일관성 마커

**길이**: 예시가 50단어(단순) → **500+ 단어**(복잡 멀티샷). 이는 Higgsfield 자체 약 200-토큰 일반 상한과 모순된다(→ core `universal-rules.md` R5). 있는 그대로 보고, 화해시키지 않는다.

## 모션 전이 — 문서화된 리터럴 문법 (verbatim)

`"In @video change location to @image_1. [Genre/context description]."`
→ *"relights the subject accurately and copies the motion perfectly, no manual masking."*

## 빈 프롬프트 배치 (verbatim)

*"Leave the prompt empty. Select your character and your location. Cinema Studio handles the rest"* — 기본 키프레임용.

**멀티 캐릭터**: 각각 `@image_1`, `@image_2`, `@image_3`로 태그해 한 프롬프트에; 시스템이 *"places them together, assigns correct lighting, and holds every face consistent across cuts."*
**연속**: 이전 영상을 컨텍스트로 업로드하고 다음 비트만 쓴다.

## 파라미터 enum은 라이브 조회

`genre` / `multi_shots` / `speedramp` / `cfg_scale` / `preset_id` 등의 enum은 어떤 정적 Higgsfield 문서에도 없다. 벤더 agent 문서가 직접 지시한다: **"When unsure, run `higgsfield model get <model>` and inspect the schema."** — 벤더 스스로 이 스킬의 live-lookup 설계를 승인하는 셈이다. enum은 MCP에만 있다. 실제 값은 `models_explore`로 확인한다.
