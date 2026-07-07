---
name: project
description: |
  4개 AI 직원 플러그인(코워커·디자이너·코더)의 진입을 분기하는 **허브 라우터 스킬**.
  `/project --cowork`·`--designer`·`--code` 플래그 또는 자연어 의도 감지로 적합한 분기의 셋업 워크플로우를 실행하고 CLAUDE.md를 생성한다. PM 자체는 구현 로직을 품지 않고 각 플러그인의 셋업 스킬로 위임한다.

  다음과 같은 요청 시 반드시 이 스킬을 사용하세요:
  - "새 프로젝트 시작", "프로젝트 설정 도와줘", "CLAUDE.md 만들어줘" → 의도 감지 후 4-plugin 분기
  - "/project --cowork" (실무·콘텐츠·작가), "/project --designer" (브랜드·디자인 시스템), "/project --code" (개발환경)
  - "/project resume", "/project catalog", "/project status", "/project apikey", "/project doctor", "/project feedback"
  - "이어서 진행", "설치 완료", "다시 진행" — 설치 완료 후 재개 요청
  - 사업계획·콘텐츠·디자인·개발 등 자연어 요청이 들어왔을 때 적합한 AI 직원 플러그인으로 라우팅해야 할 때

  이 스킬은 **이름·회사 같은 글로벌 프로필을 재질문하지 않는다.** 프로젝트마다 "이번에 뭘 할 건지, 어떻게 처리하고 싶은지"만 인터뷰한다.
user-invocable: true
version: "0.2.0"
---
<!-- moai-pm v0.2.0 · 4-plugin 허브 라우터 -->

# project — 4개 AI 직원 플러그인 허브 라우터

사용자는 이 프로젝트에서 **무엇을 할지** 말해주면 됩니다. 그러면 PM(본 스킬)이 4개 AI 직원 플러그인 중 적합한 곳으로 진입을 분기하고, 해당 플러그인이 셋업 워크플로우를 수행해 `CLAUDE.md`를 생성합니다.

## 개요

이 스킬은 **허브 라우터**다. 자연어 의도 또는 `--cowork`/`--designer`/`--code` 플래그를 감지해 4-plugin 아키텍처의 적합한 분기로 라우팅한다. PM 자체는 실무·디자인·개발 로직을 품지 않고, 각 플러그인의 셋업 프로토콜(`references/core/*-setup.md`)로 위임한다.

**핵심 기능**:
- 자연어 의도 감지 → 4-plugin 분기 (불명확 시 AskUserQuestion)
- 플래그 명시 분기 (`--cowork`·`--designer`·`--code`)
- 각 분기의 셋업 워크플로우 실행 → CLAUDE.md 생성
- Gap Detection: 누락 플러그인 자동 감지 → 설치 안내 → `/project resume` 재개
- 관리 커맨드 (catalog/status/apikey/doctor/feedback)

---

## 4-plugin 아키텍처

goos.kim "플러그인=AI 직원" 발상 — 4개 AI 직원 플러그인. 전부 `modu-ai/claude` 단일 마켓플레이스.

| 플러그인 | 한글명 | 역할 | 스킬 수 |
|----------|--------|------|---------|
| `moai-coworker` | **코워커** | 실무 + 글쓰기 작가 올인원 (사업·마케팅·콘텐츠·문서·법무·세무·이커머스·미디어·출판·웹툰) | 192 |
| `moai-designer` | **디자이너** | 디자인 전담 (브랜드·디자인 시스템·Claude Design 핸드오프·GAN 품질 루프) | 11 |
| `moai-coder` | **코더** | 개발 전담 (SPEC DDD/TDD·품질 게이트·MoAI-ADK 정본) | 28 |
| `moai-pm` | **PM** | 프로젝트 초기화 허브 (본 스킬 — 라우팅만) | 1 |

**컨셉**: 코워커는 실무+작가 모자 교체, 디자이너·코더는 전문 분리, PM은 진입 허브.

---

## 라우팅 (핵심)

### 플래그 명시 분기

| 커맨드 | 분기 | 대상 플러그인 | 셋업 프로토콜 |
|--------|------|--------------|---------------|
| `/project --cowork` | 코워커 체인 init | moai-coworker | `references/core/cowork-setup.md` |
| `/project --designer` | 브랜드 컨텍스트 셋업 | moai-designer | `references/core/designer-setup.md` |
| `/project --code` | 개발 환경 셋업 | moai-coder | `references/core/coder-setup.md` |

### 자연어 의도 분기 (플래그 없는 `/project`)

bare `/project`는 사용자 발화에서 의도를 감지해 분기한다. 상세 매핑은 `references/core/router.md`.

| 발화 맥락 | 분기 |
|-----------|------|
| 사업계획·마케팅·콘텐츠·문서·법무·세무·이커머스·미디어·출판·웹툰·소설 | `--cowork` |
| 디자인 시스템·브랜드·Claude Design·DESIGN.md·로고·색·타이포 | `--designer` |
| 개발·코딩·SPEC·DDD·TDD·MoAI-ADK·개발환경 | `--code` |
| 불명확 (2개+ 맥락 또는 단서 부족) | AskUserQuestion 4-plugin 선택 |

### 모호성 해소

의도가 2개 이상의 플러그인에 걸치거나 단서가 부족하면 AskUserQuestion(1질문, 4옵션 이내)으로 확인한다. 상세: `router.md` §모호성 해소.

---

## 워크플로우

### `/project` — 허브 라우팅 (기본 동작)

