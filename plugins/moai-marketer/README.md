# 마케터 (moai-marketer)

마케팅 전담 AI 직원입니다. 캠페인 기획·퍼포먼스 분석(marketing-*), 블로그·뉴스레터·SNS 콘텐츠(content-*), 이미지·오디오·영상 미디어 생성(media-*) 스킬 28종과 Meta Ads·게시 채널·ElevenLabs·Higgsfield MCP 연동을 하나의 플러그인으로 제공합니다. 슬래시 명령을 외울 필요 없이 자연어로 요청하면 매칭되는 스킬이 자동 호출됩니다.

**이런 분께 추천**: 마케터 · 콘텐츠 크리에이터 · 1인 브랜드

## 설치

Claude Code에서 두 단계로 설치합니다:

```
claude plugin marketplace add modu-ai/claude
claude plugin install moai-marketer@moai-claude
```

또는 Claude Code 세션 안에서:

```
/plugin marketplace add modu-ai/claude
/plugin install moai-marketer
```

## 스킬 28종

호출 형식: `/moai-marketer:marketing-<스킬명>` — 예: `/moai-marketer:marketing-campaign-planner`. 자연어 요청("이번 달 인스타 광고 캠페인 기획해줘")으로도 자동 매칭됩니다.

### 마케팅 (11종)

| 스킬 | 역할 |
|------|------|
| `marketing-campaign-planner` | 광고·SNS·이메일 통합 캠페인 기획(목표·채널·예산·KPI) |
| `marketing-meta-ads-manager` | 메타(페이스북·인스타) 광고 생성·온오프·예산 조정 (신규 광고는 항상 PAUSED 생성) |
| `marketing-meta-ads-analyzer` | 메타 광고관리자 엑셀 보고서 성과 진단·강도별 처방 리포트 |
| `marketing-performance-report` | GA4·네이버·메타·카카오·구글 데이터 통합 ROAS·KPI 성과 보고서 |
| `marketing-seo-audit` | 네이버·구글·AI 검색(GEO) 노출 점검 및 SEO 감사 보고서 |
| `marketing-landing-page` | 단독 전환 랜딩 1페이지 카피·코드 제작 |
| `marketing-landing-page-conversion-audit` | 기존 랜딩페이지 전환율 진단·우선순위 처방 |
| `marketing-pixel-audit` | 메타·구글 추적 픽셀 설치·설정 점검 리포트 |
| `marketing-target-script` | 타겟 고객 페인포인트 분석·채널별 맞춤 메시지 |
| `marketing-personal-branding` | 개인 브랜드 포지셔닝·콘텐츠·채널 전략 문서 |
| `marketing-youtube-podcast-planner` | 유튜브·팟캐스트 기획·대본·쇼노트 구성 |

### 콘텐츠 (8종)

| 스킬 | 역할 |
|------|------|
| `content-blog` | 네이버·티스토리·브런치·WordPress·Ghost용 블로그 포스팅(제목·본문·SEO 메타) |
| `content-newsletter` | 이메일 뉴스레터(제목·프리헤더·본문·CTA)와 구독자 확보 전략 |
| `content-email-sequence` | 가입·구매 후 단계별 자동 발송 이메일 시퀀스 설계(정보통신망법 준수) |
| `content-sns-content` | 인스타·스레드·X·링크드인·유튜브 쇼츠 등 채널별 SNS 게시글·캡션·해시태그 |
| `content-card-news` | 인스타·스레드·카카오 채널용 카드뉴스 4장(카피·디자인 가이드·이미지 프롬프트) |
| `content-copywriting` | 헤드라인·CTA·슬로건·광고 카피 후보 다중 생성 |
| `content-editorial-calendar` | 콘텐츠 발행 캘린더·채널별 게시 일정 기획 |
| `content-social-media` | (DEPRECATED) `content-sns-content`로 흡수 — 신규 호출은 새 스킬 사용 |

