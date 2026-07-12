# wan.md — Wan 계열 크래프트 (Alibaba Tongyi)

> 대상 모델(라이브 카탈로그 기준): `wan2_6`, `wan2_7`
> 파라미터·aspect·duration·media role은 `models_explore(action:'get')`로 라이브 조회.

**Evidence tier:** 1차 (Alibaba Cloud Model Studio + GitHub Wan-Video, 직접 fetch·검증)
출처: https://help.aliyun.com/zh/model-studio · https://github.com/Wan-Video

카탈로그에서 뜻밖에 가장 잘 문서화된 non-Higgsfield 계열. Alibaba Cloud Model Studio가 **여러 명명 공식**을 발행한다.

---

## 명명 공식 (1차)

| 시나리오 | 공식 |
|---|---|
| Basic | `Entity + Scene + Motion` |
| Advanced | `Entity(desc) + Scene(desc) + Motion(desc) + Aesthetic control + Stylization` |
| **image-to-video** | **`Motion + Camera movement`** — *"Focus prompt on movement descriptions and specific camera directions rather than static elements."* (core R2의 근거) |
| Sound (2.7/2.6) | `Entity + Scene + Motion + Sound description (voice / SFX / BGM)` |
| **Multi-shot (2.7/2.6)** | `Overall description + Shot number + Timestamp + Shot content` — 명시적 시간 범위(`[0–3s]`)의 번호 매긴 샷 |
| Reference-to-video | `Reference identifier + Action + Scene + Lines + BGM`, `"Image 1"` / `"Video 2"` 식별자 사용 |

## Seedance와 정면 모순 (per-family가 필요한 이유)

Wan은 멀티샷에서 **명시적 Timestamp 범위**를 공식으로 처방한다. 반면 ByteDance는 Timestamp가 Seedance를 불안정하게 만든다고 경고한다(`seedance.md` 참조). **서로 다른 모델의 정반대 컨벤션**이다. 이 둘을 하나의 "범용 비디오 공식"으로 통합하는 것은 정리가 아니라 correctness 회귀다.

## 오디오 억제 — 리터럴 구문 (1차)

`"No dialogue."` / `"No background music."` (긍정 서술이 아니라 벤더가 명시한 억제 구문 — R1의 계열 예외로 그대로 사용).

## 카메라 이동의 감정 의도 (1차, verbatim)

Push-in → intimacy/tension · Pull-out → scale/isolation · Tracking → viewer alongside subject · Orbit → subject importance · Fixed → stillness/focus.

**공식 avoid-list(verbatim 범주)**: 실존 인물 지명 · 한 클립 내 급격한 씬 전환 · 정확한 가독 텍스트 요구 · 매우 긴 안무 시퀀스 · 특정 단어 립싱크.
**길이**: 상한 명시 없음. **Negative prompt**: 컨벤션 문서화 없음. **Deprecation**: *"Wan 2.7 no longer supports the shot_type parameter."* 실제 param은 `models_explore`로 확인한다.
