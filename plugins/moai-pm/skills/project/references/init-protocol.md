# init-protocol.md — `/project` 초기화 전체 플로우

## 개요

`/project`는 모두의클로드 프로젝트를 초기화하고, 사용자의 업무 워크플로우를 인터뷰한 뒤, **스킬 체이닝 + 프로젝트 전용 커스텀 에이전트 기반 CLAUDE.md**를 생성한다.

**현재 상태**:
- Phase 2 인벤토리는 설치된 플러그인을 **동적으로 도출**(plugin.json 스캔)하여 신규 플러그인을 자동 포함한다.
- Phase 4 Gap Detection: 체인 스킬 ↔ 인벤토리 대조 → 누락 감지 → 설치 안내 → Re-entry.
- `/project resume`로 설치 완료 후 저장된 진행 상태에서 재개한다(구 표기 호환).
- 글로벌 프로필 시스템은 사용하지 않는다(이름·회사·역할 재질문 없음).
- 생성 `CLAUDE.md`에 8개 HARD 규칙 블록이 고정 포함된다.

---

## 전체 플로우

```
/project
    ↓
Phase 1: 워크플로우 인터뷰 (맥락 충분까지 수집)
    ↓
Phase 2: Inventory — 설치된 플러그인·스킬 인벤토리 구성
    ↓
Phase 3: 스킬 체인 설계 (산출물별 파이프라인)
    ↓
Phase 4: Gap Detection — 누락 플러그인/스킬 감지 + 설치 안내
    ↓ (누락 0건이거나 옵션 2/3 선택 시)
Phase 5: 설계 확인 (AskUserQuestion)
    ↓
Phase 6: CLAUDE.md 생성 (CLAUDE.md.tmpl 기반, ≤200라인)
    ↓
Phase 7: 커스텀 에이전트 생성 (.claude/agents/*.md)
    ↓
Phase 8: API 키 / 커넥터 + 첫 실행 안내
```

---

## Phase 1: 워크플로우 인터뷰

사용자의 **이 프로젝트 맥락**만 수집한다. 이름·회사·역할 같은 **글로벌 프로필 정보는 묻지 않는다**.

### 1-1. 업무 유형

`AskUserQuestion`(1질문, 4옵션, multiSelect):

```
"이 프로젝트에서 어떤 일을 하시나요? (복수 선택 가능)"
☐ 사업 기획·전략 — 사업계획서, 시장조사, IR, 투자제안서
☐ 콘텐츠 제작 — 블로그, 카드뉴스, 뉴스레터, SNS, 카피
☐ 문서·행정 — PPT, 한글, Word, Excel, 공문, 계약서
☐ 제품·연구 — PM 문서, UX 리서치, 논문, 특허, 데이터 분석
+ Other
```

### 1-2. 주요 산출물

`AskUserQuestion`(1질문, 자유입력 + 예시 4개).

### 1-3. 톤·형식 제약 (선택)

`AskUserQuestion`(1질문, 4옵션): 공식·격식체 / 캐주얼·대화체 / 산업별 전문 용어 / 제약 없음.

수집 결과는 메모리에 임시 저장되며, Phase 6에서 `CLAUDE.md`에 직접 기록된다. 별도 `moai-profile.md`를 생성하지 않는다.

---

## Phase 2: Inventory — 활성 스킬 인벤토리 구성

### 2-1. 인벤토리 소스

**[HARD] 스캔 필터링 — moai-claude 출처만 인정 (동적 도출)**: `~/.claude/plugins/`에는 여러 마켓플레이스 플러그인이 섞여있을 수 있다. project 스킬은 **moai-claude(modu-ai/claude) 마켓플레이스 출처 플러그인만** 인벤토리에 포함하고, 그 외는 완전히 제외한다.

**[HARD] 플러그인 집합은 하드코딩 화이트리스트가 아니라 동적으로 도출한다.** `moai-*` 접두어이면서 moai-claude 마켓플레이스 출처인 플러그인을 `plugin.json` 스캔으로 식별한다. 마켓플레이스에 신규 플러그인이 추가되면 자동으로 포함된다. **카운트(플러그인 수·스킬 수)는 하드코딩하지 않는다** — `.claude-plugin/marketplace.json`이 로스터 정본이다.

**소스 A — Bash 디렉터리 스캔**:

```bash
PLUGIN_DIR=~/.claude/plugins
INSTALLED_MOAI_PLUGINS=()
for dir in "$PLUGIN_DIR"/moai-*; do
  p=$(basename "$dir")
  if [ -d "$dir" ] && [ -f "$dir/.claude-plugin/plugin.json" ]; then
    INSTALLED_MOAI_PLUGINS+=("$p")
  fi
done
for plugin in "${INSTALLED_MOAI_PLUGINS[@]}"; do
  find "$PLUGIN_DIR/$plugin/skills" -maxdepth 2 -name SKILL.md 2>/dev/null
done
```

각 SKILL.md frontmatter의 `name:` 필드를 추출해 `<skill-name> → <plugin>` 매핑을 구성한다.

