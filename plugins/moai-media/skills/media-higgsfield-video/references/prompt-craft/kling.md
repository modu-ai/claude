# kling.md — Kling 계열 크래프트 (Kuaishou)

> 대상 모델(라이브 카탈로그 기준): `kling3_0`, `kling3_0_turbo`, `kling2_6`
> 파라미터·aspect·duration·media role은 `models_explore(action:'get')`로 라이브 조회.

**Evidence tier:** 1차-relayed (kling.ai / klingai.com 도메인 전체가 HTTP 446 WAF/geo-block → 직접 fetch 불가. WebSearch crawl 경유 1차 콘텐츠, 직접 검증은 안 됨. 다른 계열보다 한 단계 낮음.)
출처: https://app.klingai.com

---

## 공식 프레임워크 (relayed)

*"a useful prompt usually defines the subject, action, setting, camera language, lighting, and atmosphere in plain, readable language."* Kling 자신이 이를 **유연한 작문 프레임워크이지 엄격한 공식이 아니라고** 명시한다. 널리 인용되는 `Subject + Movement + Scene + Camera + Lighting + Atmosphere` "공식"은 서드파티 각색이다.

**길이**: `negative_prompt` 2,500자(API 필드 문서 verbatim); `prompt` 대칭 가정.

## 제외 표현 (relayed, R1 예외 주의)

verbatim: *"It is recommended to supplement negative prompt via negative sentences within positive prompts."* — Kling은 자체 API에 부정 필드가 있어도 제외를 긍정 프롬프트 안 부정문으로 접어 넣기를 권한다. Higgsfield는 그 필드를 노출하지 않으므로 이는 우회가 아니라 벤더 선호 관행이다. 스킬은 부정 파라미터를 내보내지 않고 제외를 긍정 문장으로 표현한다.

## 멀티샷

Kling 3.0은 *"highly flexible storyboard control"* / 단일 생성 네이티브 멀티샷을 지원한다. 그러나 Kling 네이티브 멀티샷은 샷별 프롬프트 필드를 갖는 별도 UI/API 모드인 반면 Higgsfield는 단일 flat `prompt`만 노출한다. 따라서 스토리보드는 shot 라벨로 **하나의 prompt 문자열 안에 인라인** 구성한다.

## 대사 (relayed)

5개 언어(zh/en/ja/ko/es) + 방언 + 한 영상 내 혼합. 다중 캐릭터 구조: `<who is speaking> (<how things are said>) <what they say>`.

**Do**: 구체적 시각 명사·모션 큐(`smoke drifting upward`); 자연어 카메라 용어(close-up, low angle, slow push-in, tracking); 제외는 긍정 프롬프트 안 부정문으로.
**Don't**: 시각 상관물 없는 추상/내면 상태 언어(*"magic"*, *"feels tense"*).

**Gap**: `start_image` 제공 시 프롬프트에서 무엇을 뺄지에 대한 공식 진술 없음. 실제 role·duration은 `models_explore`로 확인한다.
