# MoAI Cowork — Changelog

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
