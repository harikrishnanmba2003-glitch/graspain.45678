# Graspin — build instructions for Claude

You are building Graspin, an education platform of eight consoles that share one database.
A working prototype of every console exists in /reference/prototype. It is the visual and
behavioural source of truth. The Word build packs in /docs/build-packs are the written spec.

## Decisions are final
Volume 00 (Master Decision Record) and the section “Final decisions that apply to this volume” in every volume decide every choice that used to be open. Build exactly what they say. Release 1.1 items (Volume 00 Part 4) are not built in release 1.0.

## Before any work
1. Read this file fully.
2. Read the module spec in /docs/specs/ for the module you are building.
3. Open the prototype file named in the spec and read the named functions in full.
4. Open the matching screenshots in /reference/screens/.

## Fidelity rules (never break)
F1  /reference is read-only. Never edit it.
F2  Precedence: final decisions (Volume 00 and each volume’s “Final decisions” section) and DO-NOT-COPY notes > module spec > prototype behaviour > your judgement.
F3  Read the prototype function before building the screen.
F4  Copy every word exactly: labels, headings, errors, toasts, emails.
F5  Copy numbers, colours, spacing exactly. Use tokens from packages/ui only.
F6  Reproduce every role restriction in the UI and enforce it on the server.
F7  Business rules (BR-xxx) live once, in packages/core, with unit tests.
F8  Every sensitive action writes an audit entry in the same transaction.
F9  Nothing important lives only in the browser. Storage moves to the database.
F10 Never invent features, fields or copy. Put genuine doubts in docs/questions.md. Decisions are already made (Volume 00): never ask for them or reopen them.
F11 A screen is done only when its AC tests pass and screenshots match. Report both.
F12 Small steps: one prompt, one pull request, one written report.

## Stack (see ADR-0001)
TypeScript, Next.js (App Router), PostgreSQL + Prisma, Redis, WebSocket realtime,
S3-compatible storage, LiveKit for classes and calls, pnpm monorepo, Vitest, Playwright.

## Commands
pnpm install | pnpm dev --filter <app> | pnpm test | pnpm test:e2e | pnpm parity <module>
pnpm db:migrate | pnpm db:seed | pnpm lint | pnpm typecheck

## Conventions
Currency: Indian rupees, en-IN grouping, symbol ₹, whole rupees. Dates: IST, "6 Oct 2026".
IDs and password formats: see packages/core/ids.ts. Never change a format.
Use plain English in all user-facing text. No jargon, no emojis, no slang.
Product and feature names are global and conceptual. Do not introduce regional-language names.

## When you finish a task
Write docs/parity/<module>-<step>.md: what you built, which AC tests pass, screenshot diff
results, deviations, open questions. Then stop and wait for review.
