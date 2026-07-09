---
name: design-sync-upload
description: |
  디자인 시스템 자산(DESIGN.md·토큰·로고)을 Claude Design에 업로드합니다. 자동 우선 + 수동 폴백 양경로.
  자동 경로는 DesignSync MCP(`write_files`/`register_assets`/`finalize_plan`)로 바로 등록하며 `/design-login` 인증이 필요합니다. 인증이 없거나 MCP가 없으면 수동 폴백으로 `UPLOAD-GUIDE.md` + 스테이징 자산 폴더를 산출해 사용자가 직접 업로드합니다.

  다음과 같은 요청 시 반드시 이 스킬을 사용하세요:
  - "Claude Design에 디자인 시스템 업로드"
  - "DesignSync로 자산 등록"
  - "DESIGN.md 업로드해 줘"
  - "디자인 시스템 자동 동기화"
  - "업로드 가이드 만들어 줘 (수동)"
  - "claude.ai/design에 올릴 자료 스테이징"
user-invocable: true
version: 0.1.0
---

# design-sync-upload — Claude Design 업로드 (자동 + 수동 폴백)

## 개요

디자인 시스템 자산을 Claude Design에 올리는 방식은 환경에 따라 두 가지입니다. 이 스킬은 **자동(DesignSync MCP)을 먼저 시도**하고, 인증·가용성 조건이 안 되면 **수동 폴백(UPLOAD-GUIDE.md + 스테이징 폴더)**으로 자연스럽게 강등합니다. 어느 경로든 사용자가 손으로 파일을 흩뿌리지 않고 한 번에 업로드할 수 있게 만드는 것이 목표입니다.

> **본문 작성 대기 (다운스트림 도메인 태스크)**: 이 SKILL.md는 구조 + 인증 분기 + 폴백 절차 스켈레톤입니다. MCP 도구 호출 파라미터 상세·에러 코드 처리·스테이징 폴더 레이아웃 도메인 산문은 후속 태스크에서 채웁니다. `[본문 대기]` 표시 절이 그 대상입니다.

## 트리거 키워드

Claude Design 업로드, DesignSync MCP, design-login, 디자인 시스템 동기화, UPLOAD-GUIDE, 자산 스테이징, write_files, register_assets

## 입력

| 입력 | 형태 |
|---|---|
| DESIGN.md | `cd-system-prep` 산출물 |
| 토큰 | `design-tokens-transformer` 산출물(DTCG/CSS/shadcn) |
| 자산 | 로고 변형(가로/정사각/마스코트/WH), 폰트, 이미지 |

## 경로 선택 — 인증 감지 분기

```
자산 준비
  → [감지] DesignSync MCP 가용 AND /design-login 인증됨?
      ├─ YES → 자동 경로 (DesignSync MCP)
      └─ NO  → 수동 폴백 (UPLOAD-GUIDE.md + 스테이징 폴더)
```

> [본문 대기] 인증/가용성 감지 구체 신호(MCP 도구 존재 여부, 로그인 상태 확인 방법) + 감지 실패 시 기본 강등 정책.

## 자동 경로 — DesignSync MCP

`/design-login` 인증 상태에서 DesignSync MCP 도구로 자산을 직접 등록합니다.

1. **`write_files`** — DESIGN.md·토큰·부속 파일을 Design 프로젝트에 기록
2. **`register_assets`** — 로고·폰트·이미지 자산 등록(변형 매트릭스 매핑)
3. **`finalize_plan`** — 등록 세트를 확정하고 분석 대기 상태로 전환

> [본문 대기] 각 MCP 도구의 파라미터 스키마 + 순서 의존성 + 부분 실패 시 재시도/롤백 정책 + 에러 코드 → 폴백 전환 조건.

## 수동 폴백 — UPLOAD-GUIDE.md + 스테이징 폴더

MCP가 없거나 미인증이면 사용자가 직접 업로드할 수 있는 산출물을 만듭니다.

1. **스테이징 폴더 구성** — 기본 `./design-sync-staging/`에 DESIGN.md + 토큰 + 정리된 자산 사본 배치
2. **UPLOAD-GUIDE.md 생성** — 업로드 우선순위·주의사항·Published 토글 절차 기재
3. **사용자 안내** — 폴더 전체를 claude.ai/design에 업로드하도록 지시

```markdown
## Claude Design 업로드 가이드 (수동)

### 업로드 우선순위
1. DESIGN.md — 가장 먼저
2. 토큰 세트(DTCG/CSS/shadcn)
3. 로고 변형(SVG 우선)
4. 참고 자산

### 주의
- 모노레포 전체 X → 정리된 폴더만
- 민감 자산(고객 데이터·매출) 익명화 후 업로드
- 폰트 라이선스 확인

### Published 토글
1. 업로드 후 5-15분 대기(분석)
2. 테스트 프롬프트로 검증
3. 브랜드 일치 시 Published ON, 어긋나면 Remix
```

> [본문 대기] 스테이징 폴더 상세 레이아웃 + UPLOAD-GUIDE.md 완전 템플릿 + 자산 변형 매트릭스 매핑 규칙.

## 출력 형식

```
## Claude Design 업로드 [자동 / 수동]

### 경로
- 선택: 자동(DesignSync MCP) / 수동 폴백
- 사유: [인증 상태 / MCP 가용성]

### (자동) 등록 결과
- write_files: N개
- register_assets: N개
- finalize_plan: 확정 / 대기

### (수동) 산출물
- ./design-sync-staging/  (DESIGN.md + 토큰 + 자산 N개)
- ./design-sync-staging/UPLOAD-GUIDE.md

### 다음 단계
- (자동) 5-15분 분석 대기 → 테스트 프롬프트 → Published 토글
- (수동) 폴더 업로드 → 위 가이드 따라 진행
```

## 사용 예시

> [본문 대기] 예시 1(인증됨 → 자동 등록) · 예시 2(미인증 → 수동 스테이징) · 예시 3(자동 시작 후 에러 → 폴백 전환) 상세 입출력.

## 주의사항

### Do

- 자동을 먼저 시도하고, 조건 미달 시 조용히 수동으로 강등 — 사용자 작업 흐름을 끊지 않음
- 수동 폴백에서도 사용자가 손으로 파일을 흩뿌리지 않도록 폴더를 완결적으로 구성
- 민감 자산은 업로드 전 익명화 안내

### Don't

- `/design-login` 미인증 상태에서 자동 경로 강행 금지 — 즉시 수동 폴백
- 자동 부분 성공을 완료로 보고 금지 — `finalize_plan`까지 확정돼야 완료
- 폰트 라이선스 미확인 자산을 업로드 세트에 포함 금지

## 관련 스킬

| 스킬 | 사용 시점 |
|---|---|
| `moai-designer:cd-system-prep` | 선행: DESIGN.md 합성 |
| `moai-designer:design-tokens-transformer` | 선행: 업로드할 3계층 토큰 생성 |
| `moai-designer:moai-domain-design-handoff` | 대안: 핸드오프 패키지가 산출물일 때 |
| `moai-designer:cd-handoff-reader` | 역방향: Claude Design → Claude Code 인계 분석 |
