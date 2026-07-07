---
description: Claude agentic 코딩 가이드 — tool use, sub-agents, MCP 연동 자율 코딩 워크플로우
argument-hint: "[작업 설명]"
allowed-tools: Skill, Read, Grep, Glob, Agent
---

# /claude-agentic-coding

Agentic 코딩 워크플로우 진입. `claude-agentic-coding` 스킬 가이드에 따라 tool use + sub-agents + MCP를 조합해 자율 코딩.

`$ARGUMENTS`에 작업 설명을 받으면:
1. 작업 분해 (독립·의존 구분)
2. 조사·테스트·리뷰를 sub-agent로 위임 (`code-investigator` 등)
3. 병렬 수행 + 결과 취합
4. 구현·검증·보고

스킬: `plugins/moai-coder/skills/claude-agentic-coding/SKILL.md`
조사 에이전트: `plugins/moai-coder/agents/code-investigator.md`
