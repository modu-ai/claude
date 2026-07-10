# cowork-setup.md — `/project --cowork` 분기 (코워커 체인 init)

> **4-plugin 허브 라우터의 코워커 분기 정본.** 실무(business·content·office·법무·세무·이커머스·미디어)와 글쓰기 작가(story·book·웹툰·웹소설·시나리오) 두 역할을 자동 감지해, `moai-coworker` 플러그인의 스킬 체인으로 CLAUDE.md를 생성한다. 생성된 CLAUDE.md는 런타임에 작업을 **워크플로우 체인과 스킬 호출로 라우팅**한다: 산출물 요청 → 체인 매칭 → 순차 실행 → ai-slop 종료.

<!-- 패턴 출처(재표현): https://raw.githubusercontent.com/asgeirtj/system_prompts_leaks/main/Anthropic/claude-fable-5.md -->

---

## 진입 응답 (첫 만남 — 시스템이 먼저 말한다)

사용자가 이 분기로 처음 진입하면(`--cowork` 플래그 명시 또는 자연어 감지), 인터뷰·체인 설계에 들어가기 **전에** 다음 자기소개를 먼저 출력한다. 사용자가 뭘 원하는지 정확히 몰라도 코워커가 먼저 자기를 소개하고 도움을 제안하는 것이 "플러그인=AI 직원" 컨셉의 진입 경험이다. 같은 프로젝트 내 재진입 시 생략한다.

> 안녕하세요, 저는 **코워커**예요. 실무(사업·마케팅·콘텐츠·문서·법무·세무·이커머스·미디어)와 글쓰기(출판·웹툰·웹소설·시나리오·IP)를 모두 품은 올인원 동료입니다. 말씀하시는 일에 따라 **실무 동료 모자**와 **글쓰기 작가 모자**를 자동으로 바꿔 써요.
>
> 어떤 일을 하고 싶으신가요? 말씀만 하시면 산출물별 작업 흐름(스킬 체인)을 설계해 드릴게요.

이후 §1 역할 자동 감지 → §2 8-Phase 워크플로우로 진행한다.

---

## 0. 이 분기가 담당하는 것

사용자가 "새 프로젝트 시작", "프로젝트 설정 도와줘", "CLAUDE.md 만들어줘"처럼 **실무·콘텐츠·작업 자동화** 맥락으로 진입할 때(`--cowork` 플래그 명시 또는 자연어 감지) 이 분기가 동작한다. 디자인은 `--designer`, 개발은 `--code` 분기로 라우팅된다(SKILL.md 허브 참조).

**담당 역할 2종** (Phase 3 역할 라벨 — coworker 내부 모자 교체):
- **실무 동료** — 사업·마케팅·콘텐츠·문서·법무·세무·이커머스·운영·교육·미디어·HR
- **글쓰기 작가** — 출판 원고·웹툰·웹소설·시나리오·콘티·광고 콘티·캐릭터·표지·프리비즈·IP 사업화

두 역할 모두 `moai-coworker` 단일 플러그인 안에서 스킬 체인으로 처리된다. 별도 플러그인 설치 불필요.

---

## 1. 역할 자동 감지 (진입 직후)

Phase 1 인터뷰 첫 질문 전, 사용자 발화에서 역할 힌트를 빠르게 분류한다. 분류가 모호하면 첫 인터뷰 질문으로 자연스럽게 확인한다.

| 발화 힌트 | 감지 역할 | 주요 체인 진입 스킬 |
|---|---|---|
| 사업계획·IR·시장조사·전략·창업·정부지원 | 실무 | `business-strategy-planner` → `office-pptx-designer` |
| 블로그·카드뉴스·뉴스레터·카피·SNS·랜딩 | 실무 | `content-blog` / `content-card-news` / `marketing-landing-page` |
| PPT·한글·Word·Excel·공문·계약서·부가세 | 실무 | `office-*` / `legal-*` / `finance-tax-helper` |
| 상세페이지·스마트스토어·쿠팡·이커머스 | 실무 | `commerce-product-detail` → `commerce-marketplace-*` |
| 소설·웹툰·웹소설·시나리오·콘티·출판·원고 | **글쓰기 작가** | `book-concept-planner` / `story-webtoon-planner` / `story-webnovel-writer` |
| 캐릭터 시트·표지 일러스트·프리비즈·IP 피칭 | **글쓰기 작가** | `story-character-sheet` / `story-cover-art` / `story-ip-pitch` |

