# 플러그인 카탈로그 (v4.0.0)

모두의클로드 마켓플레이스는 한국 실무 4종 빌드 플러그인 패밀리로 구성됩니다. v4.0.0에서 작가·콘텐츠 도메인 전용 `moai-story`가 신설되었습니다.

## moai-cowork

사업·이커머스·마케팅·콘텐츠·법률·재무·HR·교육·디자인·미디어 등 한국 실무 도메인의 171개 스킬을 하나로 묶은 통합 플러그인. v4.0.0에서 출판(book-*) 스킬 8종이 moai-story로 이관되었습니다. 자연어 요청으로 project 스킬이 워크플로우를 설계합니다.

## moai-design

Claude Design과 짝을 이루는 에이전틱 디자인 플러그인. 브리프 작성, 브랜드 컨텍스트 주입, DTCG 토큰 생성, GAN 품질 루프를 다룹니다.

## moai-code

moai CLI 바이너리 없이 Claude Code 안에서 SPEC plan → run → sync 개발 사이클을 그대로 쓸 수 있는 무설치 개발 방법론 플러그인.

## moai-story

작가와 콘텐츠 비즈니스를 위한 플러그인(v4.0.0 신설). 출판 기획·집필·퇴고부터 웹툰·웹소설·드라마/영화 시나리오·광고/영상 콘티·캐릭터 시트·표지·시네마틱 프리비즈·IP 피칭까지 21개 스킬. Higgsfield MCP 연동으로 캐릭터 일관성 작화·콘티·프리비즈를 생성합니다. story-project가 장르 파이프라인으로 라우팅합니다.

## 설치

```
claude plugin marketplace add modu-ai/claude
/plugin install story        # 작가·콘텐츠 (신규)
/plugin install cowork       # 한국 실무 올인원
```

기존 book-* 스킬 사용자는 `/plugin install story`로 마이그레이션하세요. 자세한 절차는 [migration.md](./migration.md)를 참고. 생성형 스킬은 [higgsfield-setup.md](./higgsfield-setup.md)의 OAuth 인증이 필요합니다.