**소스 B — system reminder 파싱**: 현재 세션 system reminder의 "user-invocable skills" 목록에서 moai-claude 출처 `moai-*` 스킬만 등록한다.

**교차 검증**: 두 소스가 일치하면 신뢰도 HIGH. 한쪽에만 있으면 MEDIUM(설치는 됐으나 세션 미반영 등).

### 2-2. `.moai/config.json` 인벤토리 스냅샷 스키마

```json
{
  "scanned_at": "2026-07-11T00:00:00+09:00",
  "plugins_installed": ["moai-pm", "moai-coworker", "..."],
  "skills_available": {
    "content-blog": "moai-coworker",
    "general-ai-slop-reviewer": "moai-coworker",
    "cd-brief": "moai-designer"
  },
  "confidence": { "moai-pm": "HIGH" }
}
```

### 2-3. Phase 1 답변 기반 매칭

| 업무 유형 | 우선 직원(플러그인) |
|----------|------------|
| 사업 기획·전략 | 코워커(business-* 스킬군) |
| 콘텐츠 제작 | 마케터(content-*, marketing-* 스킬군) |
| 문서·행정 | 사무관(office-*), 법무(legal-*) |
| 제품·연구 | 코워커(spec/ux 스킬군), 튜터(education-* 스킬군) |
| 이커머스 | 셀러(commerce-* 스킬군) |
| 출판·원고·웹툰·IP | 작가(book-*), 스토리(story-*) |
| 디자인 핸드오프·브랜드 | 디자이너(cd-*, moai-domain-design 스킬군) |
| 개발·SPEC·품질 게이트 | `/project --code`로 안내 |

라우터 허브는 project 스킬(`/project` 진입). 실무/콘텐츠/사무 도메인은 코워커로 수렴하며, 스토리는 `moai-story`, 출판은 `moai-writer`, 디자인은 `moai-designer`로 분기된다. `general-ai-slop-reviewer`·`general-humanize-korean`은 `moai-coworker` 소속으로 텍스트 후처리 체인에 항상 활용 가능하다.

---

## Phase 3: 스킬 체인 설계 (핵심)

### 3-1. 체인 구성 규칙

```
[기획/분석 스킬] → [생성 스킬] → [포맷 변환/미디어 스킬] → general-ai-slop-reviewer
```

텍스트 산출물 체인은 **반드시 `general-ai-slop-reviewer`로 종료**. 한국어 최종본은 직후 `general-humanize-korean` 2차 패스를 추가. 비텍스트는 ai-slop 단계 생략. Inventory에 없는 스킬은 체인에서 제외하거나 Gap Detection으로 넘긴다.

### 3-2. 체인 프리셋 테이블

상세 체인 프리셋(주요 산출물별 권장 체인)은 `cowork-setup.md` §3을 참조한다(단일 소스 — 중복 유지 안 함).

### 3-3. 체인 요약 포맷

Phase 5(확인 단계)에서 사용자에게 보여줄 요약:

```
이 프로젝트의 실행 체인 설계

[주 산출물 1] 사업계획서(PPT)
  체인: business-strategy-planner → office-pptx-designer → general-ai-slop-reviewer
  트리거 예시: "사업계획서 만들어줘"
```

---

## Phase 4: Gap Detection — 누락 플러그인/스킬 감지

### 4-1. 누락 감지 알고리즘

```
for each skill in chain_skills:
    if skill not in inventory.skills_available:
        missing_skills.append(skill)
        missing_plugin = SKILL_PLUGIN_MAP[skill]
        missing_plugins.add(missing_plugin)
```

### 4-2. 스킬 → 플러그인 매핑

스킬군 → 소속 플러그인 매핑은 **`.claude-plugin/marketplace.json` 로스터를 정본으로 삼는다** — 하드코딩 매핑 테이블을 유지하지 않는다(신규 플러그인 추가 시 자동 반영). 참고 패턴: `business-*`/`content-*`/`marketing-*`/`office-*`/`legal-*`/`finance-*`/`education-*`/`media-*`/`general-*` → `moai-coworker`; `commerce-*` → `moai-seller`; `book-*` → `moai-writer`; `story-*` → `moai-story`; `cd-*`/디자인 도메인 → `moai-designer`; 개발 도메인 스킬 → `moai`; `project`(PM 허브) → `moai-pm`.

### 4-3. 누락 발견 시 AskUserQuestion 4 옵션

```
"체인에 필요한 스킬이 설치되지 않은 플러그인에 포함돼 있습니다."

누락 스킬: [skill-A] → [moai-X] 플러그인 필요

옵션:
  1. (권장) 설치 안내 받기 + 설치 후 재개
     → 설치 명령을 안내하고, 완료 후 '/project resume'으로 재개합니다.
     → 현재 진행 상태(.moai/cache/init-progress.json)는 보존됩니다.
  2. 누락 스킬 제외하고 진행
  3. 대체 스킬로 변경
  4. 중단
```

### 4-4. 옵션 1 선택 시: 설치 안내 흐름

```
1. 누락 플러그인별 설치 명령 안내:
   /plugin install moai-coworker@moai-claude   (또는 해당 플러그인)
   (최초 1회 마켓 등록: /plugin marketplace add modu-ai/claude)

2. .moai/cache/init-progress.json 저장

3. 안내: "'/project resume' 입력 또는 '이어서 진행', '설치 완료' 발화"
```

