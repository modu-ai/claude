---
name: general-cd-handoff-reader
description: |
  Claude Design → Claude Code 핸드오프 번들(공식 3요소: 디자인 파일 + chat + README)을 분석해 요약 보고서와 Claude Code에 넘길 짧은 지시 1줄을 자동 생성합니다.
  README를 먼저 읽어 구조·의도를 파악하고, 토큰·컴포넌트 JSON이 있으면 best-effort로 활용하되 없으면 CSS·HTML("code under the hood")에서 토큰·컴포넌트 트리를 유도합니다.

  다음과 같은 요청 시 반드시 이 스킬을 사용하세요:
  - "Claude Design 핸드오프 번들 분석"
  - "handoff 번들 요약"
  - "핸드오프 번들 읽어 줘"
  - "디자인 토큰 추출"
  - "Claude Code 핸드오프 준비"
version: "4.0.0"
---
<!-- moai-cowork v4.0.0 · 3-point sync: plugin.json "version":"4.0.0" = SKILL.md version 4.0.0 = marketplace metadata.version 4.0.0 (REQ-STORY-006/NFR-STORY-003) -->

# general-cd-handoff-reader — 핸드오프 번들 분석

## 개요

Claude Design은 핸드오프 시 **공식적으로는 3가지 coarse 항목**(디자인 파일 + chat + README)을 묶어 전달합니다 — Anthropic은 디자인을 "code under the hood(HTML/CSS/JS)"로 규정하며, 구조화된 DTCG JSON을 공식 규격으로 문서화하지 않았습니다. `design-tokens.json`·`components.json` 같은 세부 파일명은 **MoAI 작업 가정이며 Anthropic 문서화 규격이 아닙니다**. 이 스킬은 그 번들을 분석해 **사람이 5분 안에 핸드오프 상태를 파악**할 수 있는 요약 보고서와 **Claude Code에 그대로 붙여 넣을 수 있는 지시 1줄**을 만들어 줍니다.

> **핸드오프 출처 (2026-06 업데이트)**: 이 번들은 Claude Design 캔버스의 **Export → Hand off to Claude Code**(local 또는 web)에서 생성됩니다. 반대 방향(코드→디자인)은 Claude Code 터미널의 `/design-sync`로 코드베이스 디자인 시스템을 Claude Design에 import합니다 — 즉 핸드오프는 단방향이 아니라 양방향입니다.

## 트리거 키워드

Claude Design 핸드오프, handoff 번들, design-tokens 분석, components.json, Claude Code 인계, 디자인 토큰 추출

## 입력 — 2가지 진입 모드

Claude Design "Handoff to Claude Code"의 실제 흐름은 아래 2가지입니다:

| 진입 모드 | 형태 | 비고 |
|---|---|---|
| **붙여넣기 프롬프트 + 번들 URL** (메인 흐름) | Export 시 제공된 준비된 프롬프트 + 번들 URL | Claude Code가 URL을 fetch해 컨텍스트에 로드 — 그 로드된 내용을 분석 |
| **`.zip` 다운로드** (오프라인 컨테이너) | `./handoff-bundle.zip` 또는 압축 해제된 `./handoff-bundle/` 디렉토리 | "Download as .zip" = raw 디자인 파일 + assets + README |

## 워크플로우

### 1단계 — README 우선 파싱 + 방어적 glob

**정확한 번들 형식은 Anthropic이 공식 문서화하지 않았습니다.** 따라서 하드 5-파일 체크를 하지 않고 방어적으로 처리합니다. 공식 규격은 **3가지 coarse 항목(디자인 파일 + chat + README)** 뿐이며, 아래 세부 JSON 파일명은 **MoAI 작업 가정이지 Anthropic 문서화 규격이 아닙니다**.

**(1) README 우선 (source of truth)** — 번들에서 README를 **가장 먼저** 읽어 구조·의도를 파악합니다. Anthropic이 "모델에게 디자인 해석 지침을 주도록" 설계한 **유일한 공식 문서화 요소**입니다. (`README.md` 확장자는 추론이므로 `README*`로 glob.)

**(2) 나머지는 선택적 best-effort glob** — 아래 JSON은 있으면 활용하고 없어도 실패하지 않습니다:

```
handoff-bundle/            # 폴더 / URL fetch 결과 / zip 무엇이든
├── README*                ← 공식(개념 실재), 가장 먼저 파싱
├── (디자인 파일)           ← 공식: HTML/CSS/JS "code under the hood"
├── (chat)                 ← 공식(개념 실재), 파일명은 미문서화
├── design-tokens.json / tokens.json   ← 추론(선택) — 두 이름 모두 수용
├── components.json        ← 추론(선택)
├── layout-hierarchy.json  ← 추론(선택)
└── assets/                ← 참조 자산(개념 실재), 폴더명 추론
```

**(3) 존재하는 것 파싱 + fallback** — 하드 요구·reject 금지:

