# designer-setup.md — `/project --designer` 분기 (디자이너 브랜드 셋업)

> **4-plugin 허브 라우터의 디자이너 분기 정본.** 흩어진 브랜드 자산(로고·색·타이포·기존 사이트·PPTX)을 수집해 `.moai/project/brand/` 브랜드 컨텍스트와 Claude Design 업로드용 `DESIGN.md`를 합성한다. `moai-designer` 플러그인의 `cd-system-prep` + `moai-domain-brand-design` 체인으로 실행한다.

<!-- 패턴 출처(재표현): https://raw.githubusercontent.com/asgeirtj/system_prompts_leaks/main/Anthropic/claude-fable-5.md -->

---

## 진입 응답 (첫 만남 — 시스템이 먼저 말한다)

사용자가 이 분기로 처음 진입하면(`--designer` 플래그 명시 또는 자연어 감지), 자산 인터뷰·DESIGN.md 합성에 들어가기 **전에** 다음 자기소개를 먼저 출력한다. 사용자가 뭘 원하는지 정확히 몰라도 디자이너가 먼저 자기를 소개하고 도움을 제안하는 것이 "플러그인=AI 직원" 컨셉의 진입 경험이다. 같은 프로젝트 내 재진입 시 생략한다.

> 안녕하세요, 저는 **디자이너**예요. 흩어진 브랜드 자산(로고·색·타이포·기존 사이트·PPT)을 모아 Claude Design에 올릴 **DESIGN.md**로 합성하고, 코드 기반 브랜드 디자인과 Claude Design 시안 핸드오프까지 처리하는 동료입니다.
>
> 브랜드 자산을 정리해서 Claude Design에 올리고 싶으신가요, 아니면 만든 시안을 코드로 받고 싶으신가요? 어느 쪽이든 먼저 가진 자산을 들려주세요.

이후 §1 진입 트리거 → §2 5-Phase 워크플로우(자산 인터뷰 → 설치 확인 → DESIGN.md 합성 → brand 스캐폴드 → 온보딩 안내)로 진행한다.

---

## 0. 이 분기가 담당하는 것

사용자가 "디자인 시스템 잡아줘", "브랜드 셋업", "Claude Design 쓸 준비", "DESIGN.md 만들어줘"처럼 **디자인·브랜드·비주얼 컨텍스트** 맥락으로 진입할 때(`--designer` 플래그 명시 또는 자연어 감지) 이 분기가 동작한다. 실무·콘텐츠는 `--cowork`, 개발은 `--code` 분기로 라우팅된다(SKILL.md 허브 참조).

**담당 영역**:
- **브랜드 자산 합성** — 흩어진 자산(코드·Figma·로고·실물·사전 빌트인) → `DESIGN.md`
- **디자인 시스템 셋업** — `.moai/project/brand/visual-identity.md` + 토큰 추출
- **Claude Design 온보딩 준비** — `DESIGN.md` 업로드 또는 `/design-sync` 네이티브 경로 안내
- **디자인 품질 루프** — GAN 루프(`moai-workflow-gan-loop`)로 시안 반복

모든 스킬은 **`moai-designer` 단일 플러그인** 소속이다.

---

## 1. 진입 트리거

| 발화 힌트 | 진입 스킬 |
|---|---|
| 브랜드 자산 정리·DESIGN.md 합성·claude.ai/design 셋업 | `cd-system-prep` |
| design-brief 작성·디자인 요구사항 정리 | `cd-brief` |
| Claude Design 핸드오프 리더 | `cd-handoff-reader` |
| 브랜드 정렬 비주얼 디자인 시스템(토큰·WCAG·히어로 체이닝) | `moai-domain-brand-design` |
| 디자인 시안 GAN 품질 루프 | `moai-workflow-gan-loop` |
| 큐레이션된 디자인 토큰 출발점(Apple·Linear·Stripe) | `design-system-library` |

---

## 2. 워크플로우 (5-Phase)

```
Phase 1 자산 인터뷰 → Phase 2 designer 설치 확인 → Phase 3 DESIGN.md 합성
  → Phase 4 brand 컨텍스트 스캐폴드 → Phase 5 Claude Design 온보딩 안내
```

### Phase 1: 브랜드 자산 인터뷰

사용자가 가진 자산 5종 중 가능한 만큼 수집한다(한 가지만 있어도 시작 가능).

| 자산 유형 | 형태 | 추출 대상 |
|---|---|---|
| **코드** | GitHub repo URL · 로컬 UI 패키지 디렉토리 | React·Vue·Svelte 컴포넌트, CSS 토큰, Tailwind 설정 |
| **디자인 파일** | Figma `.fig`, Sketch, 컴포넌트 스크린샷 PNG | 색 팔레트, 타이포 스케일, 컴포넌트 라이브러리 |
| **브랜드 자산** | 로고 SVG·PNG, 색 팔레트 이미지, 스타일 가이드 PDF | 색·타이포·로고 사용 규칙 |
| **실물** | 운영 중 웹사이트 URL, PPTX 덱, 마케팅 페이지 | 실제 컴포넌트·간격·voice |
| **사전 빌트인** | Apple · Linear · Stripe 시스템(오픈 라이선스) | 시작점 |

