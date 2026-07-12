# catalog-protocol.md — 라이브 카탈로그 조회 프로토콜

> `media-higgsfield-core` | 파라미터·모델·프리셋을 **런타임에 조회**하는 도구와 순서.
> 이 파일은 "무엇을 물어보는가"를 정의한다. "무엇을 하드코딩하는가"의 답은 언제나 **아무것도**다.

**Evidence tier:** 1차 (라이브 MCP 표면 관측 + Higgsfield 공식 agent 문서. `mcp-catalog-snapshot.md` §5 근거)

Higgsfield 자신의 agent 문서가 이 설계를 직접 확인한다. `references/`는 에이전트에게 이렇게 지시한다: **"When unsure, run `higgsfield model get <model>` and inspect the schema."** — 벤더 스스로 정적 파라미터 계약 발행을 거부한다.
출처: https://github.com/higgsfield-ai/skills

---

## 1. 카탈로그 SSOT 도구

| 도구 | 런타임 역할 |
|---|---|
| `models_explore(action:'list'\|'search'\|'get'\|'recommend')` | 카탈로그 진실원. `get`은 한 모델의 정확한 제약(aspect·duration·media role·모델별 param)을 반환. `recommend`는 목표 + 입력 컨텍스트로 후보를 제안. `list`는 유형별 전체 목록. `search`는 키워드 검색. |
| `show_marketing_studio(type:'image_style'\|'brand_kit'\|'product'\|'hook'\|'setting'\|'ad_reference')` | `ms_image` / `marketing_studio_video`의 **필수** 사전 목록 호출. style·hook·setting UUID를 반환. |
| `presets_show` | `higgsfield_preset`용 프리셋 카탈로그. |
| `get_workflow_instructions()` | 브리핑형 워크플로 카탈로그. 인자 없이 목록, `{workflow}`로 상세. |
| `get_cost`(생성 도구의 `params.get_cost:true`) | 비용 프리플라이트. `job-lifecycle.md` 참조. |
| `balance` | 크레딧 잔액. |
| `media_upload` / `media_import_url` | 로컬 파일·웹 URL → `media_id`. `medias[].value`에 사용. |
| `job_status` / `job_display` | 비동기 JOB 폴링. |

---

## 2. 표준 런타임 순서 (REQ-010)

모든 생성은 아래 순서를 따른다. 이 순서가 곧 "테이블을 신뢰하지 않고 카탈로그에 물어본다"의 구현이다.

1. **후보 좁히기** — 사용자 의도에서 계열 후보를 추린다(→ 각 `prompt-craft` 크래프트 노트). 이 단계는 후보를 *좁힐 뿐*, 파라미터를 단정하지 않는다.
2. **라이브 조회** — `models_explore(action:'get', ...)`로 선택 후보의 실제 제약(aspect_ratios·durations·medias roles·모델별 param 값)을 가져온다. `marketing_studio` 계열이면 `show_marketing_studio`로 style/hook/setting을 가져온다.
3. **비용 프리플라이트** — `get_cost: true`로 `credits`를 확인한다(크레딧 0 소모). `adjustments`가 있으면 리드백해 둔다.
4. **생성** — 조회된 값으로만 실제 `generate_image` / `generate_video`를 호출한다.
5. **폴링·리드백** — `job_status`로 `completed`까지 폴링하고, 반환된 `adjustments`를 사용자에게 보고한다(→ `job-lifecycle.md`).

---

## 3. 범위 밖 모델 폴백 (live lookup)

15개 크래프트 계열에 없는 모델(예: `z_image`, `kling_omni_image`, `grok_image`)을 사용자가 요청하면:

- 계열 크래프트 파일이 없다는 사실을 **명시적으로 말한다.**
- `models_explore(action:'get')`로 제약을 **live lookup(라이브 조회)**한다.
- 공통 규칙 R1–R5(→ `universal-rules.md`)를 적용한다.

계열 특화 크래프트가 없다고 해서 모델을 못 쓰는 게 아니다 — 카탈로그를 라이브로 조회하면 제약을 알 수 있다. 다만 그 사실을 숨기지 않고 사용자에게 알린다.

---

## 4. 왜 스냅샷을 계약으로 쓰지 않는가

`mcp-catalog-snapshot.md`는 plan 단계의 **증거 기준선(point-in-time)**이지 런타임 계약이 아니다. 런타임에 라이브 카탈로그가 스냅샷과 달라졌다면(드리프트) 그것은 **설계가 증명되는 순간**이다 — 스킬은 라이브 값을 쓰고, 드리프트를 `progress.md`에 기록하되, 스냅샷을 스킬 본문에 "고쳐 넣지" 않는다.
