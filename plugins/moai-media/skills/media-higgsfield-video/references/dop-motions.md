# dop-motions.md — 카메라 디렉팅 크래프트 + Marketing Studio 프리셋 참고

> `media-higgsfield-video` | 카메라 모션 언어(프롬프트 크래프트)와 Marketing Studio preset 슬러그 참고.
> 모델·파라미터·preset 슬러그는 하드코딩하지 않는다 — 런타임에 `models_explore` / `show_marketing_studio`로 조회한다. 이 파일의 슬러그 목록은 **예시(illustrative)이지 계약이 아니다.**

출처: https://github.com/higgsfield-ai/skills · https://higgsfield.ai/blog/marketing-studio-video-1

---

## Marketing Studio preset 슬러그 — 라이브 조회 (26개는 예시)

이전 이 파일은 "6가지 공식 비디오 프리셋" 표를 하드코딩했으나, 그것은 라이브 스키마와 어긋난 허구였다. `marketing_studio_video`의 preset은 `mode` 슬러그이며, 2026-07-12 `show_marketing_studio` 라이브 확인 시 **26개**였다. 아래는 **참고용 예시**이며, 런타임에는 반드시 `show_marketing_studio`로 실제 목록을 조회한다(카탈로그가 바뀌면 이 목록도 바뀐다):

`ugc` · `ugc_gadget_saved_me` · `ugc_giant_figure` · `ugc_unboxing_virtual_try_on` · `ugc_unboxing_asmr` · `ugc_virtual_try_on_sneakers` · `couple_sharing_home` · `ugc_selfie_testimonial` · `ugc_direct_to_camera` · `ugc_secret_hack_reveal` · `crush_test` · `hypermotion_oj` · `camera_pov` · `classic_meets_modern` · `mess_to_fresh` · `mystery_box` · `product_showcase` · `reboxing` · `tv_spot` · `ugc_addiction` · `ugc_before_and_after` · `ugc_how_to` · `ugc_unboxing` · `ugc_virtual_try_on` · `virtual_try_on` · `wild_card`

hook/setting 구성 규칙(상호 배타 등)은 `references/prompt-craft/marketing-studio.md`.

---

## 카메라 이동 언어 (프롬프트 크래프트 — 파라미터 아님)

카메라 디렉팅은 파라미터가 아니라 프롬프트 산문으로 표현한다. 계열별 세부는 각 `prompt-craft/*.md`.

### 카메라 이동의 감정 의도 (Wan 공식, core R 참고)

| 이동 | 의도 |
|---|---|
| Push-in | intimacy / tension |
| Pull-out | scale / isolation |
| Tracking | viewer alongside subject |
| Orbit | subject importance |
| Fixed | stillness / focus |

### 자연어 카메라 용어 (계열 공통)

close-up · low angle · slow push-in · tracking shot · wide establishing shot · macro · dolly · crane. 추상적 내면 상태("feels tense")가 아니라 시각적 상관물로 서술한다.

### MiniMax 브래킷 카메라 미니언어 (참고 — `minimax_hailuo`)

`[Truck left]` `[Pan left]` `[Push in]` `[Pull out]` `[Pedestal up]` `[Tilt up]` `[Zoom in]` `[Shake]` `[Tracking shot]` `[Static shot]` 등. 한 `[]` 안에 여러 명령을 넣으면 동시 적용(권장 최대 3). 순서는 서사 순으로. 주의: MiniMax의 silent-override 위험은 video `SKILL.md` 위험 블록 참조.

---

## 채널별 비율·길이 (참고)

정확한 aspect_ratios·durations는 모델별로 다르며 `models_explore(action:'get')`로 조회한다. 대략:

| 채널 | 비율 | 대략 길이 |
|---|---|---|
| 인스타/유튜브 가로 | 16:9 | 6–15s |
| 릴스·숏폼·틱톡 | 9:16 | 5–10s |
| 정사각 SNS | 1:1 | 5–10s |

Marketing Studio는 기본이 landscape이므로 숏폼은 `9:16`을 명시적으로 전달한다(→ `prompt-craft/marketing-studio.md`).
