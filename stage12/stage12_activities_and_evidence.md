# Stage 12 activities and evidence

BLANK student response template. Supplied from the beginning in stage12/ in your EXISTING repository; complete it only when you reach Stage 12 after the previous applicable stage is integrated, verified and recorded; preserve project/, tests, earlier records and Git history. UG/common and PG/extended scope must be explicit. Use concise results and versioned links, not copied logs or source. No staff answers or fabricated approvals.

Group/tutorial: Grp 2 tutorial Wed 4:30 - 6:30
Members and UG/PG applicability: Undergraduate, RachelUC, Merlin3313611, TarnimaKhan22, u3325845 (Novera)


## A Release scope and starting SHA

Release label/version and requirements baseline: SmartCare Assignment 3 – Stage 12 Final Release Candidate (Undergraduate). The release covers FR-01–FR-09, QRY-01–QRY-04, FP-01–FP-03 and UI-01–UI-02, based on the Assignment 3 Overview/revision 2 requirements baseline. FR-10 is retired and excluded from the release. The application uses session-only storage without a persistent database.
Common starting SHA / branch / applicable members:  The Stage 12 common starting point is commit c871297 on main, following the merge of Stage 9 PR #45 and PR #46. The applicable undergraduate members are Merlin, Rachel, Tarnima and Novera. The integrated application was verified locally on 9 November 2026 using python -m pytest -q from project/, with 157 tests passed in 0.33s.
PG starting SHA / branch / applicable members or not applicable: not applicable
Working-state review and approved integration: The completed Stage 9 implementation was merged into main through PR #46 after the Stage 9 Section H documentation was merged through PR #45. The integrated application includes patient and practitioner registration and lookup, appointment booking, cancellation and retained history, practitioner appointment listing, pure query functions and the interactive console. The local stage12/release-evidence branch was fast-forwarded to c871297 without conflicts. Full regression testing from project/ using python -m pytest -q passed all 157 tests in 0.33s on 9 November 2026.
Protected common candidate and PG differences: Our group follows the undergraduate pathway, so PG-only Stages 10 and 11 are not applicable. The verified Stage 9 common candidate is commit c871297 on main, with 157 tests passing. Stage 12 documentation is being prepared on separate branches, including stage12/release-evidence, to protect the integrated application. Final Stage 12 changes will be reviewed and integrated before the release SHA is recorded.
Feature freeze / owner / verifier: The undergraduate SmartCare implementation has reached the Stage 9 integrated baseline at commit c871297, with all 157 automated tests passing. No additional features are planned for the Stage 12 release; only verified release-blocking defects should be corrected. Merlin is responsible for release scope and Git integration evidence (Sections A, B and I), while Rachel is responsible for regression testing evidence (Section C). Final release approval remains pending completion of the Stage 12 review, documentation checks and team verification.


## B Requirements and release readiness matrix

Tutorial activity 1: All tests pass, README setup is incomplete, one dependency is unreviewed and a known limitation is undocumented. Decide Release / Release with conditions / Do not release and justify:
- Decision: Do not release yet .

In the tutorial scenario, SmartCare has passing tests, but the README setup instructions are incomplete, one dependency is unreviewed and a known limitation is undocumented. Passing tests alone is not enough for release approval. The team must complete the README, review the dependency, document the limitation and verify the application from a fresh copy before approving release.

Tutorial activity 2 and actual readiness matrix. Add exact requirement/acceptance IDs, evidence and reviewer; distinguish common/PG applicability.

