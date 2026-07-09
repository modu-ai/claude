---
name: design-tokens-transformer
description: |
  하나의 브랜드 토큰을 3계층(DTCG SSOT ↔ 원시 CSS 변수 ↔ semantic/shadcn 롤)으로 양방향 변환합니다.
  L1 DTCG(W3C `$value`/`$type`/`$description`)를 진실 원천으로 삼아 L2 CSS custom properties와 L3 Tailwind v4 `@theme` + `.dark` 전환 체계를 파생하고, 역방향(코드→DTCG)과 라운드트립 무결성 검사도 지원합니다.
  handoff 번들의 3계층 인코딩(02-tokens.json / colors_and_type.css / globals.css)을 자동 변환하는 파이프라인입니다.

  다음과 같은 요청 시 반드시 이 스킬을 사용하세요:
  - "DTCG 토큰을 CSS 변수로 변환"
  - "디자인 토큰 3계층 매핑"
  - "shadcn semantic 롤 생성"
  - "Tailwind v4 @theme 토큰 만들어 줘"
  - "CSS 변수에서 DTCG SSOT 역추출"
  - "토큰 라운드트립 무결성 검사"
user-invocable: true
version: 0.1.0
---

# design-tokens-transformer — 3계층 토큰 양방향 변환

## 개요

브랜드 토큰은 소비처마다 다른 형태를 요구합니다. 이 스킬은 **동일한 브랜드 진실(색·타이포·spacing·radius·shadow·motion)**을 3계층으로 인코딩·변환합니다. L1(DTCG)이 SSOT이고, L2/L3은 파생물이며, 역방향 추출과 라운드트립 검사로 계층 간 정합을 보장합니다.

> **본문 작성 대기 (다운스트림 도메인 태스크)**: 이 SKILL.md는 구조 + 변환 절차 스켈레톤입니다. 각 계층의 상세 스키마 예시·전체 변환 규칙표·엣지케이스 도메인 산문은 후속 태스크에서 채웁니다. 아래 `[본문 대기]` 표시가 있는 절이 그 대상입니다.

## 트리거 키워드

DTCG 토큰 변환, 3계층 토큰 매핑, CSS custom properties 생성, shadcn semantic 롤, Tailwind v4 @theme, 토큰 라운드트립, design tokens transformer

## 3계층 모델

| 계층 | 형태 | 소비처 | 대표 파일(handoff.zip) |
|---|---|---|---|
| **L1 — DTCG SSOT** | W3C Design Tokens (`$value`/`$type`/`$description`), 계층적 그룹 | 브랜드 진실 원천 | `assets/round3/02-tokens.json` |
| **L2 — 원시 CSS 변수** | `--color-*` · `--neutral-50..950` · `--tracking-*` + self-host `@font-face` | 단일 파일 HTML 렌더 / 카드 | `colors_and_type.css` |
| **L3 — semantic/shadcn** | `--base-background` · `--base-primary` · `--base-ring` · `--base-sidebar-*` · `--base-chart-1..5` + Tailwind v4 `@theme` + `.dark` 전환 | 프로덕션 코드(shadcn 체계) | `assets/round3/globals.css` |

### L1 — DTCG SSOT 스키마

- W3C 포맷: 각 토큰은 `$value` / `$type` / `$description` 보유
- 계층적 그룹: `color.{brand,neutral,semantic,dark,gradient}` · `typography.{family,weight,size,lineHeight,letterSpacing}` · `spacing` · `radius` · `shadow` · `motion.{duration,easing}` · `container` · `logo`
- `$description`은 출처·의미를 기록 → 브랜드 진실 원천

> [본문 대기] DTCG 그룹별 최소 토큰 세트 + `$type` 허용값 표 + 예시 JSON 블록.

### L2 — 원시 CSS 변수 스키마

- `--color-primary` / `--color-ink` / `--color-bg` / `--color-surface`
- `--neutral-50` … `--neutral-950` (휘도 스케일)
- `--tracking-display-tight` 등 자간 변수(한국어 자간 규칙 인코딩)
- self-host `@font-face` (Pretendard 등) + CDN 폰트

> [본문 대기] CSS 변수 네이밍 규칙 + `@font-face` 블록 템플릿 + 자간 변수 매핑표.

### L3 — semantic/shadcn 롤 스키마

