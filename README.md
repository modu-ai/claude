# 모두의 코워크 (MoAI) — `moai-cowork` 마켓플레이스

한국 실무 4종 플러그인 패밀리 + 4트랙 한국어 문서 사이트를 한 곳에. Claude Code / Claude Desktop에서 한 번의 등록으로 네 플러그인을 모두 만나고, 비개발자부터 개발자까지 4가지 Claude 제품(Chat · Cowork · Design · Code) 활용 가이드를 제공합니다.

## 설치

```bash
claude plugin marketplace add modu-ai/moai-cowork
```

등록 후 플러그인별 설치 (`moai-cowork` 마켓):

```bash
/plugin install moai@moai-cowork              # 개발 방법론 (무설치, /moai)
/plugin install moai-coworker@moai-cowork     # 실무·콘텐츠 올인원
/plugin install moai-designer@moai-cowork     # 에이전틱 디자인
/plugin install moai-pm@moai-cowork           # 프로젝트 시작 허브 (/project)
```

## 플러그인 카탈로그

| 플러그인 | 표면 | 한 줄 설명 |
|----------|------|-----------|
| **moai** (`/moai`) | Code | SPEC plan/run/sync 개발 방법론 무설치 에디션 — DDD/TDD·품질 게이트·문서 동기화. 비개발자·개발자 모두 `/moai`로 개발 |
| **moai-coworker** (`/project` 외 자연어) | Cowork · Chat | 사업·이커머스·마케팅·콘텐츠·법률·재무·HR·교육·디자인·미디어 등 한국 실무 도메인 통합 올인원 |
| **moai-designer** (`/design`) | Design | Claude Design 연동, 디자인 토큰(DTCG)·DESIGN.md·브랜드 시스템·GAN 품질 루프. 브리프부터 핸드오프까지 |
| **moai-pm** (`/project`) | PM | 프로젝트 시작 허브 — `/project` 라우터가 코더·코워커·디자이너 분기로 안내 |

## 문서 사이트 — 4트랙 구조

문서 사이트 [claude.mo.ai.kr](https://claude.mo.ai.kr)는 비개발자(10~60대)를 위한 한국어 Claude 활용 가이드입니다. 학습 난이도 상승 순서로 4개 트랙을 제공하며, 각 트랙은 Anthropic 공식 자료(support.claude.com / docs.claude.com)에 정렬됩니다.

| 트랙 | 제품 | 학습 범위 |
|------|------|-----------|
| **Chat** | Claude Desktop App | 첫 대화·프롬프트·아티팩트·프로젝트·웹검색·리서치·확장사고·메모리·스킬·커넥터 |
| **Cowork** | Claude Cowork | "Claude Code for the rest of your work" — 자율 실행·프로젝트·스킬·플러그인·디스패치·컴퓨터사용·아키텍처 |
| **Design** | Claude Design | 디자인 시스템·컴포넌트·토큰·핸드오프 (Anthropic Labs 제품) |
| **Code** | Claude Code | 6가지 진입면(웹·데스크톱·IDE·CLI) — 비개발자도 터미널 없이 시작 |

목차의 진실 출처(SSOT)는 [`www/data/menu/main.yaml`](www/data/menu/main.yaml)입니다.

## 저장소 구조

```
modu-ai/moai-cowork/
├── .claude-plugin/marketplace.json   # 마켓 매니페스트 (4 plugins, name: moai-cowork)
├── plugins/                          # 마켓 플러그인 소스
│   ├── moai/                         # 설치명: moai (개발 방법론)
│   ├── moai-coworker/                # 설치명: moai-coworker
│   ├── moai-designer/                # 설치명: moai-designer
│   └── moai-pm/                      # 설치명: moai-pm
├── www/                              # 문서 사이트 (claude.mo.ai.kr, Hugo)
│   ├── content/guide/                # 4-트랙 가이드 (chat·cowork·design·code)
│   ├── data/menu/main.yaml           # 목차 SSOT (3축: 데스크탑·CLI·공통하단)
│   └── hugo.toml
├── README.md
└── LICENSE
```

> 이 저장소는 **마켓플레이스 + 문서**만을 다룹니다. MoAI-ADK 개발 환경(에이전트/규칙/스킬 설정 등)은 별도 관리되며 `.gitignore`로 이 저장소에서 제외됩니다.

## 라이선스

[LicenseRef-MoAI-NC-ND-1.0](./LICENSE) — 비상업적 사용 허용, 2차적 저작물(변경본) 배포 금지.

## 더 보기

- 문서 사이트: [claude.mo.ai.kr](https://claude.mo.ai.kr)
