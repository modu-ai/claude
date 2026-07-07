# Cowork v4.0.0 마이그레이션 가이드

v4.0.0에서 출판·크리에이티브 스킬(book-* 8종)이 `moai-story` 플러그인으로 이관되었습니다.

## 영향 받는 스킬

- `book-concept-planner`
- `book-target-reader`
- `book-outline-designer`
- `book-chapter-writer`
- `book-revision-coach`
- `book-author-bio`
- `book-proposal-writer`
- `book-publisher-matcher`

cowork 스킬 수: 179 → 171. Higgsfield MCP 연동도 moai-story로 이관되었습니다.

## 마이그레이션 절차

### 1. moai-story 설치

```
/plugin install story
```

### 2. Higgsfield 인증 (생성형 스킬 사용 시)

생성형 스킬(story-webtoon-art·story-conti·story-ad-conti·story-character-sheet·story-cover-art·story-previz)을 쓰려면 Higgsfield OAuth 1회 인증이 필요합니다. 절차는 [higgsfield-setup.md](./higgsfield-setup.md)를 참고하세요.

### 3. 기존 워크플로우

book-* 스킬은 moai-story 플러그인에서 동일한 이름·체인으로 그대로 동작합니다. 기존 호출 방식을 바꿀 필요가 없습니다.

## 롤백

v4.0.0 미만으로 롤백하려면:

```
claude plugin install modu-ai/claude@3.0.0
```
