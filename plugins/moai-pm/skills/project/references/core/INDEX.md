# project Core Protocol — 인덱스

## 개요

**4-plugin 허브 라우터 스킬(`/project`)**의 핵심 프로토콜 파일 인덱스. PM은 라우팅만 담당하고, 각 AI 직원 플러그인(코워커·디자이너·코더)의 셋업 스킬로 위임한다.

**현재 상태 요약:**
- 진입점은 bare `/project`(허브 라우팅 — 의도 감지 후 4-plugin 분기). `--cowork`/`--designer`/`--code` 플래그로 명시 분기.
- 자연어 의도 감지 불가 시 AskUserQuestion 4-plugin 선택 (`router.md`).
- 각 분기의 셋업 워크플로우(`*-setup.md`)가 CLAUDE.md 생성까지 수행.
- Gap Detection(누락 플러그인 감지 → 설치 안내 → `/project resume` 재개)은 각 setup 프로토콜에 통합.
- 글로벌 프로필 시스템 없음 — 이름·회사·역할을 프로젝트마다 묻지 않음.

---

## 파일 목록 (12개)

### 허브 라우팅

#### 1. router.md — 자연어 → 4-plugin 라우팅
4개 AI 직원 플러그인 키워드 매핑, 모호성 해소, 복합 요청 분기.

### 분기 정본 (3개)

#### 2. cowork-setup.md — `/project --cowork` 분기 (코워커 체인 init)
8-Phase 워크플로우(인터뷰→인벤토리→체인설계→Gap→확인→CLAUDE.md→API키→첫실행). 실무/글쓰기 작가 역할 자동 감지. moai-coworker 스킬 체인 프리셋.

#### 3. designer-setup.md — `/project --designer` 분기 (디자이너 브랜드 셋업)
5-Phase 워크플로우(자산인터뷰→설치확인→DESIGN.md합성→brand스캐폴드→온보딩안내). cd-system-prep + moai-domain-brand-design 위임. `.moai/project/brand/` 산출.

#### 4. coder-setup.md — `/project --code` 분기 (코더 개발환경 셋업)
5-Phase 워크플로우(유형인터뷰→설치확인→정본스캐폴드→언어·MCP→SPEC안내). moai-workflow-project 정본 templates로 `.claude/`·`.moai/`·CLAUDE.md 생성.

### 상세 레퍼런스 (coworker 분기 중심, 공유)

#### 5. init-protocol.md — 관리 커맨드 + 8-Phase 상세 레퍼런스
`/project resume`·catalog·status·apikey·doctor 흐름 + coworker 분기 8-Phase 각 단계 AskUserQuestion 스키마·inventory.json/init-progress.json 스키마·Re-entry 상세.

#### 6. context-collector.md — 맥락 수집 프로토콜
맥락 충분성 등급(A/B/C), 모호성 감지, AskUserQuestion 전략.

#### 7. claudemd-generator.md — CLAUDE.md 생성 프로토콜
`references/templates/CLAUDE.md.tmpl` 변수 치환 규칙, 200라인 예산, HARD 규칙 고정 블록.

#### 8. execution-protocol.md — 스킬 체인 실행 프로토콜
플러그인 트리거 → 체인 순차 실행 → 단계별 요약 → general-ai-slop-reviewer 종료.

#### 9. evaluation-protocol.md — 평가 프로토콜
5개 차원 평가: 정확성, 완전성, 실용성, 톤 적합성, 도메인 적합성.

#### 10. evolution-protocol.md — 자기학습 진화 프로토콜
Self-Refine 사이클: 반성 → 피드백 → 패턴 → 업데이트 → 학습.

#### 11. diagnostic-protocol.md — 진단 프로토콜
`/project doctor`, `/project status` 커맨드. 환경 상태 진단.

#### 12. quality-evaluator.md — 품질 자동 평가
산출물 품질 자동 검증, AI 슬롭 체크리스트 포함.

### (삭제됨) profile-manager.md
**전면 제거됨**. 이름·회사·역할을 프로젝트마다 묻지 않는 정책으로 전환.

---

## templates/