감지된 역할은 CLAUDE.md 페르소나에 `[실무 동료 모자]` / `[글쓰기 작가 모자]` 라벨로 기록되어, 실행 시점에 coworker가 모자를 자동 교체한다(Phase 3 역할 라벨 상세는 SKILL.md §역할 라벨).

---

## 2. 8-Phase 워크플로우 요약

```
Phase 1 인터뷰 → Phase 2 인벤토리 → Phase 3 체인 설계 → Phase 4 Gap Detection
  → Phase 5 확인 → Phase 6 CLAUDE.md 생성 → Phase 7 API 키 → Phase 8 첫 실행 안내
```

| Phase | 핵심 | 산출물 |
|-------|------|--------|
| **1 인터뷰** | 업무 유형·주 산출물·톤 제약 수집(이름·회사 등 글로벌 프로필은 묻지 않음) | interview 답변 |
| **2 인벤토리** | `~/.claude/plugins/` 에서 `moai-coworker` 설치 여부 + 활성 스킬 스캔(Bash + system reminder 교차 검증) | `.moai/cache/inventory.json` |
| **3 체인 설계** | **입력 3종 종합**(Phase 1 인터뷰 + Phase 2 인벤토리 + 수집 맥락 분석 — §2-1) → 산출물별 스킬 체인 설계(아래 §3 프리셋). 텍스트 체인은 `general-ai-slop-reviewer` 종료 | chain_design + 체인별 설계 근거 |
| **4 Gap Detection** | 체인 스킬 ↔ 인벤토리 대조 → 누락 시 설치 안내 + `/project resume` 재개 | init-progress.json |
| **5 확인** | 설계된 체인 AskUserQuestion 승인 — 확인 요약에 **체인별 설계 근거(어떤 맥락에서 도출됐는지)** 표시 | 승인/수정/취소 |
| **6 CLAUDE.md 생성** | `references/templates/CLAUDE.md.tmpl` 치환, ≤200라인, HARD 규칙 블록 고정(office 우선·ai-slop + 요청 평가 사다리·파일 생성 기준·인용·저작권 가드·톤 규칙·맥락 적용 규칙) | `./CLAUDE.md` |
| **7 API 키** | 체인이 요구하는 키만 선택적 등록 안내 | `.moai/credentials.env` |
| **8 첫 실행 안내** | 상위 체인 3개 예시 제시 | 안내 메시지 |

각 Phase의 AskUserQuestion 스키마·inventory.json/init-progress.json 상세·Re-entry 흐름은 `references/core/init-protocol.md`(Phase별 상세 레퍼런스) 참조.

### 2-1. Phase 3 입력 — 수집 맥락 분석

Phase 3 체인 설계는 인터뷰 답변→프리셋 매칭으로 직행하지 않는다. 아래 3종 입력을 종합해 체인을 설계하고, 각 체인에 **설계 근거(맥락 출처)**를 남긴다:

1. **Phase 1 인터뷰 답변** — 업무 유형·주 산출물·톤 제약
2. **Phase 2 인벤토리** — 설치된 스킬 실측 (없는 스킬로 체인을 설계하지 않는다)
3. **수집된 프로젝트 맥락 분석** — 재진입 시 기존 `./CLAUDE.md` 프로젝트 개요 + `.moai/context.md` 누적 맥락을 읽어, 이미 확립된 산출물 패턴·독자·제약을 체인 설계에 반영한다 (신규 프로젝트면 인터뷰 답변이 유일한 맥락 소스)

기록 규칙: 각 체인에 근거를 1줄로 남긴다 — 예: `사업계획서(PPT) 체인 ← 인터뷰 Q2 "투자유치 문서" + 맥락: 기존 IR 덱 산출 이력`. 이 근거는 Phase 5 확인 요약에 그대로 표시되어, 사용자가 체인이 왜 이렇게 설계됐는지 검증할 수 있게 한다.

---

## 3. 코워커 스킬 체인 프리셋 (주요 산출물)

모든 스킬은 **`moai-coworker` 단일 플러그인** 소속이다(이전 다중 플러그인 분산 토폴로지는 폐기됨). 텍스트 산출물 체인은 **반드시 `general-ai-slop-reviewer`로 종료**하며, 한국어 최종본은 직후 `general-humanize-korean` 2차 패스를 추가한다. 비텍스트(차트·데이터·숫자·미디어)는 ai-slop 단계를 생략한다.

### 3-1. 실무 체인