| Release claim / requirement / scope | Evidence | Location/link and SHA | Reviewer | Sufficient? | Gap/action |
|---|---|---|---|---|---|
| FR-06-FR-08 - Cancellation and retained history (tutorial release claim) | Cancellation service, retained appointment history and regression tests; integrated suite passed 157 tests in 0.33s | `project/smartcare/services.py`, `project/tests/test_services.py`; Stage 8 PR #26; SHA `c871297` | Rachel | Yes for automated regression; final review pending | Confirm final cancellation/history review |
| Architecture responsibilities are appropriate - common | Domain, data store, services, queries and console have separated responsibilities | `project/smartcare/`; Stage 9 integration; SHA `c871297` | Merlin | Pending final review | Confirm architecture responsibilities and dependencies |
| PG RES - Rescheduling safety | Not applicable (UG pathway) | Not applicable | Not applicable | N/A | None |
| Responsible AI - common recheck / PG assurance | Stage 6 records confirm human-first review and Copilot comparison. Stage 8 records confirm human hypotheses, evaluation of Copilot suggestions, independent review and regression testing. Stage 9 Sections B, E and H record human design, Copilot critique, independent PR review and integration. | Stage 6, Stage 8 and Stage 9 evidence documents; Stage 9 PR #44; baseline SHA `c871297` | Rachel | Yes for previous-stage evidence; Stage 12 review pending | Complete final Stage 12 responsible-AI and code-quality review in Section E. PG assurance not applicable |
| Maintainability - common | Separated modules, automated tests and updated application README; 157 tests passed | `project/README.md`, `project/smartcare/`, `project/tests/`; SHA `c871297` | Rachel | Pending final checks | Confirm code quality review and fresh-copy setup |
| FR-01-FR-03 - Registration, lookup and validation | Patient and practitioner registration, lookup and validation covered by integrated tests | `project/smartcare/services.py`, `project/tests/test_patient_lookup.py`, `project/tests/test_practitioner_lookup.py`; SHA `c871297` | Rachel | Yes for automated regression | Confirm final requirement-level review |
| FR-04-FR-05 - Booking and conflict rules | Booking and conflict behaviour covered by integrated regression suite | `project/smartcare/services.py`, `project/tests/test_services.py`, `project/tests/test_workflows.py`; SHA `c871297` | Merlin | Yes for automated regression | Confirm booking/conflict acceptance criteria |
| FR-06-FR-08 - Cancellation, history and lookup | Cancellation retains appointment history and lookup functionality; regression suite passed | `project/smartcare/services.py`, `project/tests/test_services.py`; Stage 8 PR #26; SHA `c871297` | Rachel | Yes for automated regression | Confirm cancellation and lookup acceptance criteria |
| FR-09, QRY-01-QRY-04, FP-01-FP-03 - Listing and pure queries | Practitioner appointment listing and pure query functions, including 12 Stage 9 query tests | `project/smartcare/queries.py`, `project/smartcare/services.py`, `project/tests/test_queries.py`; PR #38; SHA `c871297` | Merlin | Yes for automated regression | Confirm listing, filtering, ordering and purity requirements |
| UI-01-UI-02 - Console workflow and error recovery | Interactive console workflows and invalid-input recovery covered by Stage 9 tests; 157 tests passed overall | `project/smartcare/console.py`, `project/main.py`, `project/tests/test_workflows.py`, `project/tests/test_console_validation.py`; SHA `c871297` | Tarnima | Automated tests passed; demo pending | Confirm final console demonstration and error recovery |
| FR-10 - Retired persistence requirement / session-only scope | In-memory data store; persistence excluded under requirements revision 2 | `project/smartcare/data_store.py`, `project/README.md`; SHA `c871297` | Merlin | Pending documentation confirmation | Confirm session-only limitation is clearly documented |
| PG RES and assurance integration | Not applicable (UG pathway) | Not applicable | Not applicable | N/A | None |

## C Full regression results

| Suite/scope | Environment/version | Working directory and command | Tested SHA | Actual result | Evidence link |
|---|---|---|---|---|---|
| Complete common | [response] | [response] | [response] | [response] | [response] |
| Complete PG if applicable | [response] | [response] | [response] | [response] | [response] |
| Affected focused checks after correction | [response] | [response] | [response] | [response] | [response] |
| Full integrated recheck | [response] | [response] | [response] | [response] | [response] |
Prior assertions preserved / reviewed test diff: [response]
Remaining failure / limitation: [response]


