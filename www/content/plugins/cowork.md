---
title: "MoAI-Cowork 플러그인"
weight: 10
description: "Claude Cowork용 28종 플러그인 — 업무·콘텐츠·미디어·분석을 AI로 자동화하는 스킬 모음"
geekdocBreadcrumb: true
---

# MoAI-Cowork 플러그인

Claude Cowork에서 바로 사용할 수 있는 **28종 플러그인** 패키지입니다. 설치 후 `/` 명령어로 스킬을 호출하거나, 자연어로 작업을 요청하면 Claude가 알맞은 스킬을 자동으로 선택합니다.

{{< hint type="note" >}}
**현재 사용 가능한 유일한 플러그인 라인입니다.** MoAI-Code와 MoAI-Design은 출시 예정입니다.
{{< /hint >}}

## 설치 방법

Claude Cowork 사이드바 → **플러그인** → **마켓플레이스** → `cowork-plugins` 검색 후 설치.

업데이트 시: `/plugin marketplace update cowork-plugins`

---

## 28종 플러그인 한눈에 보기

### 핵심

| 플러그인 | 설명 |
|---|---|
| [moai-core](/plugins/moai-core) | 프로젝트 설정, AI 슬롭 검수, 문서 품질 관리 |

### 콘텐츠·미디어

| 플러그인 | 설명 |
|---|---|
| [moai-content](/plugins/moai-content) | 블로그, SNS, 뉴스레터, 랜딩 페이지, 카드뉴스, HTML 슬라이드 |
| [moai-media](/plugins/moai-media) | AI 이미지(Higgsfield) · 음성(ElevenLabs) 생성 |
| [moai-design](/plugins/moai-design) | 브랜드 디자인 시스템 · Figma 연동 |
| [moai-book](/plugins/moai-book) | 전자책·PDF 기획·집필·출판 |

### 업무·생산성

| 플러그인 | 설명 |
|---|---|
| [moai-office](/plugins/moai-office) | Word·Excel·PowerPoint·한글 문서 자동 생성 |
| [moai-productivity](/plugins/moai-productivity) | 할 일 관리, 회의록, 이메일 초안 |
| [moai-operations](/plugins/moai-operations) | SOP, 운영 매뉴얼, 프로세스 문서 |

### 비즈니스

| 플러그인 | 설명 |
|---|---|
| [moai-business](/plugins/moai-business) | 사업계획서, 투자 제안, 전략 보고 |
| [moai-marketing](/plugins/moai-marketing) | 마케팅 전략, 광고 카피, 캠페인 기획 |
| [moai-sales](/plugins/moai-sales) | 영업 제안서, 고객 이메일, 세일즈 덱 |
| [moai-commerce](/plugins/moai-commerce) | 쇼핑몰 상품 설명, 리뷰 관리, 온라인 판매 |
| [moai-pm](/plugins/moai-pm) | 프로젝트 관리, 일정·리소스 계획 |
| [moai-product](/plugins/moai-product) | 제품 로드맵, 요구사항 문서, PRD |

### 전문 분야

| 플러그인 | 설명 |
|---|---|
| [moai-finance](/plugins/moai-finance) | 재무 분석, 예산 계획, 회계 보고 |
| [moai-legal](/plugins/moai-legal) | 계약서 검토, NDA, 법률 문서 초안 |
| [moai-hr](/plugins/moai-hr) | 채용 공고, 인사 평가, 조직 관리 |
| [moai-research](/plugins/moai-research) | 리서치 보고서, 논문 요약, 데이터 분석 |
| [moai-data](/plugins/moai-data) | 데이터 시각화, 분석 리포트, 대시보드 |
| [moai-bi](/plugins/moai-bi) | BI 리포트, KPI 추적, 경영 지표 |

### 지식·교육

| 플러그인 | 설명 |
|---|---|
| [moai-education](/plugins/moai-education) | 강의 자료, 학습 콘텐츠, 교육 계획 |
| [moai-tutor](/plugins/moai-tutor) | 개인 학습 프로젝트, 튜터링, 학습 자료 |
| [moai-comms](/plugins/moai-comms) | 커뮤니케이션, PR 보도자료, 위기 대응 |

### 생활·기타

| 플러그인 | 설명 |
|---|---|
| [moai-lifestyle](/plugins/moai-lifestyle) | 여행 계획, 레시피, 생활 관리 |
| [moai-wealth](/plugins/moai-wealth) | 개인 자산 관리, 투자 분석, 재테크 |
| [moai-career](/plugins/moai-career) | 이력서, 자기소개서, 면접 준비 |
| [moai-support](/plugins/moai-support) | 고객 응대, FAQ, 서비스 매뉴얼 |
| [moai-public-data](/plugins/moai-public-data) | 공공데이터 수집·분석·시각화 |

---

## 자주 쓰는 조합 (체인)

```
블로그 발행: moai-content:blog → moai-core:ai-slop-reviewer
보고서 PDF: moai-office:docx-generator → moai-office:pdf-writer
AI 이미지 포함 콘텐츠: moai-content:* → moai-media:higgsfield-image
```

---

## 관련 링크

- [플러그인 허브 전체 보기](/plugins)
- [스킬 체이닝 가이드](/cookbook/skill-chaining)
- [자동화 레시피](/cookbook/automation-recipes)