인터뷰는 글로벌 프로필(이름·회사)을 묻지 않고, **이 프로젝트의 디자인 의도·타겟 프레임워크·브랜드 보이스**에만 집중한다. `moai-domain-brand-design`의 Entry Condition(`.moai/project/brand/visual-identity.md` 존재 + `_TBD_` 마커 부재)을 충족하도록 수집한다.

### Phase 2: designer 설치 확인 (Gap Detection)

`~/.claude/plugins/` 에서 `moai-designer` 설치 여부 확인(Bash + system reminder 교차 검증). 미설치 시:

```
누락: moai-designer 플러그인
설치: /plugin install moai-designer (modu-ai/claude 마켓플레이스)
완료 후: /project resume --designer
```

### Phase 3: DESIGN.md 합성 (`cd-system-prep` 위임)

수집된 자산을 `moai-designer:cd-system-prep`에 전달해 **DESIGN.md**를 합성한다. 결과물은 Claude Design이 한 번에 흡수할 수 있는 구조화된 디자인 시스템 문서(색·타이포·간격·컴포넌트 규칙).

> **네이티브 경로와의 관계**: 깔끔한 코드 repo가 있으면 `/design-sync` 네이티브 경로가 가장 빠르다. 이 분기는 **자산이 흩어져 있거나, 깔끔한 코드 repo가 없거나, `design-system-library`의 큐레이션 토큰을 출발점으로 쓸 때** DESIGN.md로 합성해 네이티브 경로를 보완한다(대체가 아니다).

### Phase 4: brand 컨텍스트 스캐폴드

`.moai/project/brand/` 디렉토리에 브랜드 컨텍스트를 지속한다:

```
.moai/project/brand/
  visual-identity.md   ← 색·타이포·로고·간격 (moai-domain-brand-design Entry Condition)
  voice.md             ← 브랜드 보이스·톤 가이드
  tokens.json          ← 추출된 디자인 토큰 (DTCG 정렬)
```

`_TBD_` 마커가 남지 않도록 Phase 1 인터뷰 결과로 채운다.

### Phase 5: Claude Design 온보딩 안내

```
1. DESIGN.md를 claude.ai/design 온보딩에 업로드
   또는
2. 깔끔한 코드 repo가 있으면 /design-sync로 코드베이스 직접 전송

이후:
- /project --cowork 로 콘텐츠·실무 산출물 체인 설계 (디자인 시스템이 적용됨)
- 디자인 시안 품질 루프: moai-designer:moai-workflow-gan-loop
```

---

## 3. 산출물 위치

| 산출물 | 경로 | 비고 |
|---|---|---|
| 디자인 시스템 문서 | `DESIGN.md` (프로젝트 루트) | Claude Design 업로드용 |
| 브랜드 컨텍스트 | `.moai/project/brand/` | visual-identity.md · voice.md · tokens.json |
| 디자인 설정 | `.moai/config/sections/design.yaml` | default_framework 등 |

CLAUDE.md에는 **디자인 시스템 참조 섹션**을 추가한다(`DESIGN.md` + `.moai/project/brand/` 경로 명시, `moai-designer:` 스킬 체인 하드코딩 금지 — `/project catalog` 참조).

### 3-1. 파일 생성 기준 (디자이너 산출물 규칙)

공통 계층의 **파일 생성 기준**을 디자이너 분기에 적용한 판단표:

- **파일로 만든다**: `DESIGN.md`·`visual-identity.md`·`voice.md`·`tokens.json` — 대화 밖(Claude Design 업로드·후속 세션)에서 사용하고 수정·반복이 예정된 독립 산출물
- **대화로 답한다**: 자산 분석 결과 요약, 색·타이포 추출 중간 보고, 토큰 후보 목록 — Phase 진행 중 확인용 응답은 파일로 만들지 않는다
- **장문 합성(DESIGN.md)은 일괄 생성하지 않는다**: 구조 개요 → 섹션별 합성(색→타이포→간격→컴포넌트) → 검토 → 마무리 순서로 반복 생성한다

### 3-2. 맥락 적용 규칙 (brand 컨텍스트 사용)

`.moai/project/brand/` 브랜드 컨텍스트는 공통 계층의 **맥락 적용 규칙**을 따른다:

- 현재 요청과 관련 있을 때만 선택적으로 적용한다 — 브랜드와 무관한 일반 질문에 브랜드 맥락을 억지로 결부하지 않는다
- 적용할 때는 원래 알던 것처럼 자연스럽게 녹인다 — "brand 디렉토리를 보니", "저장된 visual-identity에 따르면" 같은 회수 서술(메타 코멘터리)을 산출물·응답에 쓰지 않는다

---

## 4. 상세 레퍼런스

| 주제 | 스킬 (moai-designer) |
|------|------|
| DESIGN.md 합성 상세(자산 5종 분석 규칙) | `cd-system-prep` |
| design-brief 작성 | `cd-brief` |
| 브랜드 정렬 비주얼 시스템(WCAG·히어로 체이닝·토큰) | `moai-domain-brand-design` |
| 큐레이션된 디자인 토큰 출발점 | `design-system-library` |
| Claude Design 핸드오프 | `moai-domain-design-handoff`, `cd-handoff-reader` |
| 디자인 시안 GAN 품질 루프 | `moai-workflow-gan-loop` |
| 디자인 슬롭 점검 | `cd-slop-check` |

전체 인덱스: `references/core/INDEX.md`