- `CLAUDE.md.tmpl` — coworker 분기 Phase 6에서 로드되는 CLAUDE.md 생성 템플릿.

---

## 파일 간 의존성

```
SKILL.md (허브) → router.md (자연어 분기)
       ↓
   ┌───┼───┐
   ↓   ↓   ↓
cowork-  designer-  coder-
setup.md setup.md   setup.md
   ↓       │         │
   ↓       ↓         ↓
init-protocol.md (8-Phase 상세 + 관리 커맨드)
context-collector.md ← claudemd-generator.md (CLAUDE.md.tmpl 로드)
       ↓
execution-protocol.md → evaluation-protocol.md
       ↓
evolution-protocol.md ← diagnostic-protocol.md ← quality-evaluator.md
```

---

## 스킬 체이닝 핵심 원칙 (coworker 분기)

1. 텍스트 산출물 체인은 **반드시 `moai-coworker:general-ai-slop-reviewer`로 종료**한다.
2. 한국어 최종본은 직후 `moai-coworker:general-humanize-korean` 2차 패스.
3. 체인은 [기획/분석 → 생성 → 포맷 변환 → 검수] 구조를 기본으로 한다.
4. 비텍스트 산출물(차트·데이터·숫자·음성·미디어)은 ai-slop 단계를 생략한다.
5. DOCX/PPTX/XLSX/HWPX/HTML 포맷은 Claude 기본 artifacts가 아닌 **moai-coworker 스킬 우선**.
6. **Gap Detection**: 각 분기에서 체인 스킬을 인벤토리와 대조해 누락 플러그인을 자동 감지하고, 설치 안내 후 Re-entry로 재개한다.

---

## 4-plugin 아키텍처 (단일 modu-ai/claude 마켓플레이스)

이전 27-플러그인 분산 토폴로지(moai-core/hr/operations/lifestyle/product/support/career/data/public-data/research/commerce/bi/sales/wealth/productivity/comms + 다중 도메인)는 **폐기**되었다. 모든 도메인 스킬은 아래 4개 AI 직원 플러그인으로 수렴했다.

| 플러그인 | 한글명 | 역할 | 스킬 수 | 라우팅 분기 |
|---------|--------|------|---------|------------|
| moai-coworker | 코워커 | 실무 + 글쓰기 작가 올인원 (사업·마케팅·콘텐츠·문서·법무·세무·이커머스·미디어·출판·웹툰 + 구 다중 도메인 전부 흡수) | 192 | `--cowork` |
| moai-designer | 디자이너 | 디자인 전담 (브랜드·디자인 시스템·Claude Design 핸드오프·GAN 품질 루프) | 11 | `--designer` |
| moai-coder | 코더 | 개발 전담 (SPEC DDD/TDD·품질 게이트·MoAI-ADK 정본) | 28 | `--code` |
| moai-pm | PM | 프로젝트 초기화 허브 (본 스킬 — 라우팅만) | 1 | (본 스킬) |

**합계: 4 플러그인 / 232 스킬** (단일 modu-ai/claude 마켓플레이스)

---

## 2계층 아키텍처

```
계층 1: 플러그인 (Read-Only) — 4개 AI 직원 플러그인 (moai-pm 허브 + coworker/designer/coder)
         ↑ 각 분기 Gap Detection: Bash ~/.claude/plugins/ + system reminder 교차 검증
         ↑ 누락 플러그인 감지 → 설치 안내 → /project resume 재개
계층 2: ./CLAUDE.md (자동 로딩) — 프로젝트별 맞춤형 페르소나 + 스킬 체인 정의
         + ./.moai/ — 설정, 컨텍스트, API 키, 브랜드 컨텍스트(designer 분기)
         + .moai/cache/inventory.json — 활성 스킬 인벤토리
         + .moai/cache/init-progress.json — Re-entry 재개 상태
         + auto-memory — Claude 자율 저장 (세션 간 학습 누적)

❌ 제거됨: 글로벌 프로필 계층 (moai-profile.md)
❌ 폐기됨: 27-플러그인 분산 토폴로지 → 4-plugin 수렴
```
