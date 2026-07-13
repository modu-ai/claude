# 모두의 코워크 문서 사이트 — Changelog

## v4.0.0 (2026-07-07)

### Added

- **moai-story 플러그인 신설** — 작가·콘텐츠 비즈니스 도메인 전용 플러그인. 출판·웹툰·웹소설·시나리오·콘티·캐릭터·표지·프리비즈·IP 사업화 21개 스킬 + Higgsfield MCP 연동.
- [플러그인 카탈로그](./plugins/index.md)에 moai-story 섹션 추가.
- [cowork v4.0.0 마이그레이션 가이드](./plugins/migration.md) 신설.
- [Higgsfield MCP 설정 가이드](./plugins/higgsfield-setup.md) 신설.

### Changed

- cowork v3.0.0 → v4.0.0 (breaking): 출판(book-*) 스킬 8종이 moai-story로 이관. 스킬 수 179 → 171.
- 마켓플레이스 `metadata.version` 3.0.0 → 4.0.0 (catalog 단일 version 지점).

### Migration

기존 book-* 스킬 사용자는 `/plugin install story`로 moai-story를 설치하세요. 상세 절차는 마이그레이션 가이드를 참고.