| 대상 | 있을 때 | 없을 때 (fallback) |
|---|---|---|
| README | 구조·의도·컴포넌트 매핑 가이드 파싱 | (핵심 요소) 없으면 디자인 파일 코드에서 의도 추측 — 경고 |
| 토큰 JSON | `design-tokens.json` **또는** `tokens.json` 둘 다 수용 | **CSS custom properties / standalone HTML에서 토큰 유도** ("code under the hood") |
| 컴포넌트 JSON | `components.json` 컴포넌트 트리 사용 | **HTML DOM 구조에서 컴포넌트 트리 추론** |
| 레이아웃 JSON | `layout-hierarchy.json` 반응형 정보 사용 | HTML/CSS 미디어쿼리에서 반응형 패턴 추론 |
| chat | 디자인 결정 맥락 추출 | 맥락 약화 — 코드만으로 추론임을 명시 |

**(4) 파일명 분열 정규화** — general-cd-handoff-reader(`design-tokens.json`) ↔ moai-workflow-design(`tokens.json`) 두 이름을 모두 수용하고, `.moai/design/` 출력 시 한 이름으로 정규화합니다.

**(5) version gating 완화** — 알 수 없거나 없는 bundle version은 **best-effort 파싱 + 경고**로 처리하며 hard-reject하지 않습니다. (bundle version "1.0"은 Anthropic 근거가 없는 MoAI placeholder입니다.)

### 2단계 — 각 파일 분석

#### README.md 분석

- 프로젝트 목표·범위
- 컴포넌트 매핑 가이드
- 의도된 사용자 플로우
- 알려진 제약·미완성 부분

#### design-tokens.json 분석

```
- 색 토큰 N개 (primary·secondary·semantic 구분)
- 타이포 N개 (family·size·weight 스케일)
- 간격 N개 (spacing scale)
- 모서리·그림자·전환 등
- 시맨틱 매핑 정확도 (예: primary/500 → #2a8a8c)
```

#### components.json 분석

```
- 사용된 컴포넌트 N개
- 컴포넌트 트리 (depth·중첩)
- variants·states 명시 여부
- 기존 코드베이스 컴포넌트와 매칭 가능성
```

#### layout-hierarchy.json 분석

```
- 페이지 수
- 반응형 변형 정의 여부 (mobile·tablet·desktop)
- 그리드·간격 일관성
- 인터랙티브 요소 (호버·클릭·드래그) 목록
```

#### chat-history.md 분석

```
- 주요 디자인 결정과 이유 추출
- 사용자가 명시한 제약·우선순위
- 거부된 대안 (왜 안 했는가)
- 미해결 질문
```

### 3단계 — 요약 보고서 생성

```markdown
# 핸드오프 번들 분석 — [프로젝트명]

## 한눈에 보기

| 항목 | 내용 |
|---|---|
| 페이지 수 | N |
| 컴포넌트 수 | N (그중 기존 코드와 매칭 가능: M) |
| 디자인 토큰 | 색 N·타이포 N·간격 N |
| 인터랙티브 요소 | N (호버·클릭·드래그) |
| 반응형 정의 | mobile·tablet·desktop 모두 / 일부 / 없음 |
| 엣지 상태 | empty·error·loading 정의 여부 |

## 디자인 토큰 요약

### 색
- primary/500: #[hex] (기존 토큰과 일치 / 새로움)
- ...

### 타이포
- Display: [폰트] [size]
- ...

## 컴포넌트 트리

```
Page
├─ Hero
│  ├─ Headline (h1)
│  ├─ Subheadline (h2)
│  └─ CTA Button (primary, large)
├─ FeatureGrid (3-col)
│  ├─ FeatureCard × 6
│  └─ ...
└─ Footer
```

## 디자인 결정 맥락 (chat-history.md에서 추출)

1. 사이드바 대신 탭 선택 — 이유: 사용자가 모든 섹션 동시 인지 필요
2. 흰 배경 + 단일 강조색 — 이유: 기존 마케팅 사이트 톤 유지
3. ...

## 미해결 질문

- [ ] 결제 페이지의 카드 위젯이 기존 ChargeCard와 호환되는가?
- [ ] 다크 모드 변형이 정의되어 있지 않음
- [ ] ...

## 구현 우선순위 (추천)

1. P0: Hero · CTA (전환 핵심)
2. P1: FeatureGrid (스크롤 다음 영역)
3. P2: Footer · 보조 페이지
4. P3: 다크 모드 변형 (정의 후 추가)

## Claude Code 핸드오프 지시 (복붙용)

```
이 핸드오프 번들을 받아 프로덕션 코드로 구현해 줘.
번들 URL: [URL]
기존 디자인 시스템 토큰을 그대로 사용. 컴포넌트는 우리 React 라이브러리
([ChargeCard·FeatureGrid·CTA 등 매칭 컴포넌트])로 매핑. 결과를 로컬에서
미리보기 가능하게 (npm run dev). chat-history.md의 디자인 결정 맥락을
존중. 다크 모드는 정의 후 별도 라운드로.
```
```