## D Console and end to end demonstration

| Demo step | Synthetic setup/input | Expected requirement | Observed result | Evidence/link |
|---|---|---|---|---|
| Problem and stakeholders | SmartCare appointment management for patients, practitioners and administrative users | Support registration, lookup, booking, cancellation and appointment history | Interactive menu displayed options 0–8 for the supported common-scope operations | `project/smartcare/console.py` |
| Register and find Patient and two Practitioners | Patient P001; practitioners DR001 and DR002, using fictional test labels | FR-01–03: register and retrieve records | P001, DR001 and DR002 registered successfully in the first session. Patient P001 and practitioner DR001 were retrieved successfully | Manual console demonstration; `project/smartcare/console.py` |
| Valid booking | A001: P001 with DR001, 2026-11-20 10:00 | FR-04–05: create a valid scheduled appointment | A001 booked successfully with status `scheduled` | Manual console demonstration |
| Same practitioner exact-time conflict rejected | A002: P001 with DR001, 2026-11-20 10:00 | Reject conflicting scheduled appointments for the same practitioner | Booking rejected with "Practitioner already has a SCHEDULED appointment at this time"; menu remained available | Manual console demonstration |
| Different practitioner same time allowed | A003: P001 with DR002, 2026-11-20 10:00 | Allow appointments with different practitioners at the same time | A003 booked successfully in the first session | Manual console demonstration |
| Cancel SCHEDULED and retain/find CANCELLED object | Cancel A001, then find A001 | FR-06–08: cancellation changes status while retaining appointment history | A001 changed to `cancelled` and was retrieved afterward with the same appointment ID, patient, practitioner and time | Manual console demonstration |
| Invalid/repeated cancellation rejected | Attempt to cancel A001 again | Reject cancellation when the appointment is no longer scheduled | Console returned "Only SCHEDULED appointments may be cancelled" and continued operating | Manual console demonstration |
| Default all-status listing | DR001 with blank status filter | FR-09: list practitioner appointments without excluding cancelled history | Cancelled A001 appeared in the default listing in the first session | Manual console demonstration |
| Explicit filtering / empty vs unknown / deterministic order | DR001 with `cancelled`; DR002 with `scheduled`; registered DR001 with no appointments; unknown DR999; bookings entered at 10:00, 11:00 and 09:00 | FR-09 and QRY/FP: filtering, empty results, unknown practitioner handling and deterministic ordering | Cancelled and scheduled filters returned matching appointments. Empty registered-practitioner listing displayed "No matching appointments found"; DR999 returned "Practitioner not found". Unfiltered appointments appeared in chronological order: 09:00, 10:00, 11:00 | Two manual console demonstrations |
| Invalid date/status/menu/lookup recovery and continued operation | 2026-02-30 10:00; `invalid-date`; status `invalid`; unknown appointment A999; menu option 9 and blank input | Reject invalid input without terminating the console | Invalid calendar date, date format, status, lookup and menu selections produced error messages. The console returned to the menu after each | Two manual console demonstrations |
| Session-only limitation and normal exit | Menu option 0 | Exit normally and disclose that records are not persisted | Console displayed "Goodbye! Session data will not be saved." and "Session-only data: records are lost on exit." | Two manual console demonstrations |
| One meaningful requirement-linked pytest test explained | `test_appointment_cancellation_and_history` uses synthetic patient P1, practitioner DR1 and appointment A1 | FR-06–08: cancellation must retain appointment history and allow later lookup | The test simulates registration, booking, cancellation and lookup using mocked console inputs. Assertions check that A1 is reported as cancelled, remains retrievable with its original details and that the console exits normally. This verifies the observable cancellation-history workflow, but not object identity directly. | `project/tests/test_workflows.py`, lines 69–90 |
| Architecture and one actual AI decision / known limitation | Shared SmartCareDataStore, existing services, pure query functions and console | Keep responsibilities separate and verify AI suggestions against requirements | The console handles input/output and errors, services enforce business rules, and pure queries filter and sort appointments. GitHub Copilot suggested additional menu framework classes and persistent storage, but these were rejected as unnecessary for the session-only scope. Code inspection and the earlier 141-test regression supported the simpler design. The known limitation is that records are lost when the console exits. | `project/smartcare/console.py`; `project/smartcare/services.py`; `project/smartcare/queries.py`; `stage09/stage09_activities_and_evidence.md`, Section E |
| PG reschedule identity/participants/time and no-op | Not demonstrated | PG-only requirement | Not verified in this common-scope demonstration; applicability to be confirmed | Pending scope confirmation |
| PG conflict/invalid status/failure non-mutation | Not demonstrated | PG-only requirement | Not verified in this common-scope demonstration; applicability to be confirmed | Pending scope confirmation |
| PG old slot / current lookup/list ordering / assurance risks | Not demonstrated | PG-only requirement | Not verified in this common-scope demonstration; applicability to be confirmed | Pending scope confirmation |

