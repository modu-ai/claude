# moai-pm (PM) — 4명의 AI 직원을 부르는 진입점

> **PM**은 프로젝트를 처음 시작할 때 **어떤 AI 직원이 필요한지 판단해 안내**해 주는 허브 플러그인입니다. 복잡한 설정 대신, "이런 일 할 거야"라고 말하면 알아서 적합한 AI 직원으로 연결해 줍니다.

---

## 4명의 AI 직원

goos.kim의 "플러그인=AI 직원" 발상 — 모두의클로드는 **4명의 AI 직원**으로 구성됩니다. 전부 `modu-ai/claude` 마켓플레이스 하나에서 설치합니다.

| AI 직원 | 플러그인 | 이런 분께 | 무엇을 하나요 |
|---------|---------|-----------|---------------|
| 🧑‍💼 **코워커** | `moai-coworker` | 사업·마케팅·콘텐츠·문서 작성·출판·웹툰 작가 | 실무 동료와 글쓰기 작가 모자를 상황에 따라 교체. 사업계획서, 블로그, 카드뉴스, 계약서, 소설, 웹툰까지 올인원 (192스킬) |
| 🎨 **디자이너** | `moai-designer` | 브랜드·디자인 시스템을 잡고 싶은 분 | 흩어진 브랜드 자산(로고·색·타이포)을 모아 Claude Design용 DESIGN.md로 합성 (11스킬) |
| 💻 **코더** | `moai-coder` | 개발 프로젝트를 시작하는 분 | 개발 환경 셋업, SPEC 기반 개발(DDD/TDD), 품질 게이트까지 (28스킬) |
| 📋 **PM** | `moai-pm` (본 플러그인) | 전부 | 위 3명 중 **누가 필요한지 판단해 연결** (이 플러그인) |

PM은 직접 일하지 않습니다. **누가 이 일에 맞는지 찾아주는 안내자** 역할만 합니다.

---

## 설치

```
/plugin install moai-pm
```

PM만 설치하면 허브가 켜집니다. 실제 일은 각 AI 직원 플러그인이 하므로, 필요한 직원도 함께 설치하세요:

```
/plugin install moai-coworker    # 실무·콘텐츠·작가 (대다수 사용자)
/plugin install moai-designer    # 디자인 (필요 시)
/plugin install moai-coder       # 개발 (필요 시)
```

> 설치하지 않은 직원이 필요해지면, PM이 자동으로 감지하고 **"이 직원을 설치해 주세요"**라고 안내한 뒤 설치 완료 시 이어서 진행합니다(`/project resume`).

---

## 사용법

### 가장 쉬운 방법 — 그냥 말걸기

```
/project
"사업계획서랑 투자자 발표 자료 만들고 싶어"
```

PM이 말에서 필요한 AI 직원을 찾아 안내합니다. 대부분의 경우 **코워커**로 연결됩니다.

### 명시적으로 지정하기 — 플래그

어떤 직원이 필요한지 이미 알면 플래그로 바로 지정할 수 있습니다:

| 명령 | 어떤 직원 | 언제 |
|------|----------|------|
| `/project --cowork` | 🧑‍💼 코워커 | 사업·마케팅·콘텐츠·문서·계약서·출판·웹툰·소설 |
| `/project --designer` | 🎨 디자이너 | 브랜드 디자인 시스템·DESIGN.md·Claude Design 준비 |
| `/project --code` | 💻 코더 | 개발 환경 셋업·SPEC 워크플로우·MoAI-ADK |

### 어떤 직원을 쓸지 모르겠다면

PM이 **"어떤 작업으로 시작할까요?"**라고 4명의 직원을 보여주고 고르게 합니다.

---

## 각 직원이 셋업해 주는 것

### 🧑‍💼 코워커 분기 (`--cowork`)
- 프로젝트 목적·주 산출물·톤을 인터뷰로 파악 (이름·회사는 안 물어봅니다)
- 산출물별 **스킬 체인** 설계 (예: 사업계획서 = 기획 → PPT 제작 → AI 맛 제거 검수)
- 프로젝트 `CLAUDE.md` 작업 지침 생성
- 실무 동료 / 글쓰기 작가 역할 자동 감지

### 🎨 디자이너 분기 (`--designer`)
- 브랜드 자산(로고·색·타이포·기존 사이트·PPT) 수집
- Claude Design 업로드용 **DESIGN.md** 합성
- `.moai/project/brand/` 브랜드 컨텍스트 저장
- Claude Design 온보딩 안내

### 💻 코더 분기 (`--code`)
- 프로젝트 유형·기술 스택 인터뷰
- `.claude/` + `.moai/` + `CLAUDE.md` 개발 환경 스캐폴드 (MoAI-ADK 정본)
- SPEC 기반 개발 워크플로우(`/moai plan → run → sync`) 안내
- 품질 게이트(DDD/TDD, TRUST 5) 설정

---

## 자주 쓰는 명령

| 명령 | 무슨 일 |
|------|--------|
| `/project` | 프로젝트 시작 (말걸기 — PM이 직원 판단) |
| `/project --cowork` · `--designer` · `--code` | 직원 직접 지정 |
| `/project resume` | 직원 설치 후 이어서 진행 |
| `/project catalog` | 설치된 직원·스킬 목록 보기 |
| `/project status` | 현재 설정 상태 |
| `/project apikey` | API 키 관리 |
| `/project doctor` | 환경 진단 (뭔가 안 될 때) |
| `/project feedback` | 버그·제안 GitHub 등록 |

---

## 첫 실행 예시

```
당신: /project
      "카페 창업하려는데 사업계획서랑 메뉴판·SNS 콘텐츠 만들고 싶어"

PM: 코워커가 딱 맞겠네요. 몇 가지만 물어볼게요.
    (인터뷰 진행 → 체인 설계 → 승인 → CLAUDE.md 생성)

PM: 준비됐습니다! 이렇게 시작해 보세요:
    1. "카페 사업계획서 PPT로 만들어줘"
       → business-strategy-planner → office-pptx-designer → AI 맛 제거 검수
    2. "시그니처 메뉴 카드뉴스로 만들어줘"
       → content-card-news → AI 맛 제거 검수
    3. "인스타용 음료 소개 카피 5개 써줘"
       → content-copywriting → AI 맛 제거 검수
```

---

## 더 알아보기

- **허브 라우팅 상세**: `skills/project/references/core/router.md`
- **각 분기 셋업 프로토콜**: `cowork-setup.md` · `designer-setup.md` · `coder-setup.md`
- **전체 프로토콜 인덱스**: `skills/project/references/core/INDEX.md`

---

**라이선스**: LicenseRef-MoAI-NC-ND-1.0 · **작성자**: 모두의AI · **버전**: 0.2.0