### 4단계 — 후속 권장

#### 두 경로 분기

| 경로 | 사용 시점 | 본 스킬의 역할 |
|---|---|---|
| **Claude Code 빌드 경로** (1차 목적) | 프로덕션 코드로 구현해야 할 때 | 번들 분석 + Claude Code 1줄 지시 자동 생성 (아래 워크플로우) |
| **Canva 마케팅 후속 경로** (Anthropic ↔ Canva 공식 파트너십) | 마케팅 팀이 SNS·이벤트·광고 변형을 후속 편집해야 할 때 | 본 스킬의 분석은 참고용. 실제 Canva export는 Claude Design 캔버스의 Export → Canva 메뉴에서 직접 실행 |

두 경로를 동시에 진행하면 디자인이 두 도구에서 동시에 변형되어 일관성이 깨집니다. **한 시안에서 한 경로만** 운영하세요.

```
## 다음 단계 (Claude Code 빌드 경로)

1. 위 Claude Code 핸드오프 지시를 복사
2. Claude Code 터미널 또는 Web에서 붙여넣기
3. 첫 빌드 후 로컬 미리보기 확인
4. 코드와 디자인 차이가 있으면:
   - 작은 차이: Claude Code에서 수정 지시
   - 큰 차이: Claude Design으로 돌아가 재디자인 → 새 핸드오프

## 주의

- 핸드오프 후 디자인을 또 수정하지 마세요 — 코드와 어긋납니다
- 큰 디자인 변경은 새 핸드오프 번들 작성 후 부분 인계
- 마케팅 후속(Canva 경로)이 필요하면 핸드오프 번들과 별개로 Claude Design 캔버스에서 직접 Export → Canva
```

## 사용 예시

### 예시 1 — 완전한 번들

```
입력: ./handoff-bundle/ (README + 디자인 파일 + 토큰·컴포넌트 JSON 포함)

결과:
- 페이지 4개, 컴포넌트 18개 (기존 매칭 14)
- 색 8개, 타이포 5개, 간격 8개
- 디자인 결정 5개 추출
- 미해결 질문 3개
- Claude Code 지시 1줄 생성
```

### 예시 2 — 부분 번들 (chat-history.md 누락)

```
입력: ./handoff-bundle/ (chat-history.md 없음)

결과:
- 다른 파일 정상 분석
- chat-history.md 누락 경고 — 디자인 의도가 코드로만 추론됨
- Claude Code 지시는 생성 (맥락이 약해진 점 명시)
- 후속 권장: Claude Design 채팅 화면을 캡처해 별도 참고 자료로
```

### 예시 3 — ZIP 압축 번들

```
입력: ./handoff-bundle.zip

처리:
1. unzip으로 ./handoff-bundle/ 추출
2. 위 예시 1·2와 동일 절차
3. 분석 후 ZIP 원본은 백업 용도로 보존
```

## 출력 형식

```
## 핸드오프 번들 분석 결과

### 번들 상태
- 위치: [경로]
- 포함 파일: [목록]
- 누락 파일: [있다면]

### 한눈에 보기 테이블
[페이지·컴포넌트·토큰·인터랙티브·반응형·엣지]

### 디자인 토큰 요약
[색·타이포·간격]

### 컴포넌트 트리
[ASCII 트리]

### 디자인 결정 맥락
[chat-history에서 추출한 결정 5-10개]

### 미해결 질문
[체크리스트]

### 구현 우선순위
[P0-P3]

### Claude Code 지시 (복붙용)
[1단락 지시문]
```

## 주의사항

### Do

- README를 가장 먼저 읽고, 존재하는 파일은 가능한 한 분석 (JSON은 선택적 best-effort)
- 컴포넌트 이름이 기존 코드와 매칭되는지 명시 — Claude Code의 결과 품질을 결정
- 디자인 결정 맥락을 압축 — 5-10개로 추출
- 미해결 질문을 분리 — 구현 시작 전 결정 필요

### Don't

- 번들 분석을 핸드오프 절차의 대체로 쓰지 말 것 — 항상 Claude Code에 번들을 직접 인계
- 디자인 토큰을 임의로 변경 금지 — Claude Code가 그대로 사용해야 일관성
- chat-history.md의 결정 맥락을 임의 해석 금지 — 인용 형태로 보존

## 관련 스킬

| 스킬 | 사용 시점 |
|---|---|
| `moai-cowork:general-cd-brief` | 선행: 핸드오프할 시안 자체를 만들 때 |
| `moai-cowork:general-cd-system-prep` | 선행: 디자인 시스템 셋업 |
| `moai-cowork:project` | 후속: Claude Code 작업 폴더 초기화 |
| `moai-cowork:business-spec-writer` | 보조: 핸드오프 후 코드 SPEC 작성 |
