# MoAI Coworker — Changelog

## v5.0.0 (2026-07-08)

### Major

- **moai-story 플러그인 흡수 통합** — book-* 8스킬 + story-* 13스킬 + Higgsfield MCP가 moai-coworker로 통합. 단일 `modu-ai/claude` 마켓플레이스로 story 플러그인 폐지. 사용자 발화에서 [실무 동료]와 [글쓰기 작가] 두 역할 모자를 자동 감지해 상황에 맞게 교체.
- **3-point sync 5.0.0 복원** — `plugin.json` 5.0.0 = 전체 SKILL.md 5.0.0 = marketplace metadata.version (v4.0.0 불일치 해소). 3점 동기화 HARD 규칙 준수.
- **stale `moai-cowork` → `moai-coworker` rename (Phase 3 stale sweep)** — plugins 전체 233파일 / 1747라인 교체 (coworker 1507 + pm 53 + designer 13 + coder 2). skill 이름 보존 prefix 전용 교체, negative lookahead로 이미 올바른 `moai-coworker`는 미변경.
- **project 라우팅 moai-pm 허브로 이관** — `/project` 초기화는 moai-pm 허브 플러그인 담당 (4-plugin 라우터: coworker·designer·coder·pm).

### Migration

이전 릴리스에서 `/plugin install story`로 별도 설치했던 story 플러그인은 더 이상 불필요 — book-*·story-* 스킬이 moai-coworker에 통합됨. 동일한 스킬 이름·체인이 그대로 동작.

### Known Debt (후속 SPEC)

- `moai-pm` references/core (init-protocol·execution-protocol·diagnostic-protocol·quality-evaluator) + `templates/CLAUDE.md.tmpl`가 옛 27-plugin 구조를 전제 ("27 플러그인 / 173 스킬" 하드코딩 5곳, 스킬→플러그인 매핑 단일화). v5.0.0에서는 이름 rename만 수행 — **27→4 reference 재설계는 2026-07-09 플러그인 스킬 감사에서 완료** (init·diagnostic·evolution-protocol 4-plugin 재작성, stale 5곳 제거, SKILL_PLUGIN_MAP 재매핑).

### References

- 설계 정본: `docs/plugin-family-design/05-family-redesign-v2.md`
- 이전 릴리스: v4.0.0

---

## v4.0.0 (2026-07-07)

### Breaking Changes

- **출판(book-*) 스킬 8종이 moai-story 플러그인으로 이관**되었습니다.
  - 이관 스킬: `book-concept-planner`, `book-target-reader`, `book-outline-designer`, `book-chapter-writer`, `book-revision-coach`, `book-author-bio`, `book-proposal-writer`, `book-publisher-matcher`
  - 스킬 수: 179 → 171
- **Higgsfield MCP 연동이 moai-story 플러그인으로 이관**되었습니다 (생성형 스킬 사용자는 moai-story에서 재인증).

### Migration

book-* 스킬을 계속 사용하려면 moai-story 플러그인을 설치하세요:

```
/plugin install story
```

이후에도 동일한 스킬 이름·체인이 moai-story에서 동작합니다.

### Fixes

- 3점 동기화 HARD 규칙 준수: `plugin.json` 4.0.0 = 전체 171 스킬 SKILL.md 4.0.0 = marketplace `metadata.version` 4.0.0
- project 라우터(router.md·init-protocol.md)에서 book-* 라우팅을 moai-story 이관 안내로 갱신

### References

- 설계 정본: `docs/plugin-family-design/05-family-redesign-v2.md` §3 (SPEC-MOC-PLUGIN-STORY-001)
- 이전 릴리스: v3.0.0
