---
id: SPEC-MOC-PLUGIN-STORY-001
title: "moai-story 플러그인 신설 + 패밀리 v4 재배치"
version: "0.1.0"
status: in-progress
created: 2026-07-06
updated: 2026-07-06
author: GOOS
priority: P1
phase: "v4.0.0"
module: "plugins/moai-story"
lifecycle: spec-anchored
tags: "plugin,story,higgsfield,cowork,v4"
depends_on: ["SPEC-MOC-FAMILY-DRIFT-001"]
---

# Progress Tracking

## Phase Status

| Phase | Status | Started | Completed |
|-------|--------|---------|-----------|
| plan | ✅ completed | 2026-07-06 | 2026-07-06 |
| plan-audit | ⏳ pending | — | — |
| run | ⏸️ not started | — | — |
| sync | ⏸️ not started | — | — |

---

## Plan-Phase Summary

**Completed**: 2026-07-06
**Artifacts Created**: 4 (spec.md, plan.md, acceptance.md, design.md)

### Requirements (REQ-*) = 9
- REQ-STORY-001: moai-story 플러그인 구조
- REQ-STORY-002: 이관 스킬 8종 (cowork → story)
- REQ-STORY-003: 신규 스킬 13종 (story-*)
- REQ-STORY-004: Higgsfield MCP 연동
- REQ-STORY-005: 크레딧 고지 의무화
- REQ-STORY-006: cowork v4.0.0 마이그레이션
- REQ-STORY-007: marketplace.json 4엔트리 갱신
- REQ-STORY-008: www 문서 갱신
- REQ-STORY-009: 스킬 위생 기준 준수

### Acceptance Criteria (AC-*) = 11
- AC-STORY-001 ~ AC-STORY-011
- P0: 8 ACs
- P1: 3 ACs

### Milestones (M0-M6)
- M0: Pre-flight Verification
- M1: moai-story 스캐폴딩
- M2: 이관 스킬 8종 복사
- M3: 신규 스킬 13종 작성
- M4: cowork v4.0.0 마이그레이션
- M5: marketplace.json 갱신
- M6: www 문서 갱신

---

## Plan-Audit Pending

**Next Step**: Submit to plan-auditor for independent review before Implementation Kickoff.

**Expected Audit Criteria** (per plan-auditor MP-1/2/3/4):
- MP-1: Clarity — REQUIREMENTS 명확성, 모호성 없음
- MP-2: Completeness — 모든 필수 항목 포함, 누락 없음
- MP-3: Testability — AC가 검증 가능한 형태
- MP-4: Traceability — REQ→AC→Milestone 추적 가능

---

## Run-Phase Readiness

**Blocking Items**:
- [ ] DRIFT-001 `status: completed` 확인
- [ ] Plan-auditor PASS verdict

**Unblocked** → Run-phase 진입 (Implementation Kickoff AskUserQuestion)
