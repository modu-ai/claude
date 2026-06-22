---
title: "MoAI-Code (출시 예정)"
weight: 20
description: "Claude Code 전용 개발 도구 플러그인 — 코드 리뷰, 테스트 생성, API 문서 자동화 (2026 Q3 출시 예정)"
geekdocBreadcrumb: true
---

# MoAI-Code · 개발 도구 플러그인

{{< hint type="note" >}}
**2026 Q3 출시 예정** — 현재 내부 개발 중입니다. 출시 알림을 받으려면 [뉴스레터를 구독](https://claude.mo.ai.kr)하세요.
{{< /hint >}}

## 이런 분께 필요합니다

- Claude Code를 이미 사용하는 개발자
- 코드 리뷰·테스트 작성을 자동화하고 싶은 분
- API 문서·기술 문서를 빠르게 생성하고 싶은 분

## 준비 중인 기능

### 코드 품질

- **코드 리뷰** — PR 단위 자동 리뷰, 버그·보안 취약점 탐지
- **테스트 생성** — 단위·통합 테스트 자동 작성 (Go, Python, TypeScript 등)
- **리팩토링 제안** — 복잡도 분석 + 개선 코드 제안

### 문서화

- **API 문서** — OpenAPI spec → 사람이 읽기 좋은 문서 자동 생성
- **인라인 주석** — 함수·클래스 주석 자동 생성
- **아키텍처 다이어그램** — 코드베이스 구조 시각화

### DevOps

- **CI/CD 파이프라인** — GitHub Actions 워크플로우 자동 생성
- **DB 마이그레이션** — 스키마 변경 스크립트 초안 작성
- **환경 설정** — Docker, Compose, Terraform 구성 파일

## 현재 대안

Claude Code 자체 기능을 활용하세요:

```
/moai plan "기능 설명" → 개발 계획 수립
/moai run SPEC-ID       → 테스트 주도 구현
/moai sync SPEC-ID      → 문서 동기화
```

Claude Code 설치 및 사용법은 [Code 섹션](/code)을 참고하세요.

---

[← 플러그인 허브](/plugins)