Stable demo owner / fresh process / command: To be confirmed by the team. From the `project` directory, run `python main.py --interactive`. Both manual demonstrations used a fresh process and synthetic data. The second session also confirmed that cancelling A001 freed the 10:00 slot for A004 while retaining the cancelled record.

PG demonstrations through service/tests or not applicable: To be confirmed based on the group's UG/PG applicability and final integrated candidate.


## E Final code quality and AI review

| Review area | Code/evidence location | Finding or no finding | Correction/no change and recheck |
|---|---|---|---|
| OOP responsibilities and pure-query boundaries | [response] | [response] | [response] |
| PascalCase and snake_case naming | [response] | [response] | [response] |
| Useful type hints and meaningful docstrings | [response] | [response] | [response] |
| Four-space indentation and imports/layout | [response] | [response] | [response] |
| Focused methods / duplication / dead or commented code | [response] | [response] | [response] |
| Globals / leakage / unnecessary inheritance or frameworks | [response] | [response] | [response] |
| No SQLite/persistence/repository ABCs/speculative features | [response] | [response] | [response] |
| Synthetic data / secrets / dependencies / provenance | [response] | [response] | [response] |
| Significant common Copilot contributions and human verification | [response] | [response] | [response] |
| PG plan/diff/test approvals and Stage 11 VERIFY/TRUST | [response] | [response] | [response] |

| AI claim | Affected requirement/code | Human check | Accept/Modify/Reject and reason | Actual outcome/action or no change |
|---|---|---|---|---|
| [response] | [response] | [response] | [response] | [response] |
Access route or approved equivalent / limitations: [response]
Available AI evidence and missing evidence honestly disclosed: [response]


## F README and reproducibility check

| README item | Location | Verifier | Result/gap |
|---|---|---|---|
| Purpose and included common/PG scope | [response] | [response] | [response] |
| Out-of-scope capabilities and known limitations | [response] | [response] | [response] |
| Confirmed teaching Python version and dependency installation | [response] | [response] | [response] |
| Working directory / demo / interactive / test commands | [response] | [response] | [response] |
| Repository structure and architecture responsibilities | [response] | [response] | [response] |
| Responsible AI summary / synthetic-data rule | [response] | [response] | [response] |
| Release label/version and SHA links | [response] | [response] | [response] |
Root README index and project/README verified: [response]
Fresh clone or extracted ZIP / candidate identity: [response]
Verifier and clean environment / actual version: [response]
Setup/run/test commands and observed results: [response]
Missing local file or setup gap / remedy and recheck: [response]


## G Known limitations debt and release notes