`.moai/cache/` 디렉터리가 없으면 `Bash("mkdir -p .moai/cache")`로 생성한다.

### 4-5. `init-progress.json` 스키마

```json
{
  "started_at": "2026-07-11T14:30:00+09:00",
  "phase_completed": 3,
  "interview_answers": { "work_type": ["사업 기획·전략"] },
  "chain_design": [
    { "deliverable": "사업계획서(PPT)", "chain": ["business-strategy-planner", "office-pptx-designer", "general-ai-slop-reviewer"] }
  ],
  "missing_skills": [],
  "missing_plugins": []
}
```

### 4-6. 옵션 2/3 선택 시

옵션 2(제외): `missing_skills`에 해당하는 체인 단계를 제거하고 Phase 5로 진행하며, `CLAUDE.md`의 해당 체인에 미설치 주석을 삽입한다. 옵션 3(대체): `inventory.skills_available`에서 유사 기능 스킬을 검색해 재설계 후 Phase 5로 진행한다.

### 4-7. 누락 0건이면

즉시 Phase 5 Confirm으로 진행한다.

---

## Phase 5: 설계 확인

`AskUserQuestion`(1질문, 3옵션): 승인(권장) / 수정 / 취소.

---

## Phase 6: CLAUDE.md 생성

`references/templates/CLAUDE.md.tmpl`을 로드하여 변수를 치환한다. 상세 변수 치환 테이블·생성 절차는 `claudemd-generator.md` 참조. 생성 원칙: ≤200라인, 스킬 체인 최대 10개, 8개 HARD 규칙 블록 항상 포함, UTF-8/LF/한국어.

---

## Phase 7: 커스텀 에이전트 생성

Phase 3-6 결과를 바탕으로 `.claude/agents/*.md`를 생성한다. 절차·frontmatter·7-step 루프는 project 스킬 SKILL.md §Custom Agent & Skill-Chain Design 참조.

---

## Phase 8: API 키 / 커넥터 + 첫 실행 안내

Phase 2에서 선택된 플러그인이 API 키를 요구하면 등록 안내.

| # | 서비스 | 환경변수 | 용도 | 발급처 |
|---|--------|---------|------|--------|
| 1 | 공공데이터포털 | `DATA_GO_KR_API_KEY` | 공공데이터/KOSIS/KCI | data.go.kr |
| 2 | KIPRIS Plus | `KIPRIS_API_KEY` | 특허 검색 | plus.kipris.or.kr |
| 3 | 국가법령정보 | `KOREAN_LAW_OC` | 법령/판례 | law.go.kr |
| 4 | Google Gemini | `GEMINI_API_KEY` | 이미지 프롬프트 | ai.google.dev |
| 5 | Higgsfield | `HIGGSFIELD_API_KEY` + `HIGGSFIELD_SECRET` | Higgsfield MCP | higgsfield.ai |
| 6 | ElevenLabs | `ELEVENLABS_API_KEY` | media-audio-gen(TTS) | elevenlabs.io |

저장 위치: `./.moai/credentials.env`(프로젝트 격리, GUIDANCE 전용 — 실제 값은 절대 기록하지 않음).

첫 실행 안내는 Phase 3에서 설계된 체인 중 상위 3개를 예시로 제시한다. 전체 목록: `/project catalog`. 현재 상태: `/project status`.

---

## Re-entry: 설치 완료 후 진행 재개

| 트리거 | 처리 |
|--------|------|
| `/project resume` | 명시적 재개 커맨드 |
| `/project resume` | 레거시 별칭 — 계속 인식(비파괴) |
| "이어서 진행" / "설치 완료" / "다시 진행" | 자연어 → resume 흐름 자동 트리거 |

### 복원 흐름

1. `.moai/cache/init-progress.json` 존재 확인(없으면 "저장된 진행 상태가 없습니다. `/project`로 새로 시작하세요.")
2. `init-progress.json` 로드(Phase 1-3 결과 복원)
3. Phase 2 Inventory 재실행(설치 확인)
4. Phase 4 Gap Detection 재검증(여전히 누락 시 4옵션 재제시, 0건이면 Phase 5로 진행)
5. Phase 5 이후는 정상 흐름과 동일

---

## `/project apikey` — API 키 관리

```
/project apikey
```

6개 API 키를 조회/변경/추가/삭제한다.

---

## AskUserQuestion 제약 준수 요약

| Phase | 질문 수 | 옵션 수 |
|-------|---------|---------|
| Phase 1-1 업무 유형 | 1 | 4(multiSelect) |
| Phase 1-2 산출물 | 1 | 자유입력 |
| Phase 1-3 톤·제약 | 1 | 4 |
| Phase 4 Gap Detection(조건부) | 1 | 4 |
| Phase 5 설계 확인 | 1 | 3 |
| Phase 8 API 키(조건부) | 1-2 | 최대 4(multiSelect) |
| **합계** | **최대 6회** | 모두 ≤4 |