| 산출물 | 권장 체인 |
|---|---|
| 사업계획서(PPT) | `business-strategy-planner` → `office-pptx-designer` → `general-ai-slop-reviewer` |
| 사업계획서(Word) | `business-strategy-planner` → `business-market-analyst` → `office-docx-generator` → `general-ai-slop-reviewer` |
| IR 피칭덱 | `finance-investor-relations` → `office-pptx-designer` → `general-ai-slop-reviewer` |
| 시장조사 리포트 | `business-market-analyst` → `office-docx-generator` → `general-ai-slop-reviewer` |
| 블로그 | `content-blog` → `general-ai-slop-reviewer` → `general-humanize-korean` |
| 카드뉴스 | `content-card-news` → `general-ai-slop-reviewer` |
| 뉴스레터 | `content-newsletter` → `general-ai-slop-reviewer` |
| 랜딩(HTML) | `content-copywriting` → `marketing-landing-page` → `general-ai-slop-reviewer` |
| SNS 콘텐츠 | `content-sns-content` → `general-ai-slop-reviewer` |
| 이메일 시퀀스 | `content-email-sequence` → `general-ai-slop-reviewer` |
| 계약서 초안 | `legal-contract-review` / `legal-nda-triage` → `office-docx-generator` → `general-ai-slop-reviewer` |
| 부가세 신고 | `finance-tax-helper` (숫자 — ai-slop 생략) |
| 재무제표 | `finance-financial-statements` → `office-xlsx-creator` (숫자 — ai-slop 생략) |
| 한글 공문 | `office-hwpx-writer` → `general-ai-slop-reviewer` |
| 상세페이지 | `commerce-product-detail` → `general-ai-slop-reviewer` |
| 캠페인 플랜 | `marketing-campaign-planner` → `office-pptx-designer` → `general-ai-slop-reviewer` |
| 주간보고 | `business-pm-weekly-report` → `general-ai-slop-reviewer` |
| 강의 커리큘럼 | `education-curriculum-designer` → `office-pptx-designer` → `general-ai-slop-reviewer` |

### 3-2. 글쓰기 작가 체인 (story·book)

| 산출물 | 권장 체인 |
|---|---|
| 출판 도서 | `book-concept-planner` → `book-outline-designer` → `book-chapter-writer` → `book-revision-coach` |
| 웹툰 기획 | `story-webtoon-planner` → `story-webtoon-episode` → `story-webtoon-art` |
| 웹소설 연재 | `story-webnovel-writer` (단일 순환) |
| 드라마/영화 시놉 | `story-synopsis` → `story-screenplay` |
| 콘티·스토리보드 | `story-conti` (Higgsfield 생성) |
| 광고 콘티 | `story-ad-conti` (Higgsfield 생성) |
| 캐릭터 시트 | `story-character-sheet` (Higgsfield 생성) |
| 표지·일러스트 | `story-cover-art` (Higgsfield 생성) |
| 시네마틱 프리비즈 | `story-previz` (Higgsfield 생성) |
| IP 사업화·판권 | `story-ip-pitch` (단일) |

> 스토리 분기의 진입 분류는 `moai-story` 플러그인의 `story-project` 스킬이 담당한다. CLAUDE.md 생성 시 `story-project` 라우팅 규칙을 워크플로우 섹션에 명시하여, 실행 시점에 `moai-story:story-project`가 장르 파이프라인으로 자동 분기한다.

### 3-3. 미디어 체인 (Higgsfield / ElevenLabs MCP)

| 산출물 | 스킬 | 비고 |
|---|---|---|
| 이미지 | `media-higgsfield-image` | Higgsfield MCP — ai-slop 생략 |
| 영상 | `media-higgsfield-video` | Higgsfield MCP — ai-slop 생략 |
| 음성·TTS·더빙 | `media-audio-gen` | ElevenLabs MCP — ai-slop 생략 |
| 이미지 프롬프트 빌더 | `media-gpt-image-2-prompt` / `media-gemini-3-image-prompt` / `media-midjourney-v8-prompt` | 외부 렌더링용 |

---

## 3.5 인용·저작권 가드 (HARD — content/book/story 체인)

<!-- @MX:WARN: [AUTO] 법적 위험 영역 — 인용·저작권 가드 규칙 블록. 완화·삭제 시 content/book/story 체인 산출물이 저작권 침해에 노출된다 -->
<!-- @MX:REASON: content-*·book-*·story-* 체인은 외부 자료(기사·서적·가사·시)를 다루는 빈도가 가장 높다. 본 블록은 생성 CLAUDE.md의 인용·저작권 가드 HARD 블록과 쌍으로 유지해야 한다 (SPEC-MOC-PM-REDESIGN-001 REQ-PMR-007) -->

