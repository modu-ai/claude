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

## 패리티 계약 (`/moai:project` ↔ `moai init`)

`/moai:project`(무설치)와 `moai init`(바이너리)은 **동일 `.claude/` + `.moai/` 파일 트리**를 생성한다(REQ-BD-005 / AC-BD-002).

**유일한 값 발산 지점**: `.moai/config/sections/system.yaml`의 `version` 필드.
- `moai init`(바이너리): 템플릿 정본의 `{{.Version}}` 플레이스홀더가 실제 바이너리 버전으로 렌더링된다(예: `3.0.0-rc6`).
- `/moai:project`(무설치): 바이너리 셸아웃이 없으므로 템플릿 렌더링이 불가하다 → 리터럴 마커 `"plugin-deployed vX.Y.Z"`를 `system.yaml`의 `version` 필드에 기입한다(REQ-BD-006 / AC-BD-003). 이 `plugin-deployed` 마커는 나중에 `moai doctor`가 탐지해 바이너리 관리 트리로의 승격을 제안하는 착지점이 된다(REQ-BD-007 — 본 SPEC 범위 외, 후속 SPEC).

**검증 하네스 (AC-BD-002 RUNTIME)** — 두 진입점의 산출 트리를 빈 디렉터리 A, B에서 각각 실행 후 비교:

```bash
CNT_A=$(cd A && find .claude .moai -type f | wc -l)
CNT_B=$(cd B && find .claude .moai -type f | wc -l)
[ "$CNT_A" -gt 10 ] && [ "$CNT_B" -gt 10 ] || { echo "FAIL: 빈 트리(하네스 미실행)"; exit 1; }
diff <(cd A && find .claude .moai -type f | sort) \
     <(cd B && find .claude .moai -type f | sort)   # 출력 없음 = PASS(버전 라인만 유일한 발산)
# 값 발산 1지점 확인:
grep '^\s*version:' B/.moai/config/sections/system.yaml   # → "plugin-deployed vX.Y.Z"
grep '^\s*version:' A/.moai/config/sections/system.yaml   # → 실제 바이너리 버전
```

`non-empty` 가드(`> 10`)는 빈-vs-빈 거짓 통과를 차단한다. 파일 집합 자체는 동일하며, 유일한 값 발산은 위 한 줄뿐이다.

## 빌드

```bash
bash scripts/render-templates.sh   # 정본 → 플러그인 트리 렌더/복사 (P1)
```

## 설계 문서

- 아키텍처: `docs/plugin-family-design/02-moai-code.md`
- 구축 스펙: `docs/plugin-family-design/04-moai-code-processing.md`

## 라이선스

LicenseRef-MoAI-NC-ND-1.0