- `--base-*` 의미 롤: `background`/`foreground`/`card`/`popover`/`surface`/`muted`/`primary`/`secondary`/`accent`/`destructive`/`border`/`input`/`ring`/`border-strong`/`chart-1..5`/`sidebar-*`
- Tailwind v4 `@theme` + `@layer base/utilities`
- `.dark` 클래스 → CSS 변수 전환으로만 다크모드 (`[HARD] dark:` Tailwind 유틸리티 직접 사용 금지)

> [본문 대기] `--base-*` → shadcn 컴포넌트 롤 매핑표 + `@theme` 블록 템플릿 + `.dark` override 규칙.

## 변환 절차 (스켈레톤)

### 정방향 — L1 → L2 → L3

1. **L1 로드·검증** — DTCG JSON 파싱, `$type`별 유효성 확인, 그룹 완결성 검사
2. **L1 → L2 파생** — brand/neutral/semantic 토큰을 `--color-*`/`--neutral-*`/`--tracking-*` CSS 변수로 평탄화, `@font-face`·CDN 폰트 블록 생성
   > [본문 대기] 그룹 경로 → CSS 변수명 변환 규칙 상세.
3. **L2 → L3 파생** — 원시 변수를 `--base-*` semantic 롤에 바인딩, `@theme` 등록, `.dark` override 세트 생성
   > [본문 대기] 원시 색 → semantic 롤 바인딩 결정 규칙 + chart/sidebar 파생.
4. **FROZEN 규칙 검증** — `#000000` 금지→`#09110f`, 단일 청록 그라디언트, 자간 규칙 등 각 계층 코멘트로 인코딩
   > [본문 대기] FROZEN 규칙 전체 목록 + 계층별 주입 위치.

### 역방향 — L3/L2 → L1

1. **소스 계층 식별** — 입력이 CSS(L2) / globals.css(L3) 중 어느 것인지 판별
2. **토큰 추출** — CSS 변수·`@theme` 선언에서 값·의미 역추출
3. **DTCG 재구성** — 추출값을 계층적 그룹으로 재조립, `$description`은 best-effort 유도(원 출처 불명 시 명시)
   > [본문 대기] CSS 변수명 → DTCG 그룹 경로 역매핑 규칙 + `$description` 유도 정책.

### 라운드트립 무결성 검사

- L1 → L2 → L3 → (역) → L1' 왕복 후 L1 ≟ L1' 비교
- 색: hex 정규화 후 동등성, 타이포: family/weight/size 보존, 자간: 값 손실 없음
- 불일치 발견 시 계층·토큰 단위로 diff 리포트
> [본문 대기] 정규화 규칙(hex 대소문자·shorthand·rgb 변환) + diff 리포트 포맷.

## 출력 형식

```
## 토큰 변환 완료 (L{src} → L{dst})

### 변환 요약
- 입력 계층: L{n} ([파일])
- 출력 계층: L{m}
- 변환 토큰: 색 N · 타이포 N · spacing N · radius N · shadow N · motion N

### 생성 파일
- [출력 경로]

### 라운드트립 검사
- 왕복 정합: PASS / N개 불일치
- (불일치 시) 계층·토큰 단위 diff

### FROZEN 규칙 검증
- [위반 없음 / 위반 목록]
```

## 사용 예시

> [본문 대기] 예시 1(DTCG→shadcn 정방향) · 예시 2(globals.css→DTCG 역추출) · 예시 3(라운드트립 검사) 상세 입출력.

## 주의사항

### Do

- L1(DTCG)을 항상 SSOT로 취급 — L2/L3은 파생물, 수동 편집 시 L1부터 갱신 후 재파생
- 다크모드는 `.dark` 클래스 CSS 변수 전환으로만 — Tailwind `dark:` 유틸리티 직접 사용 금지
- 자간(letter-spacing) 값을 손실 없이 전 계층 보존 — 한국어 타이포 품질의 핵심

### Don't

- L2/L3만 수정하고 L1을 방치 금지 — 다음 재파생에서 덮어써짐
- `#000000` 등 FROZEN 금지값을 변환 산출물에 통과 금지
- 역추출 시 불명확한 `$description`을 임의 창작 금지 — 유도 불가 시 "출처 미상" 명시

## 관련 스킬

| 스킬 | 사용 시점 |
|---|---|
| `moai-designer:cd-handoff-reader` | 선행: 번들에서 3계층 토큰 소스 추출 |
| `moai-designer:cd-system-prep` | 선행: 자산→DESIGN.md 합성(토큰 원천) |
| `moai-designer:design-system-library` | 보조: 75개 브랜드 토큰을 변환 입력으로 |
| `moai-designer:design-sync-upload` | 후속: 변환된 토큰을 Claude Design에 업로드 |
