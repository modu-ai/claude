---
name: story-webtoon-art
description: |
  웹툰 패널 작화 스킬 — Higgsfield AI Anime Generator와 Soul ID로 캐릭터 일관성을 유지하며 컷 이미지를 생성한다. 사전 크레딧 고지와 사용자 확인이 필수. MCP 미연결 시 프롬프트 온리 모드로 전환한다.

  다음과 같은 요청 시 반드시 이 스킬을 사용하세요:
  - "웹툰 작화", "웹툰 컷 이미지"
  - "캐릭터 일관성 작화", "Soul ID 웹툰"
  - "AI Anime Generator"
version: "5.0.0"
---

# story-webtoon-art

> 웹툰 회차 대본을 받아 컷 이미지를 생성하는 스킬. 캐릭터 일관성 유지가 핵심 과제이며, Soul ID로 인물 ID를 고정한 뒤 AI Anime Generator로 패널을 생성한다.

## 1. 개요

이 스킬은 **무엇을** 생성하는가 — 회차 대본의 컷 시퀀스 이미지. **언제** 실행하는가 — story-webtoon-episode의 대본이 완료된 뒤. Higgsfield MCP가 연결된 환경에서만 이미지 생성이 동작한다.

## 크레딧 고지 (사전 고지 의무)

이 작업은 **Higgsfield 크레딧을 소모**합니다. 생성 전 예상 소모량을 사용자에게 고지하고 확인을 받는다.

| 항목 | 예상 크레딧 |
|------|-----------|
| 웹툰 패널 1컷 (AI Anime Generator) | 약 2 크레딧 |

진행하기 전 사용자에게 "위 크레딧이 소모됩니다. 계속 진행할까요?"로 확인한다. 사용자가 거부하면 생성을 중단하고 프롬프트 온리 모드로 전환한다.

## 모델 라우팅 표

| 용도 | 1순위 Higgsfield 모델 |
|------|---------------------|
| 웹툰 패널 | AI Anime Generator (스타일·구도·캐릭터 ID) |
| 캐릭터 일관성 | Soul ID (인물 학습·포즈 보존) |
| 컷 분할 참조 | Popcorn (8프레임 시퀀스, story-conti와 공유) |

## MCP 미연결 폴백 (프롬프트 온리 모드)

Higgsfield MCP에 연결할 수 없을 때는 생성을 생략하고 완성 프롬프트를 텍스트로 출력한다. 출력 끝에 "Higgsfield 웹(https://higgsfield.ai)에 위 프롬프트를 붙여넣으세요" 안내를 추가한다. 서버 과부하 시 잠시 대기 후 재시도 안내를 함께 표시한다.

## 3. 워크플로우

### Step 1: 캐릭터 ID 확인
Soul ID에 주요 인물이 학습되어 있는지 확인. 없으면 story-character-sheet로 선행 학습.

### Step 2: 크레딧 고지 + 확인
생성할 컷 수 × 약 2 크레딧을 합산해 사용자에게 고지하고 승인을 받는다.

### Step 3: 컷별 프롬프트 조립
대본의 컷 정보를 AI Anime Generator 프롬프트로 변환 (스타일·화각·캐릭터 ID·동작).

### Step 4: 생성 + 검수
패널을 생성하고 일관성 위반(얼굴·의상·비율)을 검수. 위반 시 재생성 또는 Soul ID 재학습.

## 4. 주의사항

- 인물 일관성이 깨지면 독자 이탈로 이어진다. 매 컷 Soul ID를 적용한다.
- rate limit 미문서화 — 서버 과부하 시 대기 후 재시도.

## 5. 관련 스킬

- Before: `story-webtoon-episode` (대본) · `story-character-sheet` (인물 학습)
