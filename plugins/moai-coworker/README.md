# moai-coworker (코워커) — 실무와 글쓰기를 모두 품은 올인원 동료

> **코워커**는 사업·마케팅·콘텐츠·문서·법무·세무부터 출판·웹툰·웹소설·시나리오·IP 창작까지, **실무 작업과 글쓰기 작업을 모두 처리하는** 올인원 동료입니다. 상황에 따라 **실무 동료 모자**와 **글쓰기 작가 모자**를 자동으로 바꿔 씁니다.

---

## 두 개의 모자

코워커는 한 명의 동료가 **두 가지 역할**을 상황에 맞춰 처리합니다. 사용자가 뭘 말하느냐에 따라 알맞은 모자를 자동으로 착용합니다.

| 모자 | 언제 착용 | 무엇을 하나요 |
|------|-----------|---------------|
| 🧑‍💼 **실무 동료** | 사업·마케팅·콘텐츠·문서·계약·세무·이커머스·미디어·교육·인사 요청 | 사업계획서, 블로그, 카드뉴스, 뉴스레터, PPT, 한글 문서, Excel, 계약서, 부가세 신고, 상세페이지, 캠페인, 주간보고, 강의 커리큘럼 등 |
| ✍️ **글쓰기 작가** | 소설·웹툰·웹소설·시나리오·콘티·출판·원고·IP 창작 요청 | 출판 원고 풀스택(기획→개요→집필→퇴고), 웹툰 기획·에피소드·아트, 웹소설 연재, 시놉·시나리오, 콘티·광고 콘티, 캐릭터 시트, 표지 일러스트, 프리비즈, IP 사업화 |

모자는 슬래시 명령 없이 **자연어만으로 자동 교체**됩니다. "사업계획서 써줘"면 실무 동료 모자, "웹소설 연재할래"면 글쓰기 작가 모자를 씁니다.

---

## 무엇을 하나요 (192스킬)

단일 플러그인 안에 **192개 스킬**이 도메인별로 통합되어 있습니다. 이전의 여러 실무 플러그인(사업·마케팅·법무·세무·HR·운영·교육·이커머스·미디어·캐리어·데이터·연구·출판 등)과 작가 플러그인(story) 전부를 하나로 흡수했습니다.

| 도메인 | 대표 스킬 |
|--------|----------|
| 사업·전략 | business-strategy-planner, business-market-analyst, finance-investor-relations, business-startup-launchpad |
| 마케팅 | marketing-seo-audit, marketing-campaign-planner, marketing-landing-page, marketing-meta-ads-manager |
| 콘텐츠 | content-blog, content-card-news, content-newsletter, content-copywriting, content-sns-content |
| 문서·오피스 | office-docx-generator, office-pptx-designer, office-xlsx-creator, office-hwpx-writer, office-pdf-writer |
| 법무·세무 | legal-contract-review, legal-nda-triage, finance-tax-helper, finance-financial-statements |
| 이커머스 | commerce-product-detail, commerce-marketplace-naver, commerce-detail-page-copy |
| 미디어 | media-higgsfield-image, media-higgsfield-video, media-audio-gen (ElevenLabs) |
| **출판 원고** | book-concept-planner → book-outline-designer → book-chapter-writer → book-revision-coach |
| **작가·IP** | story-webtoon-planner, story-webnovel-writer, story-synopsis, story-screenplay, story-conti, story-character-sheet, story-cover-art, story-previz, story-ip-pitch |
| 후처리 | general-ai-slop-reviewer (모든 텍스트 산출물 필수 마지막 단계), general-humanize-korean (한국어 정밀 윤문) |

> 작가/IP 워크플로우는 `story-project` 스킬이 장르별 파이프라인으로 자동 라우팅합니다.

---

## 사용법

### 그냥 말걸기 (슬래시 명령 불필요)

```
"사업계획서 PPT로 만들어줘"
→ [실무 동료 모자] business-strategy-planner → office-pptx-designer → general-ai-slop-reviewer

"인스타 카드뉴스 5장 만들어줘"
→ [실무 동료 모자] content-card-news → general-ai-slop-reviewer

"로맨스 웹소설 연재 시작하고 싶어"
→ [글쓰기 작가 모자] story-project → story-webnovel-writer

"출판할 책 기획하고 싶어"
→ [글쓰기 작가 모자] story-project → book-concept-planner → book-outline-designer → ...
```

### 모든 텍스트 산출물은 AI 맛 제거로 마무리

블로그·뉴스레터·카피·사업계획서·계약서 등 텍스트 산출물은 마지막에 반드시 `general-ai-slop-reviewer`로 AI 특유의 패턴을 제거하고, 한국어는 `general-humanize-korean`으로 정밀 윤문합니다.

---

## 프로젝트 시작하기

처음 프로젝트를 셋업할 때는 **PM** 플러그인의 `/project --cowork`가 코워커 체인을 설계해 줍니다.

```
/project --cowork
"카페 창업 사업계획서랑 SNS 콘텐츠 만들 거야"
→ PM이 코워커 스킬 체인을 설계하고 CLAUDE.md를 생성
```

자세한 건 [moai-pm README](../moai-pm/README.md)를 참고하세요.

---

## 설치

```
/plugin install moai-coworker
```

`modu-ai/claude` 마켓플레이스. 코워커 하나로 실무 + 글쓰기 전 영역이 커버됩니다.

---

## 다른 AI 직원과 함께 쓰기

코워커는 4명의 AI 직원 중 한 명입니다.

| AI 직원 | 언제 |
|---------|------|
| 🧑‍💼 **코워커**(본 플러그인) | 실무·콘텐츠·작가 |
| 🎨 디자이너 | 브랜드·디자인 시스템·Claude Design |
| 💻 코더 | 개발·SPEC·품질 게이트 |
| 📋 PM | 프로젝트 시작 허브 (`/project`) |

디자인 자산이 필요하면 디자이너, 개발이 필요하면 코더, 프로젝트 셋업은 PM이 담당합니다.

---

**라이선스**: LicenseRef-MoAI-NC-ND-1.0 · **작성자**: 모두의AI · **버전**: 5.0.0
