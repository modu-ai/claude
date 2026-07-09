# 코워커 (moai-coworker)

실무 범용 코어 AI 직원입니다. 사업 전략·브랜드·제안서·협상·고객 대응·프로세스 관리 등 어느 업종에나 필요한 비즈니스 실무 스킬 41종을 제공합니다. 슬래시 명령을 외울 필요 없이 자연어로 요청하면 매칭되는 스킬이 자동 호출됩니다.

**이런 분께 추천**: 1인 사업자 · 스타트업 운영자 · 실무 전반을 혼자 처리하는 분

## 전문가 플러그인으로의 분리 안내 (v6.0.0)

기존 코워커의 전문 영역 스킬은 8개 전문가 플러그인으로 이관되었습니다. 아래 표의 요청은 해당 플러그인을 설치하면 그대로 이어서 쓸 수 있습니다.

| 이런 요청은 | 이 플러그인으로 | 이관 스킬 |
|-------------|-----------------|-----------|
| 책·웹툰·웹소설·시나리오·IP | `moai-writer` (작가) | book-*, story-*, 한국어 윤문 (23종) |
| 캠페인·콘텐츠·SNS·미디어 생성 | `moai-marketer` (마케터) | marketing-*, content-*, media-* (28종) |
| 상세페이지·마켓·광고·CRM | `moai-seller` (셀러) | commerce-* (31종) |
| 오피스 문서·공공데이터·생산성 | `moai-officer` (사무관) | office-*, general 생활 (31종) |
| 계약·법령·판례·특허 | `moai-lawyer` (법무 담당) | legal-* (9종) |
| 재무제표·결산·세금·재테크 | `moai-accountant` (재무·세무 담당) | finance-* (11종) |
| 채용·이력서·면접·평가 | `moai-recruiter` (인사·채용 담당) | business HR (8종) |
| 커리큘럼·평가·논문 | `moai-tutor` (튜터) | education-* (11종) |

## 설치

```
claude plugin marketplace add modu-ai/claude
claude plugin install moai-coworker@moai-claude
```

또는 Claude Code 세션 안에서:

```
/plugin marketplace add modu-ai/claude
/plugin install moai-coworker
```

## 스킬 41종

호출 형식: `/moai-coworker:<스킬명>` — 예: `/moai-coworker:business-strategy-planner`. 자연어 요청("사업계획서 써줘")으로도 자동 매칭됩니다.

### 전략·기획 (8종)

| 스킬 | 역할 |
|------|------|
| `business-strategy-planner` | 사업 전략 수립 |
| `business-startup-launchpad` | 창업 론칭 로드맵 |
| `business-market-analyst` | 시장·경쟁 분석 |
| `business-sbiz365-analyst` | 소상공인365 상권 분석 |
| `business-brand-identity` | 브랜드 아이덴티티 설계 |
| `business-roadmap-manager` | 로드맵·마일스톤 관리 |
| `business-consulting-brief` | 컨설팅 브리프 작성 |
| `business-kr-gov-grant` | 정부지원사업 공고 분석·신청 |

### 문서·커뮤니케이션 (10종)

| 스킬 | 역할 |
|------|------|
| `business-proposal-writer` | 제안서 작성 |
| `business-spec-writer` | 요구사항·기획 명세 작성 |
| `business-executive-summary` | 경영진 요약 보고 |
| `business-status-reporter` | 진행 상황 보고 |
| `business-pm-weekly-report` | PM 주간 보고 |
| `business-productivity-weekly-report` | 생산성 주간 회고 |
| `business-report-speak` | 보고 스피치 스크립트 |
| `business-kb-article` | 사내 지식베이스 문서 |
| `business-draft-offer` | 제안·견적 초안 |
| `business-draft-response` | 회신·답변 초안 |

### 고객·관계 관리 (7종)

| 스킬 | 역할 |
|------|------|
| `business-ticket-triage` | 고객 문의 분류·대응 |
| `business-escalation-manager` | 에스컬레이션 대응 |
| `business-conflict-handler` | 갈등 상황 대응 |
| `business-negotiation-1on1` | 1:1 협상 준비 |
| `business-vendor-manager` | 협력사·벤더 관리 |
| `business-sales-playbook` | 영업 플레이북 |
| `business-feedback-loop` | 피드백 수집·개선 루프 |

### 운영·UX (4종)

| 스킬 | 역할 |
|------|------|
| `business-process-manager` | 업무 프로세스 설계·개선 |
| `business-meeting-facilitator` | 회의 설계·퍼실리테이션 |
| `business-ux-researcher` | UX 리서치 |
| `business-ux-designer` | UX 설계 |

### 품질·범용 도구 (12종)

| 스킬 | 역할 |
|------|------|
| `general-ai-slop-reviewer` | AI 티 나는 문장 검수 (모든 텍스트 산출물 마지막 단계) |
| `general-ai-diagnostic` | AI 산출물 품질 진단 |
| `general-feedback` | 피드백 정리·반영 |
| `general-cd-brief` | Claude Design 브리프 |
| `general-cd-system-prep` | Claude Design 시스템 준비 |
| `general-cd-prompt-builder` | Claude Design 프롬프트 빌더 |
| `general-cd-handoff-reader` | Claude Design 핸드오프 해석 |
| `general-cd-slop-check` | 디자인 슬롭 체크 |
| `general-skill-builder` | 커스텀 스킬 제작 |
| `general-skill-template` | 스킬 템플릿 |
| `general-skill-tester` | 스킬 테스트 |
| `claude-prompting-basics` | 클로드 프롬프팅 기본기 |

## MCP 연동 1종

| 서버 | 플랫폼 | 필요 환경변수 | 비고 |
|------|--------|---------------|------|
| `dart` | OpenDART 전자공시 (83 API → 15 도구) | `DART_API_KEY` | business-market-analyst 등 시장·공시 분석에 사용. 키 발급: opendart.fss.or.kr (무료) |

## 라이선스

LicenseRef-MoAI-NC-ND-1.0 · © modu-ai (email@mo.ai.kr)
