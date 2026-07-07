# moai-design — 에이전틱 디자인 플러그인

Claude Code 터미널·데스크탑에서 **Claude Design 연동**부터 **코드 기반 브랜드 디자인**까지 하나의 `/design` 표면으로 처리하는 플러그인입니다. 디자인 토큰(DTCG)·DESIGN.md·75종 브랜드 시스템·GAN 품질 루프를 포함합니다.

## 설치

```bash
claude plugin marketplace add modu-ai/claude
/plugin install design
```

플러그인 명령은 `플러그인명:명령` 콜론 네임스페이스로 노출됩니다. 이 플러그인의 `name`은 `design`이므로 명령은 **`/design:<name>`** 형태입니다(예: `/design:brief`).

## 두 갈래 경로 (Path A / Path B)

`/design`(bare)은 AskUserQuestion 1라운드로 경로를 선택한 뒤 해당 파이프라인으로 진입합니다.

- **Path A — Claude Design import**: claude.ai/design에서 만든 시안을 **핸드오프 번들**(.zip 또는 붙여넣기 프롬프트 + 번들 URL)로 받아 `moai-workflow-design`이 import하고 `cd-handoff-reader`가 분석합니다. README를 source of truth로 먼저 파싱하고 토큰/컴포넌트는 있으면 사용·없으면 코드(HTML/CSS)에서 유도하는 방어적 방식입니다.
- **Path B — 코드 기반 브랜드 디자인**: 브랜드 컨텍스트에서 출발해 `moai-domain-copywriting`(카피)과 `moai-domain-brand-design`(비주얼 토큰)을 **병렬**로 생성한 뒤, `moai-workflow-gan-loop`으로 품질을 반복 개선합니다.

## 파이프라인

```
manager-spec (BRIEF)
      │
      ▼
[ moai-domain-copywriting  ‖  moai-domain-brand-design ]   ← 병렬
      │
      ▼
frontend role (구현)        ← 디자인 헌법의 expert-frontend ROLE.
      │                        런타임에 Agent(general-purpose) + frontend whitelist로 해소
      ▼
sync-auditor (+ GAN 루프)   ← 4차원 회의적 채점 · pass_threshold 게이팅
```

- **BRIEF 최초**: `manager-spec`이 브랜드 인터뷰 → BRIEF를 작성합니다(디자인 헌법 "Always" 페이즈).
- **병렬 생성**: 카피와 비주얼 토큰은 별도 스킬로 병렬 실행됩니다(병렬성 계약 보존).
- **GAN 최종**: `sync-auditor`가 Design Quality(30%)·Originality(25%)·Completeness(25%)·Functionality(20%) 4차원을 채점하고, `moai-workflow-gan-loop`이 `design.yaml`의 `max_iterations`/`pass_threshold`/`escalation_after`로 반복을 제어합니다.

## 명령 (6개)

| 명령 | 동작 | 위임 스킬 |
|------|------|-----------|
| `/design:` (bare) | Path A/B 경로 선택 인터뷰 → 파이프라인 진입 | `moai-workflow-design` (+ `cd-prompt-builder`) |
| `/design:brief` | 6요소 브리프(Project·Audience·Pages·Tone·Reference·Constraints) → 붙여넣기 프롬프트 | `cd-brief` |
| `/design:tokens` | 브랜드 자산 → DESIGN.md + DTCG 토큰(색·타이포·spacing·radii·shadows) | `cd-system-prep` + `moai-domain-brand-design` |
| `/design:import` | Claude Design 핸드오프 번들(.zip 또는 URL) import·분석 | `moai-workflow-design` + `cd-handoff-reader` |
| `/design:check` | 디자인 카피 AI 슬롭 감사 → 검수 보고서 + 대안 | `cd-slop-check` + `moai-domain-copywriting` |
| `/design:system` | 75종 브랜드 디자인 시스템 라이브러리 + Tailwind CDN 매핑 | `design-system-library` |

## 구성 요소

- **스킬 11종**: 디자인 도메인/워크플로우 5종(`moai-domain-brand-design`, `moai-domain-copywriting`, `moai-workflow-design`, `moai-workflow-gan-loop`, `moai-domain-design-handoff`) + Claude Design 전처리·라이브러리 6종(`cd-brief`, `cd-system-prep`, `cd-prompt-builder`, `cd-handoff-reader`, `cd-slop-check`, `design-system-library`).
- **에이전트 3종**: `manager-spec`(BRIEF 작성), `sync-auditor`(GAN 4차원 평가), `builder-harness`(Path B1 figma-extractor 동적 생성). read-only 참조 조사는 Anthropic 내장 `Explore` 사용.
- **디자인 헌법**: `rules/moai/design/constitution.md` — 파이프라인 순서·5 안전 계층·GAN 루프 계약·평가자 관대성 방지(FROZEN).
- **설정**: `config/design.yaml` — GAN 컨트롤·브랜드 컨텍스트·Claude Design 통합·design_docs 자동 로드.

## anti-slop 정본

디자인 카피의 AI 슬롭 패턴 사전(영문·한국어 Tier 1/2 + 구조 안티패턴)의 정본은 `moai-domain-copywriting`이며, 생성 단계에서 선제적으로 준수됩니다. `cd-slop-check`는 그 사전을 참조하는 **다운스트림 QA 게이트**입니다.

## 예약 경로 (런타임 산출물)

`.moai/design/`(토큰·컴포넌트·브리프), `.moai/project/brand/`(브랜드 컨텍스트), `.moai/sprints/`(Sprint Contract 아티팩트)는 **사용자 프로젝트 런타임 산출물 경로**입니다. 플러그인은 이 경로를 참조하되 스캐폴드하지 않습니다.

## 설계 문서

- 아키텍처: `docs/plugin-family-design/01-moai-design.md`
- 구축 스펙: `docs/plugin-family-design/03-moai-design-processing.md`

## 라이선스

LicenseRef-MoAI-NC-ND-1.0