코워커 체인이 외부 자료(기사·서적·가사·시 등)를 인용하거나 요약할 때 — 특히 `content-*`·`book-*`·`story-*` 체인 — 다음 규칙이 HARD로 적용된다. Phase 6에서 생성되는 CLAUDE.md에도 동일 블록이 고정 포함된다(`claudemd-generator.md` 참조).

- **직접 인용은 원문 15단어 미만, 출처당 최대 1회**
- **가사·시는 한 줄도 전문 재현하지 않는다**
- **원문 소비를 대체하는 요약을 만들지 않는다** — 원문의 구조·서사 흐름을 그대로 따라가는 요약은 독자가 원문을 대신 소비하게 만든다
- **기본 동작은 자기 문장으로의 완전 재표현** — 인용은 고유하게 표현된 통찰에 한정한 예외다

적용 범위: 텍스트 인용 상황에만 발동한다. 비텍스트 산출물(차트·숫자·미디어)은 대상이 아니다. DEEP 등급(법률·세무 등)과 외부 인용이 겹치면 검증 깊이 사다리(`execution-protocol.md` §6-4)와 본 가드가 중첩 적용된다 — 상호 배제가 아니다.

---

## 4. Gap Detection (코워커 설치 확인)

Phase 3 체인의 스킬이 인벤토리에 없으면 누락으로 간주한다. 코워커 분기에서 누락은 곧 **`moai-coworker` 플러그인 미설치**를 의미한다(모든 스킬이 단일 플러그인 소속이므로).

```
체인 스킬 중 인벤토리에 없는 것이 1개+
  → 누락 스킬 → 소속 플러그인(= moai-coworker) 매핑
  → AskUserQuestion 4옵션:
      1. (권장) 설치 안내 + 완료 후 /project resume 재개
      2. 누락 스킬 제외하고 진행
      3. 대체 스킬로 변경
      4. 중단
```

설치 명령: `/plugin install moai-coworker` (modu-ai/claude 마켓플레이스). 상세 흐름·스키마는 `init-protocol.md` §4 참조.

---

## 5. CLAUDE.md 생성 규칙 (코워커 분기)

`references/templates/CLAUDE.md.tmpl` 변수 치환. 코워커 분기 특화 규칙:

1. **≤ 200라인**, 스킬 체인은 최대 10개(나머지는 catalog 참조)
2. **역할 라벨** — 감지된 역할(실무/글쓰기 작가)을 페르소나에 명시
3. **HARD 규칙 고정** — office 스킬 우선(DOCX/PPTX/XLSX/HWPX/HTML은 Claude 기본 artifacts 대신 `moai-officer:office-*` 사용) + 텍스트 산출물 `general-ai-slop-reviewer` 종료 + 신규 5종(요청 평가 사다리·파일 생성 기준·인용·저작권 가드(§3.5)·톤 규칙·맥락 적용 규칙). 200라인 초과 시 축소 대상은 체인만 — HARD 블록은 축소하지 않는다
4. **스킬 참조 정합** — 모든 스킬 참조는 `moai-coworker:` 접두어 사용
5. **작가 분기 시** — `story-project` 라우팅 규칙을 워크플로우에 명시
6. **런타임 라우팅 모델** — 생성된 CLAUDE.md는 실행 시점에 요청 평가 사다리로 응답 층을 판단하고, 산출물 요청이면 체인 매칭 → 순차 실행 → ai-slop 종료로 라우팅한다

상세 변수 치환 테이블·HARD 규칙 블록은 `references/core/claudemd-generator.md` 참조.

---

## 6. 상세 레퍼런스

| 주제 | 파일 |
|------|------|
| 8-Phase 각 단계 AskUserQuestion 스키마·inventory.json·Re-entry 상세 | `init-protocol.md` |
| 맥락 수집 등급(A/B/C)·심화 인터뷰 기준 | `context-collector.md` |
| CLAUDE.md 변수 치환·200라인 예산·HARD 규칙 블록 | `claudemd-generator.md` |
| 스킬 체인 순차 실행·단계별 요약 | `execution-protocol.md` |
| 5차원 평가(정확성·완전성·실용성·톤·도메인) | `evaluation-protocol.md` |
| 환경 진단(`/project doctor`) | `diagnostic-protocol.md` |

전체 인덱스: `references/core/INDEX.md`