Delivered features: [response]
Important fixes: [response]
Architecture/quality improvements: [response]
Known limitations: [response]
AI-assisted development note: [response]

| Debt item | Impact | Priority | Future action | Accepted? / release rationale |
|---|---|---|---|---|
| [response] | [response] | [response] | [response] | [response] |
Session-only synthetic data and minute-precision local time: [response]
Production auth/roles, portal, notifications, billing/insurance, clinical AI exclusions: [response]
Scale/concurrency, timezone policy, operations/monitoring, accessibility/usability limitations: [response]
Difference between accepted scope limit and unresolved required behaviour: [response]
PG assurance residual risks / owner / status or not applicable: [response]


## H Release findings and corrective action

| Requirement/claim | Reproduction/observation | Impact/severity | Owner/action | Corrective diff | Focused/full recheck | Residual limit |
|---|---|---|---|---|---|---|
| [response] | [response] | [response] | [response] | [response] | [response] | [response] |
Justified no-change conclusion if no defect found: [response]
Release blockers still open / status: [response]


## I Git review and integration evidence

Issue / PR / diff links and reviewed SHA: SmartCare development was managed through GitHub issues, feature branches and pull requests across Stages 6–9.

- Stage 6: [PR #3 – Patient lookup (Rachel)](https://github.com/u3325845/st1-assignment-3/pull/3), [PR #4 – Patient lookup evidence (Rachel)](https://github.com/u3325845/st1-assignment-3/pull/4), [PR #5 – Practitioner lookup (Merlin)](https://github.com/u3325845/st1-assignment-3/pull/5), [PR #8 – Validation tests (Tarnima)](https://github.com/u3325845/st1-assignment-3/pull/8), [PR #9 – Patient lookup evidence (Rachel)](https://github.com/u3325845/st1-assignment-3/pull/9), [PR #10 – Practitioner lookup evidence (Merlin)](https://github.com/u3325845/st1-assignment-3/pull/10), and [PR #14 – Cancellation service (Novera)](https://github.com/u3325845/st1-assignment-3/pull/14).

- Stage 7: [PR #15 – Appointment validation (Tarnima)](https://github.com/u3325845/st1-assignment-3/pull/15), [PR #16 – Patient domain tests (Rachel)](https://github.com/u3325845/st1-assignment-3/pull/16), [PR #18 – Appointment construction (Tarnima)](https://github.com/u3325845/st1-assignment-3/pull/18), [PR #20 – Practitioner tests (Merlin)](https://github.com/u3325845/st1-assignment-3/pull/20), [PR #22 – Cancellation history tests (Novera)](https://github.com/u3325845/st1-assignment-3/pull/22), and [PR #23 – Domain test updates (Rachel)](https://github.com/u3325845/st1-assignment-3/pull/23).

- Stage 8: [PR #26 – Cancelled appointment lookup repair (Novera)](https://github.com/u3325845/st1-assignment-3/pull/26), [PR #27 – F8-01 repair (Rachel)](https://github.com/u3325845/st1-assignment-3/pull/27), [PR #28 – Regression tests (Rachel)](https://github.com/u3325845/st1-assignment-3/pull/28), [PR #30 – Booking validation refactor (Merlin)](https://github.com/u3325845/st1-assignment-3/pull/30), [PR #31 – Stage 8 evidence (Merlin)](https://github.com/u3325845/st1-assignment-3/pull/31), [PR #32 – Stage 7 domain tests (Tarnima)](https://github.com/u3325845/st1-assignment-3/pull/32), [PR #33 – Stage 7 verification record (Tarnima)](https://github.com/u3325845/st1-assignment-3/pull/33), and [PR #36 – Stage 8 regression (Tarnima)](https://github.com/u3325845/st1-assignment-3/pull/36).

- Stage 9: [Issue #37 – Appointment queries](https://github.com/u3325845/st1-assignment-3/issues/37), [PR #38 – Pure queries and tests (Merlin)](https://github.com/u3325845/st1-assignment-3/pull/38), [PR #40 – Practitioner appointment listing (Rachel)](https://github.com/u3325845/st1-assignment-3/pull/40), [PR #41 – Console implementation (Tarnima)](https://github.com/u3325845/st1-assignment-3/pull/41), [PR #44 – Console validation (Novera)](https://github.com/u3325845/st1-assignment-3/pull/44), [PR #45 – Section H review record (Novera)](https://github.com/u3325845/st1-assignment-3/pull/45), and [PR #46 – Final Stage 9 integration (Novera)](https://github.com/u3325845/st1-assignment-3/pull/46).

These PRs were merged through the team's GitHub review and integration workflow. The verified Stage 9 integration baseline is commit [`c871297`](https://github.com/u3325845/st1-assignment-3/commit/c871297) on `main`. Running `python -m pytest -q` from `project/` on 9 November 2026 resulted in 157 tests passed in 0.33s. Final Stage 12 PR links, reviewed diff and release SHA will be added after final integration.

Independent reviewer / feedback / response:  The team used independent GitHub pull request reviews before merging changes. In Stage 6, Merlin approved Rachel's patient lookup implementation (PR #3, "looks good"), while Rachel approved Merlin's practitioner lookup implementation (PR #5, "all good"). Tarnima and Rachel independently approved Novera's cancellation service (PR #14). In Stage 7, Rachel approved Merlin's practitioner domain and service tests (PR #20, "good work!"). In Stage 9, Tarnima approved Merlin's pure appointment queries (PR #38) and Rachel's practitioner appointment listing (PR #40). Merlin approved Tarnima's console implementation (PR #41), Novera's console validation changes (PR #44, "All good"), Stage 9 Section H documentation (PR #45, "all good"), and final Stage 9 integration (PR #46, "all good"). These approval records demonstrate cross-member review. Final Stage 12 review and any requested changes or responses must be recorded after its PR is reviewed.

Integration commit / full recheck: Stage 9 development and documentation were integrated into `main` through PR #45 and PR #46. The verified integration commit is `c871297`. The local `stage12/release-evidence` branch was updated using `git fetch origin` and `git merge origin/main`, completing a fast-forward merge without conflicts. Full regression testing was performed on 9 November 2026 using `python -m pytest -q` from the `project/` directory, with all 157 tests passing in 0.33 seconds. The Stage 12 draft was safely restored after integration. The final Stage 12 release SHA and regression results will be recorded after all team changes are merged.

Tracked and untracked file inspection / cleanliness:On 9 November 2026, the repository was inspected using `git status --short`, `git ls-files` and `git status --short --ignored`. The only modified tracked file was `stage12/stage12_activities_and_evidence.md`, containing ongoing Stage 12 documentation. No unexpected untracked files were reported. The `.idea/`, `.pytest_cache/` and `__pycache__/` directories were correctly ignored by Git. The current branch inspection found no unintended changes; the final release branch will be rechecked after integration.

Secrets/staff material/caches/tool-metadata exclusion check:  The repository's tracked and ignored file lists were inspected using `git ls-files` and `git status --short --ignored` on 9 November 2026. The tracked files consisted of application source code, tests, README files, requirements, Git configuration and stage evidence documents. No obviously sensitive or staff-only filenames were identified. PyCharm metadata (`.idea/`), pytest cache (`.pytest_cache/`) and Python bytecode caches (`__pycache__/`) were ignored and excluded from normal Git tracking. A final content-level secrets check and submission ZIP inspection remain to be completed before release.

Candidate recovery plan / known-good SHA: The verified Stage 9 integration baseline is commit [`c871297`](https://github.com/u3325845/st1-assignment-3/commit/c871297) on `main`, which passed all 157 automated tests in 0.33 seconds on 9 November 2026. This commit serves as the current known-good recovery reference. If later Stage 12 integration introduces a regression, the team will compare the changes against this baseline, identify and correct the issue, and rerun the affected tests and complete regression suite before release approval. The final known-good release SHA will be updated after all Stage 12 contributions are integrated and verified.

Named substantive contributions: The four undergraduate team members contributed to SmartCare development, testing, review and integration across Stages 6–9.

- Merlin: Implemented FR-03 practitioner lookup and tests (PR #5), Stage 7 practitioner domain/service tests (PR #20), Stage 8 booking validation refactoring (PR #30), and Stage 9 pure appointment queries with 12 tests (PR #38). Responsible for Stage 12 Sections A, B and I.
- Rachel: Implemented FR-02 patient lookup (PR #3), patient domain tests (PR #16), Stage 8 defect fixes and regression tests (PRs #27 and #28), and Stage 9 practitioner appointment listing (PR #40). Responsible for Stage 12 Sections C, E and H.
- Tarnima: Contributed validation tests (PR #8), appointment validation and construction (PRs #15 and #18), Stage 8 regression verification (PR #36), and Stage 9 interactive console implementation (PR #41). Responsible for Stage 12 Sections D, J and M.
- Novera: Implemented appointment cancellation (PR #14), cancellation history tests (PR #22), cancelled-appointment lookup repair (PR #26), Stage 9 console validation and README updates (PR #44), and Stage 9 integration documentation and final merge (PRs #45 and #46). Responsible for Stage 12 Sections F, G and L.

All members contribute to shared Stage 12 Sections K and N. Final Stage 12 contributions and approvals will be confirmed after integration.


## J Human release decision

Decision — READY FOR COURSE RELEASE / READY WITH DOCUMENTED LIMITATIONS / NOT YET READY: [response]
Approver / date / rationale and evidence: [response]
What risks remain / conditions / owners: [response]
Can the team explain the system: [response]
Can a change be recovered: [response]
Common decision / PG decision where different: [response]


## K Final tested release SHA

Exact common tested SHA: [response]
Exact PG tested SHA or not applicable: [response]
Final submitted SHA / repository URL: [response]
Evidence-only later commit and difference explanation: [response]
Executable changes after testing and re-verification: [response]
Source ZIP name / SHA correspondence / extracted comparison: [response]


## L Submission package verification

- [ ] Feature freeze and scoped requirements traced.
- [ ] Applicable full regressions, integrated demo and invalid paths verified.
- [ ] Architecture/code quality and final AI/dependency checks complete.
- [ ] Root README and project/README reproduced by another verifier.
- [ ] Release notes, technical debt and limitations visible.
- [ ] Independent human review, integration and release decision recorded.
- [ ] Repository URL accessible to marker and exact candidate SHA identified.
- [ ] One source ZIP from submitted commit with root README.md and .gitignore.
- [ ] project/ source and all accumulated applicable tests included.
- [ ] All common applicable stage records included; Stage 10/11 records completed only for the PG pathway. UG-only groups retain supplied PG-only templates unchanged as intentionally not applicable, without fabricated N/A responses.
- [ ] No .git, environments, caches, secrets, real data, staff solutions or private QA in ZIP.
- [ ] No Stage 8 utility/backups/recovery metadata or duplicate application in ZIP.
- [ ] Mixed-group common protection and candidate upload routing checked.
- [ ] Group reflection, confidential individual peer forms and common team viva routed separately.

Confirmed assessment item/upload route: [response]
Deadline/timezone: [response]
Repository access arrangement: [response]
Mixed-candidate upload arrangement: [response]
Oral/video recording/accessibility arrangements: [response]
Remaining administration or release dependency: [response]


## M Formative questions

1. What is a release candidate?

A release candidate is a version of the software that has completed development and is being checked before final release. It should contain the intended features and undergo testing, review and documentation checks to confirm it is ready.

2. What is feature freeze and why is it used?

Feature freeze means stopping the addition of new features so the team can focus on testing, fixing defects and preparing the release. It reduces the risk of introducing new problems near submission.

3. What is regression testing in a release context?

Regression testing means rerunning existing tests after changes or integration to ensure previously working functionality still behaves correctly. For SmartCare, this includes registration, booking, conflict prevention, cancellation, lookup and appointment listing.

4. What is a known limitation?

A known limitation is a restriction or missing capability that the team understands and documents. For example, SmartCare stores data only during the current session, so records are lost when the application exits. This is an accepted scope limitation rather than a defect.

5. What is technical debt?

Technical debt is the future maintenance work created when a team chooses a simpler or temporary solution instead of a more complete one. It should be documented so its impact and possible future improvements are understood. Not every intentionally excluded feature is technical debt.

6. What are release notes?

Release notes summarise what a software version delivers, including implemented features, important fixes, improvements and known limitations. They help users and reviewers understand what has changed and what the software can currently do.

7. What is software maintenance?

Software maintenance is the process of correcting defects, improving code quality, adapting software to changing requirements and keeping it reliable after development or release. It also includes updating tests and documentation when changes are made.

8. What is the purpose of the individual demonstration/viva?

The individual demonstration or viva checks whether each student understands the system and can explain their own contributions. Students should be able to demonstrate requirements, discuss architecture, explain tests and design decisions, and describe how they evaluated GitHub Copilot's review feedback.

9. What should the final responsible-AI check establish before release?

GitHub Copilot was used to review the proposed design and provide recommendations. I evaluated its feedback against the project requirements and decided which suggestions to accept, modify or reject. The final decisions remained my responsibility.

10. What is the main course conclusion about AI and the role of the software engineer?

GitHub Copilot can provide useful design feedback and identify potential problems, but the software engineer remains responsible for evaluating recommendations, making decisions and verifying correctness. In SmartCare, I reviewed Copilot's suggestions and rejected unnecessary framework classes and persistent storage because they were outside the project scope. This demonstrated the importance of human judgement in developing reliable and maintainable software.

## N Reflection viva and handover

Strongest evidence SmartCare is ready: [response]
Weakest area: [response]
How AI use changed from Stage 1 to Stage 12: [response]
Start doing — engineering and AI use: [response]
Stop doing — engineering and AI use: [response]
Continue doing — engineering and AI use: [response]
What worked / caused rework / future delivery improvement: [response]
One paragraph — If AI can write code why do we still need software engineers: [response]

| Preparation item | Own explanation and evidence link |
|---|---|
| Problem and stakeholders | [response] |
| Two requirements and acceptance criteria | [response] |
| Domain model and architecture | [response] |
| Design trade-off | [response] |
| Meaningful test and its limits / 100 percent coverage | [response] |
| Diagnosed defect and verification | [response] |
| Shared store and session-state/query responsibilities | [response] |
| What would break if session-state lookup/query responsibilities changed? | [response] |
| Why cancellation is domain behaviour / conflict coordination is service behaviour | [response] |
| FR-07 retained history test | [response] |
| Actual AI change rejected/modified or honestly accepted with verification | [response] |
| Unresolved limitation / future production work | [response] |
| Personal implementation contribution | [response] |
| Personal test/review/design/integration contribution | [response] |
| PG agentic change and rescheduling verification | [response] |
| PG responsible-AI risk/remediation or supported no finding | [response] |

Optional bounded-change practice only: validation rule, focused test, safe error-message change, explicit-input query or agreed status rule with test. Explain expected impact before editing, make a small change, run the test, and identify evidence to inspect if unsure. No live AI unless explicitly permitted. Preserve the submitted candidate.

Practice question/change and reasoning: [response or not undertaken]
Separate reflection / peer / common team viva evidence links and routing: [response]
No further coding stage. Later corrections use the published assessment process.
