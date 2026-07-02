# SPEC-MOC-BOOTSTRAP-DESKTOP-001 — 진행 상황 (progress.md)

> 상태 스냅샷: plan-phase 산출물 작성 완료(draft). run-phase 미착수.

## §E.1 Plan-phase Audit-Ready Signal

plan-phase 산출물 세트(spec.md + plan.md + acceptance.md + progress.md) 작성 완료. 오디트 준비 신호:

- **SPEC ID self-check**: `decomposition: SPEC ✓ | MOC ✓ | BOOTSTRAP ✓ | DESKTOP ✓ | 001 ✓ → PASS` (정규 regex `^SPEC(-[A-Z][A-Z0-9]*)+-\d{3}$` 통과, 중복 없음).
- **Frontmatter 12-필드**: id/title/version/status/created/updated/author/priority/phase/module/lifecycle/tags 전부 존재. `created`/`updated` 사용(스네이크 별칭 없음). `tags` 콤마 구분 문자열. `version`·`phase`·`module`·`lifecycle` 비어있지 않음. status=draft(8-값 enum). priority=P1.
- **GEARS 준수**: REQ-BD-001~014 전부 GEARS 패턴(Ubiquitous / When / Where) 사용, 일반화된 `<subject>`.
- **Out of Scope**: 6개 `### Out of Scope — <topic>` H3 서브헤딩 + `-` 불릿(OutOfScopeRule 충족).
- **실측 기반**: 3개 트리(cowork/code/template) 직접 조사, 설계 문서 주장 미신뢰. 바이너리 의존 훅 전수 카운트는 추정 주장 없이 CODE-002로 이연(verification-claim-integrity 준수).
- **미결 결정**: D1(버전 정책), D2(표시명) — 옵션으로 인코딩, run-phase Implementation Kickoff 시 오케스트레이터 확인 필요.

## §E.2 Run-phase Evidence

> run-phase 시작: 2026-07-03. cycle_type=tdd (quality.yaml constitution.development_mode).
> Implementation Kickoff APPROVED (user, 2026-07-03). Phase 0.5 SKIPPED (plan-audit iter-3 PASS-WITH-DEBT 0.92, skip-eligible ≥0.90).
> Mode 5 (single sequential manager-develop). M5 SKIPPED (D2=KEEP). D1=BIND (0.1.0 → 3.0.0).

### M1 — `/project init` 순증 (AC-BD-001a/b/c) — PASS

- **AC-BD-001a (NET-NEW 게이트)**: `grep -c "skill-profile.yaml" SKILL.md` = **5** (HEAD was 0). 지정 경로 `.moai/skill-profile.yaml` 리터럴 매치 5건(Phase 6.6 directive + storage locations + EC6 주의사항).
- **AC-BD-001b (NET-NEW 게이트)**: `grep -ciE "폴더 규약 스캐폴드|folder-convention scaffold" SKILL.md` = **3** (HEAD was 0). Phase 6.5 directive + 현재 동작 요약 + storage locations.
- **AC-BD-001c (PRESERVE 회귀 가드)**: `grep -ciE "레거시 별칭|bare .?/project|/project init" SKILL.md` = **14** (baseline 14, 회귀 없음). `grep -c "^### 1\. CLAUDE\.md 구조" SKILL.md` = **1** (baseline 1).
- **공유 파일 경계 존중**: routing topology (`도메인 라우팅` section lines 65-95) + marketplace table (lines 419-425) 미수정 (REMEDIATION-001 AC-REM-016 소관).
- **편집 범위**: `plugins/moai-cowork/skills/project/SKILL.md` 내 4곳 — (1) 현재 동작 요약 +2 bullet, (2) Phase 6.5/6.6 워크플로 블록 추가, (3) 저장 위치 +2 라인, (4) moai-profile.md 금지 주의사항에 EC6 구분 노트.

### Audit SHOULD-FIX 처리 (run entry에서 문서화)

- **D2-defect (AC-BD-008 orphan grep)**: ADDRESS at run entry. `plugins/moai-code/commands/harness.md`는 §A.2에 문서화된 사전존재 예외(moai-code 전용 명령이라 정본 템플릿 기원 아님 → parity-source 주석 없음이 정상). 본 run-phase는 `plugins/moai-code/commands/*.md`를 일체 편집하지 않으므로 신규 orphan 0건 도입. 회귀 가드(마커 ≥ baseline + 신규 orphan=0) 유지.
- **D3-defect (AC-BD-004b ≥1 distinguishing literal per Tier row)**: DEBT로 이월 (non-blocking). 신규 AC 추가는 SPEC body 변경 → blocker → manager-spec 위임 필요 (run-phase 범위 외).



## §E.4 Sync-phase Audit-Ready Signal

_<pending sync-phase — manager-docs 소관>_

## §E.5 Mx-phase Audit-Ready Signal

_<pending Mx-phase — manager-docs 소관>_
