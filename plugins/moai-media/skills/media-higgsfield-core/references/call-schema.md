# call-schema.md — 호출 스키마 계약 (SSOT)

> `media-higgsfield-core` | `generate_image` / `generate_video`의 **형태(shape)** 계약.
> 개별 모델의 파라미터 **값**(enum·aspect·duration·media role)은 여기 하드코딩하지 않는다 — 런타임에 `models_explore(action:'get')`으로 조회한다(→ `catalog-protocol.md`).

**Evidence tier:** 1차 (라이브 `models_explore` / tool schema 관측. `mcp-catalog-snapshot.md` §0 근거)

---

## 1. 중첩 `params` 객체

생성 도구는 **평평한(flat) 최상위 인자가 아니라 중첩된 `params` 객체**를 받는다. 이 형태는 계약이고, 안의 개별 값은 모델별로 라이브 조회한다.

```
generate_image({
  params: {
    model:        "<catalog id>"        // models_explore로 확인한 실제 id
    prompt:       "<text>"
    aspect_ratio: "<model의 aspect_ratios 중 하나>"
    count:        <1-4>                  // 병렬 JOB 수
    medias:       [{ role: "<model이 선언한 role>", value: "<media_id | job_id>" }]
    get_cost:     <bool>                 // true = 크레딧만 반환, JOB 제출 안 함
  }
})
```

```
generate_video({
  params: {
    model:        "<catalog id>"
    prompt:       "<text>"               // Marketing Studio 워크플로는 선택
    aspect_ratio: "<model의 aspect_ratios 중 하나>"
    duration:     <int>                  // model의 durations / duration_range 준수
    count:        <1-4>
    medias:       [{ role: "<role>", value: "<media_id | job_id>" }]
    get_cost:     <bool>
  }
})
```

모델별 추가 인자(예: soul 계열의 `soul_id`, 일부 모델의 `resolution`)는 `params` 최상위에 얹되, 그 **허용 값은 반드시 `models_explore`로 확인**한다. 값을 이 파일에 표로 박아두지 않는다.

---

## 2. HARD 제약 (tool schema 관측)

| 제약 | 내용 |
|---|---|
| `medias[].value` | 반드시 `media_id`(`media_upload` / `media_import_url` 산출) 또는 이전 생성의 `job_id`. 날것의 `https://` URL은 **거부(REJECTED)**된다. |
| `medias[].role` | 모델별. `models_explore`가 반환하는 해당 모델의 role 목록을 조회한다. 흔한 값: `image`, `image_references`, `start_image`, `end_image`, `video_references`, `audio_references`, `input_video`, `input_audio`. |
| `aspect_ratio` | 모델이 선언한 목록 안에 있어야 한다. 일부 모델은 빈 목록을 선언(aspect 미적용). |
| `duration` | 모델이 `durations`(enum) 또는 `duration_range`(범위) 중 하나를 선언한다. 허용 밖 값은 가장 가까운 값으로 스냅/클램프된다. |
| `get_cost: true` | 프리플라이트 — JOB 제출 없이 크레딧 비용만 반환. 크레딧 소모 0. 파라미터 검증 오류도 함께 드러난다. |
| `count` vs `batch_size` | `count`(1-4) = 병렬 **JOB** 수. `batch_size`는 `ms_image`에만 있고(1-20) JOB당 이미지 수를 뜻한다. 둘은 다르다. (`batch_size`는 `ms_image` 전용이므로 그 밖의 어떤 호출에도 등장하지 않는다.) |

---

## 3. 런타임 namespace 해석 (하드코딩 금지)

Higgsfield MCP 도구의 **namespace(네임스페이스) 접두사는 등록 방식에 따라 달라진다.** 스킬은 이를 **런타임에 해석**하고, 어느 한쪽을 유일한 형태로 하드코딩하지 않는다.

| 등록 경로 | 도구 namespace 접두사 |
|---|---|
| 플러그인 `.mcp.json` (서버명 `higgsfield`) | `mcp__higgsfield__` |
| Claude Desktop / connector 등록 | `mcp__claude_ai_higgsfield__` |

런타임 해석 규칙: 도구 호출 직전 `ToolSearch`로 사용 가능한 Higgsfield 도구를 찾아 실제 노출된 namespace를 확인하고, 그 접두사로 `generate_image` / `models_explore` / `get_cost` 계열을 호출한다. 세션이 두 등록 중 어느 쪽으로 붙었는지에 따라 `mcp__higgsfield__generate_image` 또는 `mcp__claude_ai_higgsfield__generate_image`가 유효하다 — **어느 하나를 문서에 유일 정답으로 박지 않는다.**

---

## 4. `get_cost` 프리플라이트 · `adjustments` 리드백

- 모든 실제 생성 **직전**에 `get_cost: true`로 프리플라이트하여 `credits`(실제 청구값)를 확인한다. 자세한 비용 규칙은 `job-lifecycle.md`.
- 응답에 `adjustments` 필드가 있으면 서버가 채운 기본값을 뜻한다. 스킬은 이 필드를 **리드백(read-back)하여 사용자에게 보고**한다 — 오디오를 요청했는데 서버가 `generate_audio: false`로 치환했다면, 그 치환 사실을 사용자에게 알려야 한다. `adjustments`를 무시하면 사용자는 자기가 요청한 것과 다른 결과를 조용히 받게 된다.

---

## 5. 안티패턴 — 존재하지 않는 파라미터 (parameters that **do not exist**)

아래 이름들은 **이전(pre-SPEC) 스킬 본문에 있었지만 라이브 스키마에 do not exist** — 즉 존재하지 않는다. 전달하면 잘해야 무시되고 최악은 오류다. 이 목록은 오직 **산문(prose)으로만** 존재하며, 이 파일을 포함해 어떤 호출 예시(코드 블록)에도 넣지 않는다. (이 절이 곧 계약의 반례 목록이자, 발명된 옛 모델 id 표를 부활시키지 못하게 하는 트립와이어다.)

- `width_and_height` — 존재하지 않음. aspect는 `aspect_ratio`로, 실제 해상도는 모델별 `resolution`/`quality`(라이브 조회)로.
- `duration_seconds` — 존재하지 않음. 영상 길이는 `duration`(정수 초).
- `image_url` — 존재하지 않음. 참조 이미지는 `media_id`/`job_id`로만. §2 참조.
- `enhance_prompt` — 존재하지 않음.
- `style_strength` — 존재하지 않음.
- `custom_reference_id` — 존재하지 않음. 캐릭터 일관성은 모델별 media role 또는 `soul_id`로.
- `image_reference_url` — 존재하지 않음. §2의 `medias[].value` 규칙과 정면 충돌한다(URL 거부).

또한 다음도 **최상위 flat 인자로는 존재하지 않는다**: 평평한 `quality`(모델별 `params` 내부 값), `seed`(일부 3D 모델 예외), `preset`(필드명은 `preset_id`이며 `higgsfield_preset` 전용). 이전 스킬 본문이 열거하던 옛 모델 id들은 실제 카탈로그에 아예 없다 — 모델 id는 언제나 `models_explore`로 확인한다.

> 규칙: 이 절은 반례를 **이름으로 지목**하기 위해 그 이름들을 산문에 담는 유일한 장소다. 다른 어떤 파일에서도, 그리고 이 파일의 코드 블록 안에서도, 위 이름들은 등장하지 않는다.