```
Phase 0: 의도 감지 (플래그 또는 자연어)
    ├── 명확 → 해당 분기 setup 프로토콜로 진입
    └── 불명확 → AskUserQuestion 4-plugin 선택
    ↓
Phase 1-8: 해당 분기 셋업 워크플로우 (각 *-setup.md)
    ├── cowork-setup.md:    8-Phase (인터뷰→인벤토리→체인설계→Gap→확인→CLAUDE.md→API키→첫실행)
    ├── designer-setup.md:  5-Phase (자산인터뷰→설치확인→DESIGN.md합성→brand스캐폴드→온보딩안내)
    └── coder-setup.md:     5-Phase (유형인터뷰→설치확인→정본스캐폴드→언어·MCP→SPEC안내)
    ↓
Phase 종료: CLAUDE.md 생성 + 첫 실행 안내
```

### 역할 라벨 (coworker 분기 특화)

coworker 분기는 진입 시 **실무 동료** / **글쓰기 작가** 두 역할을 자동 감지한다(Phase 3 역할 라벨 — 모자 교체). 감지된 역할은 CLAUDE.md 페르소나에 라벨로 기록되어, 실행 시점에 coworker가 모자를 자동 교체한다. 상세: `cowork-setup.md` §역할 자동 감지.

---

## 커맨드 표면

| 커맨드 | 동작 |
|--------|------|
| `/project` (서브커맨드 없이) | 허브 라우팅 — 의도 감지 후 4-plugin 분기. **PRIMARY 기본 동작.** |
| `/project --cowork` | 코워커 분기 명시 |
| `/project --designer` | 디자이너 분기 명시 |
| `/project --code` | 코더 분기 명시 |
| `/project resume [--cowork\|--designer\|--code]` | 설치 완료 후 재개 (해당 분기) |
| `/project catalog` | 4-plugin · 스킬 카탈로그 |
| `/project status` | 현재 설정 상태 |
| `/project apikey` | API 키 관리 |
| `/project doctor` | 환경 진단 |
| `/project feedback` | GitHub 이슈 등록 |

---

## 설치

```
/plugin install moai-pm          # 본 허브 (필수)
/plugin install moai-coworker    # 실무·콘텐츠·작가 분기 (대다수 사용자)
/plugin install moai-designer    # 디자인 분기 (필요 시)
/plugin install moai-coder       # 개발 분기 (필요 시)
```

전부 `modu-ai/claude` 단일 마켓플레이스. Gap Detection이 누락을 감지하면 설치 안내 후 `/project resume`으로 재개한다.

---

## 주의사항

### 1. 글로벌 프로필 질문 금지

이름·회사·역할을 재질문하지 않는다. 프로젝트 맥락만 수집한다. 모든 사용자 정보는 CLAUDE.md 한 곳에만 기록된다 (`moai-profile.md` 생성 금지).

### 2. PM은 구현하지 않는다

본 스킬은 라우팅만 담당한다. 실무 체인·디자인 합성·개발 스캐폴드 로직은 각 플러그인의 셋업 스킬에 위임한다. PM이 특정 산출물을 직접 생성하지 않는다.

### 3. 단일 마켓플레이스 정합

모든 스킬 참조는 `moai-{coworker,designer,coder}:` 접두어를 사용한다. 이전 다중 플러그인 분산 토폴로지(moai-core/hr/operations/...)는 폐기되었으며, router.md의 4-plugin 매핑이 단일 진실 원천이다.

---

## 상세 프로토콜 (`references/core/`)

| 파일 | 역할 |
|------|------|
| `router.md` | 자연어 → 4-plugin 라우팅 매핑·모호성 해소·복합 요청 |
| `cowork-setup.md` | `--cowork` 분기 정본 (8-Phase·코워커 체인·역할 감지) |
| `designer-setup.md` | `--designer` 분기 정본 (브랜드 자산 합성·DESIGN.md) |
| `coder-setup.md` | `--code` 분기 정본 (MoAI-ADK 정본 스캐폴드·SPEC 워크플로우) |
| `init-protocol.md` | 관리 커맨드(resume/catalog/status/apikey/doctor) + 8-Phase 상세 레퍼런스 |
| `context-collector.md` | 맥락 수집 등급(A/B/C)·심화 인터뷰 기준 |
| `claudemd-generator.md` | CLAUDE.md 변수 치환·200라인 예산·HARD 규칙 블록 |
| `execution-protocol.md` | 스킬 체인 순차 실행·단계별 요약 |
| `evaluation-protocol.md` | 5차원 평가 (정확성·완전성·실용성·톤·도메인) |
| `diagnostic-protocol.md` | 환경 진단 (`/project doctor`) |
| `evolution-protocol.md` | 자기학습 진화 프로토콜 |
| `quality-evaluator.md` | 품질 자동 평가 |
| `INDEX.md` | 전체 프로토콜 인덱스 |

전체 인덱스: `references/core/INDEX.md`

---

## 저장 위치

- **프로젝트 작업 지침**: `./CLAUDE.md` (≤ 200라인)
- **프로젝트 스킬-선택 CONFIG**: `./.moai/skill-profile.yaml` (coworker 분기)
- **브랜드 컨텍스트**: `./.moai/project/brand/` (designer 분기)
- **프로젝트 설정**: `./.moai/config.json`
- **API 키**: `./.moai/credentials.env` (프로젝트 격리)
- **템플릿**: `references/templates/CLAUDE.md.tmpl`