### 미디어 (9종)

| 스킬 | 역할 |
|------|------|
| `media-higgsfield-image` | Higgsfield MCP 기반 AI 이미지 생성 (자연어 한 줄) |
| `media-higgsfield-video` | Higgsfield MCP 기반 AI 영상 생성 (자연어 한 줄) |
| `media-audio-gen` | ElevenLabs MCP 기반 TTS(32개국어)·보이스 클로닝·더빙·효과음 |
| `media-gpt-image-2-prompt` | OpenAI GPT-image-2 전용 6-Block 이미지 프롬프트 빌더 |
| `media-gemini-3-image-prompt` | Gemini 3 Pro Image(Nano Banana Pro) 전용 5-component 프롬프트 빌더 |
| `media-midjourney-v8-prompt` | Midjourney v8.1 전용 키워드+파라미터 프롬프트 빌더 |
| `media-codex-image` | codex CLI 내장 image_gen으로 gpt-image-2 생성(API 키 불필요) |
| `media-notebooklm-slide-prompt` | 강연 마크다운 → NotebookLM 슬라이드 데크 + 슬라이드별 이미지 프롬프트 |
| `media-asset-production` | (별칭) 두 개의 스킬로 분리됨 — 신규 호출은 분리 스킬 사용 |

## MCP 연동 6종

플러그인 루트 `.mcp.json`에 6개 MCP 서버가 선언되어 있습니다. 자격증명은 **환경변수 또는 OAuth 로그인으로만** 설정하세요(파일에 키를 적지 않습니다).

| 서버 | 역할 | 인증 방법 |
|------|------|-----------|
| `meta-ads` | Meta 공식 Ads AI Connectors — 광고 생성·인사이트·카탈로그·픽셀 | 브라우저 Meta Business OAuth 2.0 (URL 등록 시 자동 발급, 정적 토큰 불필요) |
| `post-bridge` | 멀티채널 SNS 게시 브리지 | 원격 HTTP MCP — 최초 연결 시 계정 인증 |
| `typefully` | X·스레드 게시글 작성·예약 발행 | 원격 HTTP MCP — Typefully 계정 인증 |
| `wordpress` | WordPress.com 블로그 게시 | 원격 HTTP MCP — WordPress.com 계정 인증 |
| `ElevenLabs` | TTS·보이스 클로닝·더빙·효과음 (media-audio-gen 전용) | `ELEVENLABS_API_KEY` 환경변수 (elevenlabs.io에서 발급) + `uv` 사전 설치 |
| `higgsfield` | AI 영상·이미지 생성 (media-higgsfield-* 사용) | Higgsfield 계정 토큰 (mcp.higgsfield.ai) |

## 에이전트 2종

| 에이전트 | 등급 | 역할 |
|----------|------|------|
| `campaign-strategist` | worker | 캠페인 구조·콘텐츠 캘린더·크리에이티브 브리프·성과 리포트를 만드는 실무 에이전트. 목표 이해 → 계획 → marketing-*/content-*/media-* 스킬 선택 → 실행 → 검증의 에이전트 루프로 동작. 라이브 광고 상태 변경·외부 게시는 사용자 승인 없이 절대 수행하지 않음 |
| `performance-auditor` | read-only audit | 캠페인 플랜·예산 배분·카피·성과 보고서를 회의적으로 재검증하는 감사 에이전트. 출처 없는 벤치마크는 reject하고 증거 기반 PASS/FAIL 판정만 반환하며 파일을 수정하지 않음 |

## 이관 안내

기존 `moai-coworker`의 marketing-*/content-*/media-* 스킬은 본 플러그인으로 이관되었습니다 — 신규 호출은 `moai-marketer:<스킬명>` 네임스페이스를 사용하세요.

## 라이선스

LicenseRef-MoAI-NC-ND-1.0 · © modu-ai (email@mo.ai.kr)
