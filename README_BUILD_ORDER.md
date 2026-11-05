# Graspin Complete Build Pack: start here

This zip holds everything the team needs to build Graspin in order: eleven Word volumes (Volume 0 to Volume 10), the Master Decision Record (Volume 00), the prompts as text files, the acceptance tests and business rules as CSV, the reference screens and the working prototype of every console.

**Every open decision has been decided.** Nothing waits for the product owner. Read `00_Start_Here/Volume00_Master_Decision_Record.docx` first. The same decisions are written, with exact build instructions and a few extra tests, in the section “Final decisions that apply to this volume” near the start of every volume.

## The build order

Build the folders in this order. A folder is finished when its tests pass and its parity report is written (Volume 0 Part 11).

| Step | Folder | Volume | Prompts | Tests | Rules | Screens |
|---|---|---|---|---|---|---|
| 01 | `01_Foundation` | Volume 0 | 9 | 21 | 19 | 0 |
| 02 | `02_Xora_Operations` | Volume 1 | 14 | 108 | 22 | 14 |
| 03 | `03_Business_Dashboard` | Volume 2 | 13 | 59 | 23 | 14 |
| 04 | `04_Quest_Studio` | Volume 3 | 13 | 53 | 17 | 20 |
| 05 | `05_Institute_Admin` | Volume 4 | 15 | 69 | 26 | 30 |
| 06 | `06_Academic_Head` | Volume 5 | 12 | 68 | 20 | 33 |
| 07 | `07_Coach_Portal` | Volume 6 | 13 | 120 | 34 | 86 |
| 08 | `08_Student_App` | Volume 7 | 13 | 100 | 39 | 81 |
| 09 | `09_Central_Library` | Volume 8 | 11 | 89 | 28 | 45 |
| 10 | `10_Messenger_and_Calls` | Volume 9 | 11 | 208 | 50 | 66 |
| 11 | `11_Release_QA_and_Go_live` | Volume 10 | 11 | 200 | 37 | 0 |

Totals: 135 prompts, 1095 acceptance tests (including the addendum tests numbered F01 and up), 315 business rules.

Folders 02 to 10 can be shared between people once Volume 0 is finished and Volume 1 has created institutes and users. Volume 9 (Messenger and Calls) may run in parallel with a separate person. Folder 11 is the last gate before go-live.

## What is inside each module folder

| Subfolder | What it holds |
|---|---|
| `1_Build_Pack` | The Word volume. Read it end to end before prompting. |
| `2_Prompts` | Every prompt of the volume as a text file, in order (P1.0, P1.1 …). Paste one at a time into the team’s Claude, in a fresh session. |
| `3_Acceptance_Tests` | `AC-…_tests.csv` (every test with empty status columns) and `…_business_rules.csv`. Use them as the progress tracker. |
| `4_Reference_Screens` | Screenshots of the prototype for this module. Read-only evidence. |
| `5_Prototype` | The working prototype HTML for this module. Open it in a browser. |

`12_Shared_Reference` holds the whole prototype suite (open `Graspin_Suite.html`) and the shared test logins.

## Set up the repository in five steps

1. Create an empty repository.
2. Run `python 00_Start_Here/make_repository_seed.py <path-to-repository>`. It copies CLAUDE.md, builds the read-only `/reference` folder (prototype, screens, data) and puts the Word volumes in `docs/build-packs` and the prompts in `docs/prompts`.
3. Start a fresh Claude session in the repository and paste prompt P0.1 from `01_Foundation/2_Prompts`.
4. For each module, in order: paste its prompts one at a time. After each prompt the assistant writes a report; a human checks the report against the tests in `3_Acceptance_Tests`.
5. When every module is finished, run Volume 10 (`11_Release_QA_and_Go_live`).

## Rules that never change

- The prototype is the reference for how a screen looks and behaves; the volumes say how to build it for production.
- Precedence: final decisions and DO NOT COPY notes, then the volume, then the prototype, then the assistant’s own judgement.
- Decisions are final. A later change goes through change control (Volume 0 Part 14).
- Release 1.1 items (Volume 00 Part 4) are not built in release 1.0.
- Product and feature names stay global and conceptual.

Xora AI Research Labs Private Limited, Chennai.
