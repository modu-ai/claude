# seedream.md — Seedream 계열 크래프트 (ByteDance)

> 대상 모델(라이브 카탈로그 기준): `seedream_v5_pro`, `seedream_v5_lite`, `seedream_v4_5`
> 파라미터·aspect·media role은 `models_explore(action:'get')`로 라이브 조회.

**Evidence tier:** 1차 (BytePlus ModelArk). 5.0의 "Deep Thinking" 브랜딩은 **2차/unverified**(전용 공식 5.0 프롬프트 가이드 부재).
출처: https://docs.byteplus.com/en/docs/ModelArk/1829186

---

## 공식 5원칙 (1차, BytePlus ModelArk)

1. *"Use coherent natural language to describe the subject + action + environment"* — 끊긴 키워드 나열이 **아님**.
2. 적용 컨텍스트를 밝힌다(logo vs fine art vs poster).
3. 정밀한 스타일 키워드 또는 참조 이미지를 쓴다.
4. 리터럴 렌더 텍스트는 **큰따옴표**에(R3).
5. 편집은 *"use concise, unambiguous instructions"* — 모호한 대명사 회피(R4).

Seedream 3.0 가이드 추가: *"short prompts can also produce amazing results"*; 자작 프롬프트가 AI 생성 프롬프트보다 자주 낫다.

**길이**: 상한 명시 없음(직접 검색으로 부재 확인).

## 편집 예시 (verbatim, 1차)

- 추가: *"Add matching silver earrings and a necklace to the girl in the image"*
- 삭제: *"Remove the girl's hat."*
- 교체: *"Replace the largest bread man with a croissant man, keeping the action and expression unchanged."*
- 멀티 이미지: *"Replace the subject in Image 1 with the subject from Image 2"* · *"Dress the character in Image 1 with the outfit from Image 2"* · *"Apply the style of Image 2 to Image 1."*

## Seedream 5.0 Pro 전용 (1차)

오버레이 마커(좌표점·낙서·스케치)를 통한 인터랙티브 편집 — *"fine-grained operations such as object replacement and element placement."* 벤더: *"Only dola-seedream-5-0-pro supports this capability."* (MCP로 노출되지 않음 — 플랫폼 표면 한계로만 기록.)

## 파라미터 caveat

BytePlus는 Seedream 5.0 Pro를 1K/2K로 열거하지만 Higgsfield는 `resolution[1k|1.5k|2k]`로 노출한다. `1.5k` 티어는 Higgsfield 자체 레이어로 ByteDance가 문서화하지 않았다. Lite/4.5의 `quality[basic|high]`도 ByteDance 대응이 없다. 실제 허용 값은 언제나 `models_explore`로 확인한다.
