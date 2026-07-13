# 모두의 코워크 (MoAI) — `moai-cowork` 마켓플레이스

한국 실무 4종 플러그인 패밀리를 한 곳에. Claude Code / Claude Desktop에서 한 번의 등록으로 네 플러그인을 모두 만나고, 필요한 것만 설치합니다.

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
├── README.md
└── LICENSE
```

> 이 저장소는 **마켓플레이스 + 문서**만을 다룹니다. MoAI-ADK 개발 환경(에이전트/규칙/스킬 설정 등)은 별도 관리되며 `.gitignore`로 이 저장소에서 제외됩니다.

## 라이선스

[LicenseRef-MoAI-NC-ND-1.0](./LICENSE) — 비상업적 사용 허용, 2차적 저작물(변경본) 배포 금지.

## 더 보기

- 문서 사이트: [claude.mo.ai.kr](https://claude.mo.ai.kr)
