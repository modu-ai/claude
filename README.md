# 모두의 클로드 (MoAI) — `modu-ai/claude` 마켓플레이스

한국 실무 3종 플러그인 패밀리를 한 곳에. Claude Code / Claude Desktop에서 한 번의 등록으로 세 플러그인을 모두 만나고, 필요한 것만 설치합니다.

## 설치

```bash
claude plugin marketplace add modu-ai/claude
```

등록 후 플러그인별 설치:

```bash
claude plugin install moai-cowork@modu-ai/claude   # 실무 올인원
claude plugin install moai@modu-ai/claude           # 개발 방법론 (무설치)
claude plugin install design@modu-ai/claude         # 에이전틱 디자인
```

## 플러그인 카탈로그

| 플러그인 | 표면 | 한 줄 설명 |
|----------|------|-----------|
| **moai-cowork** (`/project` 외 자연어) | Cowork · Chat | 사업·이커머스·마케팅·콘텐츠·법률·재무·HR·교육·디자인·미디어 등 한국 실무 도메인 통합 올인원 |
| **moai** (`/moai`) | Code | SPEC plan/run/sync 개발 방법론 무설치 에디션 — DDD/TDD·품질 게이트·문서 동기화. 비개발자·개발자 모두 `/moai`로 개발 |
| **design** (`/design`) | Design | Claude Design 연동, 디자인 토큰(DTCG)·DESIGN.md·브랜드 시스템·GAN 품질 루프. 브리프부터 핸드오프까지 |

## 저장소 구조

```
modu-ai/claude/
├── .claude-plugin/marketplace.json   # 마켓 매니페스트 (3 plugins)
├── plugins/                          # 마켓 플러그인 소스
│   ├── moai-cowork/
│   ├── moai-code/                    # 설치명: moai
│   └── moai-design/                  # 설치명: design
├── www/                              # 문서 사이트 (claude.mo.ai.kr, Hugo)
├── README.md
└── LICENSE
```

> 이 저장소는 **마켓플레이스 + 문서**만을 다룹니다. MoAI-ADK 개발 환경(에이전트/규칙/스킬 설정 등)은 별도 관리되며 `.gitignore`로 이 저장소에서 제외됩니다.

## 라이선스

[LicenseRef-MoAI-NC-ND-1.0](./LICENSE) — 비상업적 사용 허용, 2차적 저작물(변경본) 배포 금지.

## 더 보기

- 문서 사이트: [claude.mo.ai.kr](https://claude.mo.ai.kr)
