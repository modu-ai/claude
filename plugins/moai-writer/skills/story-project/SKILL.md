---
name: story-project
description: |
  작품 유형을 파악해 출판·웹툰·웹소설·시나리오·콘티·광고 콘티·캐릭터·표지·프리비즈·IP 사업화 파이프라인으로 라우팅하는 진입점 스킬. 사용자의 한마디 요청에서 장르를 분류해 알맞은 story-* 스킬로 안내한다. moai-coworker 플러그인의 /project 역할 담당.

  다음과 같은 요청 시 반드시 이 스킬을 사용하세요:
  - "소설 쓰고 싶어", "웹툰 기획할래", "시나리오 작성"
  - "콘티 만들어줘", "광고 스토리보드"
  - "캐릭터 시트", "책 표지 일러스트"
  - "프리비즈", "IP 피칭 문서"
version: "0.1.0"
---

# story-project

> moai-coworker 플러그인의 진입점. 사용자의 작품 의도를 분류해 알맞은 장르 파이프라인으로 라우팅한다. 어떤 스킬을 언제 호출할지 결정하는 라우터 역할을 수행한다.

## 1. 개요

사용자가 "작품을 만들고 싶다"고 할 때 가장 먼저 묻는 것은 **무엇을 만들 것인가**이다. 이 스킬은 그 질문에 답한 뒤 알맞은 story-* 스킬로 안내한다. 슬래시 명령 없이 자연어 요청만으로 라우팅이 동작한다.

## 2. 라우팅 로직

사용자 입력을 분류해 다음 파이프라인으로 안내한다.

| 입력 의도 | 진입 스킬 | 후속 체인 |
|-----------|-----------|----------|
| 출판 도서 | `book-concept-planner` | target-reader → outline-designer → chapter-writer → revision-coach |
| 웹툰 기획 | `story-webtoon-planner` | webtoon-episode → webtoon-art |
| 웹소설 연재 | `story-webnovel-writer` | (단일 스킬 순환) |
| 드라마/영화 시놉 | `story-synopsis` | screenplay |
| 정식 시나리오 | `story-screenplay` | (단일) |
| 콘티·스토리보드 | `story-conti` | (Higgsfield 생성) |
| 광고 콘티 | `story-ad-conti` | (Higgsfield 생성) |
| 캐릭터 시트 | `story-character-sheet` | (Higgsfield 생성) |
| 표지·일러스트 | `story-cover-art` | (Higgsfield 생성) |
| 시네마틱 프리비즈 | `story-previz` | (Higgsfield 생성) |
| IP 사업화·판권 | `story-ip-pitch` | (단일) |

## 3. 워크플로우

### Step 1: 의도 분류
사용자 요청에서 장르 신호 키워드를 추출한다.

### Step 2: 확인
"선택하신 영역은 X입니다. Y 스킬로 진행합니다."로 의도를 확인한다.

### Step 3: 라우팅
알맞은 story-* 스킬을 호출한다.

## 4. 주의사항

- Higgsfield 생성이 필요한 스킬(conti·ad-conti·character-sheet·cover-art·previz·webtoon-art)은 사전 크레딧 고지가 선행된다.
- 한 요청에 두 영역이 섞이면 우선순위를 묻고 한쪽씩 진행한다.

## 5. 관련 스킬

- 전체 story-*·book-* 스킬 (위 라우팅 표 참조)
