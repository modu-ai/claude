# grok.md — Grok 계열 크래프트 (xAI)

> 대상 모델(라이브 카탈로그 기준): `grok_video`, `grok_video_v15`, `grok_image`
> 파라미터·aspect·duration·media role은 `models_explore(action:'get')`로 라이브 조회.

**Evidence tier:** 1차 — an evidenced absence, directly verified (docs.x.ai 직접 fetch).
출처: https://docs.x.ai

---

## 증거로 확인된 부재 — 이 계열의 헤드라인 발견 (No Official Formula)

`docs.x.ai`(video generation, reference-to-video, image generation)를 직접 fetch한 결과:
- **프롬프트 구조 공식 없음** (공식 프롬프트 공식이 존재하지 않는다)
- **길이 권장 없음**("a prompt that is too long"만 오류 조건으로 언급, 숫자 없음)
- **negative-prompt 필드/컨벤션 없음**
- **no audio documentation** — 오디오·대사·사운드 디자인에 대한 언급이 어디에도 없다

마지막 지점은 MCP 카탈로그가 `grok_video_v15`를 *"native audio direction"* 보유로 태깅한 것과 **정면 모순**된다. xAI 공개 문서에는 오디오에 대한 no audio documentation — 아무 내용도 없다. Grok 오디오 프롬프팅 기법이라며 도는 모든 주장은 **서드파티 가이드 전용**(xAI 아님)이다.

**스킬은 Grok 오디오 컨벤션을 지어내지 않는다.** R1–R5(core `universal-rules.md`) + 관측된 공식 예시로 폴백한다.

## 공식 예시 (verbatim, docs.x.ai — 라벨 없는 평이한 단문)

- *"A glowing crystal-powered rocket launching from the red dunes of Mars, ancient alien ruins lighting up in the background as it soars into a sky full of unfamiliar constellations."*
- *"Timelapse of a flower blooming in a sunlit garden."*
- image-to-video: *"Make the water crash down and slowly pan out the camera."*

## 참조 문법 주의

xAI는 자체 `reference_images` 배열에 묶인 `<IMAGE_2>` 플레이스홀더를 쓴다. **Higgsfield는 단일 `start_image` role만 노출** — 번호 플레이스홀더 컨벤션은 깔끔히 매핑되지 않으며 동작을 가정하지 않는다. 실제 role·param은 `models_explore`로 확인한다.
