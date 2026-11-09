# Stage 12 activities and evidence

BLANK student response template. Supplied from the beginning in stage12/ in your EXISTING repository; complete it only when you reach Stage 12 after the previous applicable stage is integrated, verified and recorded; preserve project/, tests, earlier records and Git history. UG/common and PG/extended scope must be explicit. Use concise results and versioned links, not copied logs or source. No staff answers or fabricated approvals.

Group/tutorial: [response]
Members and UG/PG applicability: [response]


## A Release scope and starting SHA

Release label/version and requirements baseline: [response]
Common starting SHA / branch / applicable members: [response]
PG starting SHA / branch / applicable members or not applicable: [response]
Working-state review and approved integration: [response]
Protected common candidate and PG differences: [response]
Feature freeze / owner / verifier: [response]


## B Requirements and release readiness matrix

Tutorial activity 1: All tests pass, README setup is incomplete, one dependency is unreviewed and a known limitation is undocumented. Decide Release / Release with conditions / Do not release and justify: [response]

Tutorial activity 2 and actual readiness matrix. Add exact requirement/acceptance IDs, evidence and reviewer; distinguish common/PG applicability.

| Release claim / requirement / scope | Evidence | Location/link and SHA | Reviewer | Sufficient? | Gap/action |
|---|---|---|---|---|---|
| Cancellation history works | [response] | [response] | [response] | [response] | [response] |
| Architecture responsibilities are appropriate | [response] | [response] | [response] | [response] | [response] |
| Rescheduling is safe — PG only | [response] | [response] | [response] | [response] | [response] |
| AI use is responsible — common recheck / PG assurance | [response] | [response] | [response] | [response] | [response] |
| System is maintainable | [response] | [response] | [response] | [response] | [response] |
| FR-01–03 register/find and validation | [response] | [response] | [response] | [response] | [response] |
| FR-04–05 booking/conflict rules | [response] | [response] | [response] | [response] | [response] |
| FR-06–08 cancellation/history/find | [response] | [response] | [response] | [response] | [response] |
| FR-09 and QRY/FP listing/filter/order/purity | [response] | [response] | [response] | [response] | [response] |
| UI full console sequence and error recovery | [response] | [response] | [response] | [response] | [response] |
| Session-only scope / FR-10 retired | [response] | [response] | [response] | [response] | [response] |
| PG RES and assurance integration | [response] | [response] | [response] | [response] | [response] |


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

Issue / PR / diff links and reviewed SHA: [response]
Independent reviewer / feedback / response: [response]
Integration commit / full recheck: [response]
Tracked and untracked file inspection / cleanliness: [response]
Secrets/staff material/caches/tool-metadata exclusion check: [response]
Candidate recovery plan / known-good SHA: [response]
Named substantive contributions: [response]


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

The individual demonstration or viva checks whether each student understands the system and can explain their own contributions. Students should be able to demonstrate requirements, discuss architecture, explain tests and design decisions, and describe how they verified AI-assisted work.

9. What should the final responsible-AI check establish before release?

GitHub Copilot was used to review the proposed design and provide recommendations. I evaluated its feedback against the project requirements and decided which suggestions to accept, modify or reject. The final decisions remained my responsibility.

10. What is the main course conclusion about AI and the role of the software engineer?

AI can help generate code, identify possible problems and suggest improvements, but it cannot replace the software engineer's responsibility for understanding requirements, making design decisions and verifying correctness. SmartCare demonstrated this when we reviewed Copilot's suggestions and rejected unnecessary framework classes and persistent storage. Software engineers must use their judgement to ensure the final solution is appropriate, reliable and maintainable.


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
