# moai-code — MoAI-ADK 무설치 플러그인

`moai` CLI **설치 없이** Claude Code 터미널·데스크탑에서 MoAI-ADK의 SPEC 개발 방법론(PLAN › RUN › SYNC)을 사용하는 플러그인입니다. **비개발자와 개발자 모두** `/moai` 명령으로 개발합니다.

## 설치

```bash
claude plugin marketplace add modu-ai/claude
/plugin install moai-code
```

## 명령 (14개)

플러그인 명령은 `플러그인명:명령` 콜론 네임스페이스로 노출됩니다. 이 플러그인의 `name`은 `moai`이므로 명령은 **`/moai:<name>`** 형태입니다(예: `/moai:plan`).

| 카테고리 | 명령 |
|---------|------|
| 워크플로우 | `/moai:plan` `/moai:run` `/moai:sync` |
| 유틸리티 | `/moai:fix` `/moai:loop` `/moai:clean` `/moai:mx` `/moai:review` |
| 품질 | `/moai:codemaps` `/moai:gate` `/moai:security` |
| 프로젝트 | `/moai:project` `/moai:harness` `/moai:feedback` |

- 명령은 flat `commands/*.md` 구조로 번들됩니다(서브디렉토리는 플러그인에서 typed 이름에 반영되지 않음 — 공식 문서 검증).
- 디자인 작업은 `moai-design` 플러그인의 `/design`을 사용하세요(D7 위임).
- `coverage`·`e2e`는 정본에서 은퇴되었습니다.

## 정본 기준 (parity-source)

이 플러그인은 `moai-adk-go`의 배포 템플릿 `internal/template/templates/`를 정본으로 삼아 무설치 완전 패리티로 재패키징합니다. 각 렌더 산출물 상단의 `<!-- parity-source: ... @ <commit> -->` 주석이 정본 커밋을 고정합니다.

## 빌드

```bash
bash scripts/render-templates.sh   # 정본 → 플러그인 트리 렌더/복사 (P1)
```

## 설계 문서

- 아키텍처: `docs/plugin-family-design/02-moai-code.md`
- 구축 스펙: `docs/plugin-family-design/04-moai-code-processing.md`

## 라이선스

LicenseRef-MoAI-NC-ND-1.0
