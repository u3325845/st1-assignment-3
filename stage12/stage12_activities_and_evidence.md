# Stage 12 activities and evidence

BLANK student response template. Supplied from the beginning in stage12/ in your EXISTING repository; complete it only when you reach Stage 12 after the previous applicable stage is integrated, verified and recorded; preserve project/, tests, earlier records and Git history. UG/common and PG/extended scope must be explicit. Use concise results and versioned links, not copied logs or source. No staff answers or fabricated approvals.

Group/tutorial: Grp 2 tutorial Wed 4:30 - 6:30
Members and UG/PG applicability: Undergraduate, RachelUC, Merlin3313611, TarnimaKhan22, u3325845 (Novera)


## A Release scope and starting SHA

Release label/version and requirements baseline: SmartCare Assignment 3 – Stage 12 Final Release Candidate (Undergraduate). The release covers FR-01–FR-09, QRY-01–QRY-04, FP-01–FP-03 and UI-01–UI-02, based on the Assignment 3 Overview/revision 2 requirements baseline. FR-10 is retired and excluded from the release. The application uses session-only storage without a persistent database.
Common starting SHA / branch / applicable members:  The Stage 12 common starting point is commit c871297 on main, following the merge of Stage 9 PR #45 and PR #46. The applicable undergraduate members are Merlin, Rachel, Tarnima and Novera. The integrated application was verified locally on 9 November 2026 using python -m pytest -q from project/, with 157 tests passed in 0.33s.
PG starting SHA / branch / applicable members or not applicable: not applicable
Working-state review and approved integration: The completed Stage 9 implementation was merged into main through PR #46 after the Stage 9 Section H documentation was merged through PR #45. The integrated application includes patient and practitioner registration and lookup, appointment booking, cancellation and retained history, practitioner appointment listing, pure query functions and the interactive console. The local stage12/release-evidence branch was fast-forwarded to c871297 without conflicts. Full regression testing from project/ using python -m pytest -q passed all 157 tests in 0.33s on 9 November 2026.
Protected common candidate and PG differences: All four members follow the undergraduate pathway, so PG-only Stages 10 and 11 are not applicable. The verified Stage 9 baseline is commit `c871297` on `main`, with 157 automated tests passing. Stage 12 documentation updates have since been integrated into `main`, including Merlin's root README correction in commit `f91d0e5` and UI-01/UI-02 evidence correction in commit `4a27ef9`. The final tested release SHA will be recorded in Section K after all team contributions are integrated and verified.
Feature freeze / owner / verifier: The undergraduate SmartCare implementation completed its Stage 9 feature scope at baseline commit `c871297`, with all 157 automated tests passing. No additional features are planned for Stage 12; only confirmed release-blocking defects should require implementation changes. Merlin is responsible for Sections A, B and I; Rachel for Sections C, E and H; Tarnima for Sections D, J and M; and Novera for Sections F, G and L. Sections K and N are shared responsibilities.The final release commit reference is recorded in Section K as `Final SHA -b9b56745abfdce70e54b7415fa9b378f04695210` until the final commit is confirmed. The latest recorded regression passed all 157 tests.

## B Requirements and release readiness matrix

Tutorial activity 1: All tests pass, README setup is incomplete, one dependency is unreviewed and a known limitation is undocumented. Decide Release / Release with conditions / Do not release and justify:
- Decision: Do not release yet.

In the tutorial scenario, SmartCare has passing tests, but the README setup instructions are incomplete, one dependency is unreviewed and a known limitation is undocumented. Passing tests alone is not enough for release approval. The team must complete the README, review the dependency, document the limitation and verify the application from a fresh copy before approving release.

Tutorial activity 2 and actual readiness matrix. Add exact requirement/acceptance IDs, evidence and reviewer; distinguish common/PG applicability.

| Release claim / requirement / scope | Evidence | Location/link and SHA | Reviewer | Sufficient? | Gap/action |
|---|---|---|---|---|---|
| FR-06-FR-08 - Cancellation and retained history (tutorial release claim) | Cancellation service, retained appointment history and regression tests; integrated suite passed 157 tests in 0.33s | `project/smartcare/services.py`, `project/tests/test_services.py`; Stage 8 PR #26; SHA `c871297` | Rachel | Yes for automated regression; final review pending | Confirm final cancellation/history review |
| Architecture responsibilities are appropriate - common | Reviewed `domain.py`, `data_store.py`, `services.py`, `queries.py` and `console.py` responsibilities against the documented architecture. Domain objects handle validation and appointment state; the data store manages session records; services coordinate workflows; pure queries filter and sort appointments; the console handles interaction. No release-blocking architecture issue identified in this review | `project/smartcare/`; `project/README.md`; Stage 9 baseline SHA `c871297` | Merlin | Yes - architecture responsibilities reviewed | Completed for requirement-level review; final integrated release verification remains separate |
| PG RES - Rescheduling safety | Not applicable (UG pathway) | Not applicable | Not applicable | N/A | None |
| Responsible AI - common recheck / PG assurance | Stage 6 records confirm human-first review and Copilot comparison. Stage 8 records confirm human hypotheses, evaluation of Copilot suggestions, independent review and regression testing. Stage 9 Sections B, E and H record human design, Copilot critique, independent PR review and integration. | Stage 6, Stage 8 and Stage 9 evidence documents; Stage 9 PR #44; baseline SHA `c871297` | Rachel | Yes for previous-stage evidence; Stage 12 review pending | Complete final Stage 12 responsible-AI and code-quality review in Section E. PG assurance not applicable |
| Maintainability - common | Separated modules, automated tests and updated application README; 157 tests passed | `project/README.md`, `project/smartcare/`, `project/tests/`; SHA `c871297` | Rachel | Pending final checks | Confirm code quality review and fresh-copy setup |
| FR-01-FR-03 - Registration, lookup and validation | Patient and practitioner registration, lookup and validation covered by integrated tests | `project/smartcare/services.py`, `project/tests/test_patient_lookup.py`, `project/tests/test_practitioner_lookup.py`; SHA `c871297` | Rachel | Yes for automated regression | Confirm final requirement-level review |
| FR-04-FR-05 - Booking and conflict rules | Reviewed booking service and conflict-check implementation. Booking requires registered participants, rejects duplicate appointment IDs and prevents two scheduled appointments for the same practitioner at the same date/time. Existing automated tests and Stage 9 demonstrations provide supporting evidence | `project/smartcare/services.py`, `project/smartcare/data_store.py`, `project/tests/test_services.py`, `project/tests/test_workflows.py`; baseline SHA `c871297` | Merlin | Yes - implementation and existing regression evidence reviewed | Completed for requirement-level review; final integrated regression remains separate |
| FR-06-FR-08 - Cancellation, history and lookup | Cancellation retains appointment history and lookup functionality; regression suite passed | `project/smartcare/services.py`, `project/tests/test_services.py`; Stage 8 PR #26; SHA `c871297` | Rachel | Yes for automated regression | Confirm cancellation and lookup acceptance criteria |
| FR-09, QRY-01-QRY-04, FP-01-FP-03 - Listing and pure queries | Reviewed practitioner appointment listing and pure query implementation. Results are filtered by practitioner and optional status, ordered by date/time and appointment ID, and returned as a new list without modifying the source list. Twelve Stage 9 query tests cover filtering, ordering, empty results, repeated calls and preservation of appointment data | `project/smartcare/services.py`, `project/smartcare/queries.py`, `project/tests/test_queries.py`; PR #38; baseline SHA `c871297` | Merlin | Yes - implementation and 12 existing query tests reviewed | Completed for requirement-level review; final integrated regression remains separate |
| UI-01-UI-02 - Console workflow and error recovery | Interactive console workflows and invalid-input recovery verified through the Stage 9 Section D console demonstration and 16 automated console validation tests; 157 tests passed overall | `project/smartcare/console.py`, `project/main.py`, `project/tests/test_workflows.py`, `project/tests/test_console_validation.py`; Stage 9 Section D; PR #44; commit `7cdc625`; SHA `c871297` | Tarnima | Yes - Stage 9 Section D demonstration and 16 console validation tests completed | Completed - Stage 9 Section D console demonstration and 16 automated console validation tests provide the required evidence |
| FR-10 - Retired persistence requirement / session-only scope | In-memory data store; persistence excluded under requirements revision 2. Session-only storage and data loss on exit are documented in the application README | `project/smartcare/data_store.py`, `project/README.md`; baseline SHA `c871297` | Merlin | Yes - documented undergraduate scope limitation | Completed - session-only limitation documented; final release documentation review remains pending |
| PG RES and assurance integration | Not applicable (UG pathway) | Not applicable | Not applicable | N/A | None |

## C Full regression results

| Suite/scope | Environment/version | Working directory and command | Tested SHA | Actual result | Evidence link |
|---|---|---|---|---|---|
| Complete common | Python 3.10.8; pytest 8.3.5; virtual environment | `project/`; `python -m pytest -q` | `d14685d` | 157 passed in 0.24s on 9 November 2026 | Local pytest output; `project/tests/` |
| Complete PG if applicable | Not applicable (undergraduate group) | Not applicable | Not applicable | PG-only requirements do not apply | Section A |
| Affected focused checks after correction | Python 3.10.8; pytest 8.3.5; virtual environment | `project/`; `python -m pytest tests/test_workflows.py::test_appointment_cancellation_and_history -q` | `d14685d` | 1 passed in 0.03s on 9 November 2026 | `project/tests/test_workflows.py`; local pytest output |
| Full integrated recheck | Tarnima; environment version not recorded in this evidence | `project/`; `python -m pytest -q` | `b76eec401bd23e3cbc4e505b3285a460cfdd05aa` | 157 passed in 1.05s on 9 November 2026; clean working tree | Tarnima's final integration verification; Section K |


Prior assertions preserved / reviewed test diff: The current baseline has 157 passing automated tests covering registration, lookup, booking, cancellation and retained history, practitioner appointment listing, pure queries and console validation. Final review of changes since `d14685d` is still pending to confirm existing test assertions have not been removed or weakened.

Remaining failure / limitation: No failing tests were reported. Tarnima's integrated regression at b76eec401bd23e3cbc4e505b3285a460cfdd05aa passed all 157 tests. SmartCare uses session-only storage, so records are lost when the application exits. Final SHA -b9b56745abfdce70e54b7415fa9b378f04695210



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
| PG reschedule identity/participants/time and no-op | Not applicable | PG-only requirement excluded from undergraduate release | N/A | N/A (UG pathway) |
| PG conflict/invalid status/failure non-mutation | Not applicable | PG-only requirement excluded from undergraduate release | N/A | N/A (UG pathway) |
| PG old slot / current lookup/list ordering / assurance risks | Not applicable | PG-only requirement excluded from undergraduate release | N/A | N/A (UG pathway) |

Stable demo owner / fresh process / command: Tarnima completed two manual console demonstrations using fresh processes and synthetic data. The application was launched from the project/ directory using python main.py --interactive. The demonstrations covered patient registration, lookup, appointment booking, conflict prevention, cancellation, retained history, filtering, invalid-input recovery and normal exit.

PG demonstrations through service/tests or not applicable: Not applicable. All four group members follow the undergraduate pathway, so PG-only requirements are excluded from this release.


## E Final code quality and AI review

| Review area | Code/evidence location | Finding or no finding | Correction/no change and recheck |
|---|---|---|---|
| OOP responsibilities and pure-query boundaries | `project/smartcare/domain.py`, `data_store.py`, `services.py`, `queries.py`, `console.py` | Domain classes validate their data and appointment status changes. The store manages records, services coordinate workflows, pure queries filter and sort, and the console handles input/output. | No change needed. Reviewed source code and 157 tests passed. |
| PascalCase and snake_case naming | `project/smartcare/` | Classes use PascalCase and functions, methods and variables generally use snake_case. | No change needed. |
| Useful type hints and meaningful docstrings | `project/smartcare/services.py`, `data_store.py`, `domain.py`, `queries.py`, `console.py`, `project/main.py` | Most public methods have type hints and docstrings. Some helper methods lack annotations or docstrings. Two lookup docstrings still contain Stage 6 TODO wording, and the main entry-point docstring is outdated. | Minor documentation debt; no functional correction needed for release. |
| Four-space indentation and imports/layout | `project/smartcare/`, `project/main.py` | Source files generally follow four-space indentation and readable imports. The console imports AppointmentStatus inside `run_menu()`, but this does not affect functionality. | No change needed. |
| Focused methods / duplication / dead or commented code | `project/smartcare/services.py`, `queries.py`, `console.py` | Query functions are short and focused. Services reuse shared validation and storage operations. `run_menu()` is relatively long but remains understandable for the undergraduate scope. | No release-blocking issue identified; no change needed. |
| Globals / leakage / unnecessary inheritance or frameworks | `project/smartcare/data_store.py`, `services.py`, `console.py` | Each menu session creates one shared store for its services. No global patient, practitioner or appointment collections or unnecessary inheritance frameworks were found. | No change needed. Session data remains in memory only. |
| No SQLite/persistence/repository ABCs/speculative features | `project/smartcare/`, `project/requirements-dev.txt` | No database, persistence framework or speculative architecture was found. This follows the undergraduate session-only requirements. | No change needed. |
| Synthetic data / secrets / dependencies / provenance | `project/smartcare/console.py`, `project/requirements-dev.txt`, `.gitignore`; Git checks | Demo uses synthetic records. The development dependency is pinned to pytest 8.3.5. Git filename and tracked-project text searches found no matches for the checked secret patterns. Environments, caches and IDE files are ignored. | No finding from these checks. They do not replace a complete security or final ZIP review. |
| Significant common Copilot contributions and human verification | `stage09/stage09_activities_and_evidence.md`, Section E; `project/smartcare/console.py` | Previous Copilot review supported the shared store, responsibility separation and input validation. Human review corrected outdated query feedback and rejected unnecessary frameworks and persistence. | Decisions checked against the recorded Stage 9 review and current source code. Current regression: 157 passed at `d14685d`. |
| PG plan/diff/test approvals and Stage 11 VERIFY/TRUST | Stage 12 Section A | Not applicable; all four members follow the undergraduate pathway. | No PG verification required. |

| AI claim | Affected requirement/code | Human check | Accept/Modify/Reject and reason | Actual outcome/action or no change |
|---|---|---|---|---|
| One shared data store and separated responsibilities | `smartcare/console.py`, `services.py`; common workflows | Reviewed shared-store creation and service calls against Stage 9 evidence. | Accept — maintains session continuity and avoids duplicated business rules. | Existing design retained; 157 regression tests passed. |
| Invalid-input recovery should be tested | `smartcare/console.py`, `tests/test_workflows.py` | Checked expected exception handling and recorded Stage 9 tests and demonstrations. | Accept — errors should not terminate the menu. | Existing validation retained; current regression passed. |
| Query and service dependencies were unfinished | `smartcare/queries.py`, `services.py` | Confirmed the query functions and practitioner listing service are implemented. | Modify — Copilot reviewed an older commit, so part of its feedback was outdated. | Existing query functions reused; no duplicate implementation added. |
| Additional menu framework classes and persistent storage | `smartcare/console.py`, `data_store.py` | Compared suggestions with the undergraduate session-only scope and existing implementation. | Reject — unnecessary complexity and persistence are outside the requirements. | Simple menu and in-memory storage retained; no change required. |

Access route or approved equivalent / limitations: GitHub Copilot review was recorded in Stage 9 Section E. Stage 12 independently inspected the current local source and reviewed the previous AI decisions against the implemented code. No new Stage 12 Copilot response has been recorded.

Available AI evidence and missing evidence honestly disclosed: Stage 9 contains the actual Copilot prompt, findings, human decisions and verification evidence. The current code and tests were reviewed at SHA `d14685d`, with 157 tests passing in 0.24s. A separate fresh Stage 12 Copilot review remains pending if required by the release checklist.



## F README and reproducibility check

| README item | Location | Verifier                                                           | Result/gap                                                                                                                                                                                      |
|---|---|--------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Purpose and included common/PG scope | `project/README.md` introduction and Features | Novera(author)                                                     | Present. Undergraduate common scope only; PG scope not applicable.                                                                                                                              |
| Out-of-scope capabilities and known limitations | `project/README.md` Limitations | Novera(author)                                                     | Present: session-only data, no rescheduling, past-date, duration or patient-conflict rules.                                                                                                     |
| Confirmed teaching Python version and dependency installation | `project/README.md` Setup | Merlin3313611 (fresh clone, Python 3.14.3); Novera (Python 3.14.7) | PASS: pytest 8.3.5 installed from `requirements-dev.txt`. Gap: PowerShell blocked `Activate.ps1`; workaround added to Setup.                                                                    |
| Working directory / demo / interactive / test commands | `project/README.md` Running the program and Running the tests | Merlin3313611                                                      | PASS: `python main.py` demo ran, `python main.py --interactive` menu opened and exited, `python -m pytest -q` gave 157 passed in 0.39s. The three focused test commands were not run by Merlin. |
| Repository structure and architecture responsibilities | `project/README.md` How the code is organised | Novera(author)                                                     | Present; the five listed modules exist in `project/smartcare/`.                                                                                                                                 |
| Responsible AI summary / synthetic-data rule | `project/README.md` Responsible AI use and Limitations | Novera(author)                                                     | Gap found by this check- no AI summary in the README. Added in this PR.                                                                                                                         |
| Release label/version and SHA links | `project/README.md` Release; root `README.md`  | Novera(author)                                                     | Gap found: no release section. Added; it points to the root README and Section K for the final SHA -b9b56745abfdce70e54b7415fa9b378f04695210.                                                                                           |
Root README index and project/README verified: project/README.md commands were reproduced by Merlin on a fresh clone. The root README was updated by Merlin (PR #48); its Python statement was corrected in commit f91d0e5 (merged via PR #50) to keep the Python 3.13 teaching baseline and add the Python 3.14.3 and 3.14.7 versions actually verified. The root README's final submitted SHA field is still to be completed after the release SHA is confirmed.
Fresh clone or extracted ZIP / candidate identity: Fresh GitHub clone of main at 2a6cc811cc82f511f5bfbb60bba45d9015aeb297 on 9 November 2026. ZIP verification is still to be done (Section L).
Verifier and clean environment / actual version: Merlin (Merlin3313611), new folder outside the development repository, new virtual environment, Windows PowerShell, Python 3.14.3, pytest 8.3.5. Novera(author) also ran the suite on Python 3.14.7.   Full report: [Merlin's fresh-clone verification report](https://github.com/u3325845/st1-assignment-3/issues/51).
Setup/run/test commands and observed results: git clone, python -m venv .venv, pip install -r requirements-dev.txt, python main.py (printed A1: P1 with DR1, 2026-10-01 09:00, scheduled and the session-only notice), python main.py --interactive (menu displayed, exit 0 printed the goodbye message), python -m pytest -q (157 passed in 0.39s). Merlin also checked patient registration, case-sensitive lookup and invalid menu recovery manually.
Missing local file or setup gap / remedy and recheck:  Gap: PowerShell execution policy blocked Activate.ps1 on Merlin's machine. Remedy: added a README note to run the environment's Python directly. Recheck: Novera ran `..\.venv\Scripts\python.exe -m pytest -q` from project/ on 9 November 2026: 157 passed in 0.24s. A second recheck of the updated README by another member is done by Merlin.


## G Known limitations debt and release notes

Delivered features: Register and find patients and practitioners; book appointments with a practitioner conflict rule; cancel SCHEDULED appointments with cancelled history kept; find appointments by ID; list a practitioner's appointments with optional status filter and deterministic order; interactive console menu with error recovery.

Important fixes: Stage 8 F8-01 (practitioner double-booking conflict) and F8-02 (appointment lookup skipped cancelled appointments; fixed so retained history can be found).

Architecture/quality improvements: Pure query functions separated from services; services coordinate the store and domain; the console handles only input and output; console validation tests added for invalid-input recovery.

Known limitations: Data is session-only and lost on exit. No rescheduling, past-date rule, appointment duration or patient-conflict rule.

AI-assisted development note: GitHub Copilot was used for design review and diagnosis.All AI output was reviewed, run and checked by the members and decisions are recorded in the stage records.

| Debt item | Impact | Priority | Future action   | Accepted? / release rationale       |
|-|--|----------|-----------------|-------------------------------------|
| Session-only data| Records are lost on exit | Medium   | Add persistence | Yes. FR-10 retired and out of scope |
| No rescheduling | Users must cancel and rebook | Low | Add a reschedule service | Yes, rescheduling is PG scope |
| Stale `Stage 6 TODO` docstrings in `services.py` and outdated `main.py` docstring | Confusing to readers, no behaviour effect | Low | Clean up comments in a reviewed PR | Yes, cosmetic |
Session-only synthetic data and minute-precision local time: All data is synthetic and held in memory only; it is lost when the program exits. Appointment times use local time with minute precision and no timezone handling.

Production auth/roles, portal, notifications, billing/insurance, clinical AI exclusions: Not implemented and out of scope. SmartCare has no login or roles, patient portal, notifications, billing or insurance, and no clinical decision or AI features.

Scale/concurrency, timezone policy, operations/monitoring, accessibility/usability limitations: Designed for a single user and a single session; no concurrency handling, timezone policy or monitoring. The console menu is text-only and has no accessibility features beyond plain text.

Difference between accepted scope limit and unresolved required behaviour: The limits above are accepted scope decisions under requirements revision 2 (FR-10 retired). No required behaviour (FR-01 to FR-09, QRY, FP, UI-01 and UI-02) is known to be unresolved.

PG assurance residual risks / owner / status or not applicable: Not applicable (all members are undergraduates).


## H Release findings and corrective action

| Requirement/claim | Reproduction/observation | Impact/severity | Owner/action | Corrective diff | Focused/full recheck | Residual limit |
|---|---|---|---|---|---|---|
| FR-01–FR-03 Registration and lookup | Reviewed patient and practitioner registration, validation and lookup code. Existing tests passed. | No confirmed defect | Rachel — no change needed | None | Full regression: 157 passed | Final integrated recheck pending |
| FR-04–FR-05 Booking and conflict prevention | Reviewed booking and conflict logic. Section D records rejection of same-practitioner exact-time conflicts and acceptance of different-practitioner bookings. | No confirmed defect | Rachel — no change needed | None | Full regression: 157 passed | Conflict checking uses exact date/time; no duration or concurrency handling |
| FR-06–FR-08 Cancellation and retained history | Reviewed `Appointment.cancel()` and appointment lookup. Section D records successful cancellation, retained history and rejection of repeated cancellation. | No confirmed defect | Rachel — no change needed | None | Focused test: 1 passed in 0.03s; full regression: 157 passed | Session-only records are lost on exit |
| FR-09, QRY-01–QRY-04, FP-01–FP-03 Listing and pure queries | Reviewed `select_appointments()` and practitioner listing service. Filtering and chronological ordering use a new list without modifying stored records. | No confirmed defect | Rachel — no change needed | None | Full regression: 157 passed; Section D demonstrations | Final integrated recheck pending |
| UI-01–UI-02 Console and invalid-input recovery | Reviewed menu input handling and exception recovery. Section D records successful invalid-date, invalid-status, unknown-record and menu-choice recovery. | No confirmed defect | Rachel — no change needed | None | Full regression: 157 passed; Section D demonstrations | Unexpected process interruptions are not handled by normal menu recovery |
| Code quality and documentation | Reviewed source modules. Found outdated Stage 6 TODO docstrings, an outdated `main.py` docstring and some missing annotations/docstrings. | Low — maintainability/documentation only | Rachel — documented as minor technical debt | None | Code inspection; full regression: 157 passed | Cosmetic documentation cleanup can be done later |

Justified no-change conclusion if no defect found: The Stage 12 review did not identify a confirmed release-blocking defect in the inspected undergraduate application. The full regression suite passed 157 tests in 0.24s at SHA `d14685d`, and the focused cancellation-history test passed in 0.03s. Existing Stage 12 Section D demonstrations also support the required workflows. The identified documentation issues and session-only limitations do not require changes to working code for this release.

Release blockers still open / status: Release blockers still open / status: The integrated undergraduate application passed all 157 automated tests at `b76eec401bd23e3cbc4e505b3285a460cfdd05aa`. No confirmed release-blocking application defect has been identified. Final submission checks, ZIP verification and team release approval remain to be confirmed. Final SHA -b9b56745abfdce70e54b7415fa9b378f04695210



## I Git review and integration evidence

Issue / PR / diff links and reviewed SHA: SmartCare development was managed through GitHub issues, feature branches and pull requests across Stages 6–9.

- Stage 6: [PR #3 – Patient lookup (Rachel)](https://github.com/u3325845/st1-assignment-3/pull/3), [PR #4 – Patient lookup evidence (Rachel)](https://github.com/u3325845/st1-assignment-3/pull/4), [PR #5 – Practitioner lookup (Merlin)](https://github.com/u3325845/st1-assignment-3/pull/5), [PR #8 – Validation tests (Tarnima)](https://github.com/u3325845/st1-assignment-3/pull/8), [PR #9 – Patient lookup evidence (Rachel)](https://github.com/u3325845/st1-assignment-3/pull/9), [PR #10 – Practitioner lookup evidence (Merlin)](https://github.com/u3325845/st1-assignment-3/pull/10), and [PR #14 – Cancellation service (Novera)](https://github.com/u3325845/st1-assignment-3/pull/14).

- Stage 7: [PR #15 – Appointment validation (Tarnima)](https://github.com/u3325845/st1-assignment-3/pull/15), [PR #16 – Patient domain tests (Rachel)](https://github.com/u3325845/st1-assignment-3/pull/16), [PR #18 – Appointment construction (Tarnima)](https://github.com/u3325845/st1-assignment-3/pull/18), [PR #20 – Practitioner tests (Merlin)](https://github.com/u3325845/st1-assignment-3/pull/20), [PR #22 – Cancellation history tests (Novera)](https://github.com/u3325845/st1-assignment-3/pull/22), and [PR #23 – Domain test updates (Rachel)](https://github.com/u3325845/st1-assignment-3/pull/23).

- Stage 8: [PR #26 – Cancelled appointment lookup repair (Novera)](https://github.com/u3325845/st1-assignment-3/pull/26), [PR #27 – F8-01 repair (Rachel)](https://github.com/u3325845/st1-assignment-3/pull/27), [PR #28 – Regression tests (Rachel)](https://github.com/u3325845/st1-assignment-3/pull/28), [PR #30 – Booking validation refactor (Merlin)](https://github.com/u3325845/st1-assignment-3/pull/30), [PR #31 – Stage 8 evidence (Merlin)](https://github.com/u3325845/st1-assignment-3/pull/31), [PR #32 – Stage 7 domain tests (Tarnima)](https://github.com/u3325845/st1-assignment-3/pull/32), [PR #33 – Stage 7 verification record (Tarnima)](https://github.com/u3325845/st1-assignment-3/pull/33), and [PR #36 – Stage 8 regression (Tarnima)](https://github.com/u3325845/st1-assignment-3/pull/36).

- Stage 9: [Issue #37 – Appointment queries](https://github.com/u3325845/st1-assignment-3/issues/37), [PR #38 – Pure queries and tests (Merlin)](https://github.com/u3325845/st1-assignment-3/pull/38), [PR #40 – Practitioner appointment listing (Rachel)](https://github.com/u3325845/st1-assignment-3/pull/40), [PR #41 – Console implementation (Tarnima)](https://github.com/u3325845/st1-assignment-3/pull/41), [PR #44 – Console validation (Novera)](https://github.com/u3325845/st1-assignment-3/pull/44), [PR #45 – Section H review record (Novera)](https://github.com/u3325845/st1-assignment-3/pull/45), and [PR #46 – Final Stage 9 integration (Novera)](https://github.com/u3325845/st1-assignment-3/pull/46).

These PRs were merged through the team's GitHub review and integration workflow. The verified Stage 9 integration baseline is commit [`c871297`](https://github.com/u3325845/st1-assignment-3/commit/c871297) on `main`. Running `python -m pytest -q` from `project/` on 9 November 2026 resulted in 157 tests passed in 0.33s. Final Stage 12 PR links, reviewed diff and release SHA will be added after final integration.


Stage 12 Git updates: Merlin updated the root README in commit `f91d0e5` and corrected the UI-01/UI-02 readiness evidence in commit `4a27ef9`. Independent fresh-clone verification is recorded in GitHub Issue #51, with full details in Section F.

Independent reviewer / feedback / response:  The team used independent GitHub pull request reviews before merging changes. In Stage 6, Merlin approved Rachel's patient lookup implementation (PR #3, "looks good"), while Rachel approved Merlin's practitioner lookup implementation (PR #5, "all good"). Tarnima and Rachel independently approved Novera's cancellation service (PR #14). In Stage 7, Rachel approved Merlin's practitioner domain and service tests (PR #20, "good work!"). In Stage 9, Tarnima approved Merlin's pure appointment queries (PR #38) and Rachel's practitioner appointment listing (PR #40). Merlin approved Tarnima's console implementation (PR #41), Novera's console validation changes (PR #44, "All good"), Stage 9 Section H documentation (PR #45, "all good"), and final Stage 9 integration (PR #46, "all good"). These approval records demonstrate cross-member review. Final Stage 12 review and any requested changes or responses must be recorded after its PR is reviewed.

Integration commit / full recheck: Stage 9 development and documentation were integrated into `main` through PR #45 and PR #46, establishing the verified baseline `c871297`. On 9 November 2026, the integrated baseline passed 157 automated tests in 0.33 seconds using `python -m pytest -q` from `project/`. The local `stage12/release-evidence` branch was previously updated through a successful fast-forward merge. Merlin also completed an independent fresh-clone verification at commit `2a6cc811cc82f511f5bfbb60bba45d9015aeb297`, with all 157 tests passing in 0.39 seconds. Subsequent Stage 12 documentation changes were pushed to `main`, including commits `f91d0e5` and `4a27ef9`. During the UI-01/UI-02 documentation update, the initial push was rejected because remote `main` had advanced. Merlin ran `git pull --rebase origin main`, which completed without conflicts, and then successfully pushed the updated commit. The latest recorded integrated regression passed all 157 tests at `b76eec401bd23e3cbc4e505b3285a460cfdd05aa`. The latest integrated commit before final documentation updates was `83fd86a4355eae03a18d4c420e5706645c56d9b4`. Final SHA -b9b56745abfdce70e54b7415fa9b378f04695210

Tracked and untracked file inspection / cleanliness: On 9 November 2026, the repository was inspected using `git status --short`, `git ls-files` and `git status --short --ignored`. The only modified tracked file was `stage12/stage12_activities_and_evidence.md`, containing ongoing Stage 12 documentation. No unexpected untracked files were reported. The `.idea/`, `.pytest_cache/` and `__pycache__/` directories were correctly ignored by Git. The inspection found no unintended changes at the time of checking. Repository cleanliness must be confirmed again at the final release SHA.

Secrets/staff material/caches/tool-metadata exclusion check:  The repository's tracked and ignored file lists were inspected using `git ls-files` and `git status --short --ignored` on 9 November 2026. The tracked files consisted of application source code, tests, README files, requirements, Git configuration and stage evidence documents. No obviously sensitive or staff-only filenames were identified. PyCharm metadata (`.idea/`), pytest cache (`.pytest_cache/`) and Python bytecode caches (`__pycache__/`) were ignored and excluded from normal Git tracking. A final content-level secrets check and submission ZIP inspection remain to be completed before release.

Candidate recovery plan / known-good SHA: The verified Stage 9 integration baseline is commit [`c871297`](https://github.com/u3325845/st1-assignment-3/commit/c871297) on `main`, which passed all 157 automated tests in 0.33 seconds on 9 November 2026. This commit serves as the current known-good recovery reference. If later Stage 12 integration introduces a regression, the team will compare the changes against this baseline, identify and correct the issue, and rerun the affected tests and complete regression suite before release approval. The final known-good release SHA will be updated after all Stage 12 contributions are integrated and verified.

Named substantive contributions: The four undergraduate team members contributed to SmartCare development, testing, review and integration across Stages 6–9.

- Merlin: Implemented FR-03 practitioner lookup and tests (PR #5), Stage 7 practitioner domain/service tests (PR #20), Stage 8 booking validation refactoring (PR #30), and Stage 9 pure appointment queries with 12 tests (PR #38). In Stage 12, contributed release scope, readiness reviews and Git integration evidence (Sections A, B and I), completed independent fresh-clone verification with 157 passing tests (Issue #51), corrected the root README Python verification wording (commit `f91d0e5`), and updated UI-01/UI-02 release readiness evidence (commit `4a27ef9`).
- Rachel: Implemented FR-02 patient lookup (PR #3), patient domain tests (PR #16), Stage 8 defect fixes and regression tests (PRs #27 and #28), and Stage 9 practitioner appointment listing (PR #40). Responsible for Stage 12 Sections C, E and H.
- Tarnima: Contributed validation tests (PR #8), appointment validation and construction (PRs #15 and #18), Stage 8 regression verification (PR #36), and Stage 9 interactive console implementation (PR #41). Responsible for Stage 12 Sections D, J and M.
- Novera: Implemented appointment cancellation (PR #14), cancellation history tests (PR #22), cancelled-appointment lookup repair (PR #26), Stage 9 console validation and README updates (PR #44), and Stage 9 integration documentation and final merge (PRs #45 and #46). Responsible for Stage 12 Sections F, G and L.

All members contribute to shared Stage 12 Sections K and N. Final Stage 12 contributions and approvals will be confirmed after integration.


## J Human release decision


Decision — READY FOR COURSE RELEASE / READY WITH DOCUMENTED LIMITATIONS / NOT YET READY: READY WITH DOCUMENTED LIMITATIONS. The team unanimously approved SmartCare for its final undergraduate course release on 9 November 2026. All Stage 12 contributions have been integrated into main, and the final README, evidence documents and submission ZIP have been checked. No known release-blocking defects remain.

Approver / date / rationale and evidence: All four team members — Merlin, Rachel, Tarnima and Novera — approved the release on 9 November 2026. Tarnima independently verified the integrated commit `b76eec401bd23e3cbc4e505b3285a460cfdd05aa` by running `python -m pytest -q` from `project/`. All 157 tests passed in 1.05 seconds, and the working tree was clean. Manual console demonstrations, code-quality reviews and independent fresh-clone verification also support the release decision. Merlin completed the final README, evidence and ZIP checks.

What risks remain / conditions / owners: No known release-blocking defects remain, and no further release conditions are required. The team accepts the documented undergraduate scope limitations, including session-only storage, no persistent database, no appointment rescheduling and no concurrent multi-user operation. These limitations do not prevent SmartCare from meeting the agreed undergraduate requirements.

Can the team explain the system: Yes. All four members contributed to implementation, testing, integration and review. The team can explain the separation between domain objects, the in-memory data store, services, pure queries and console interaction. Project records and GitHub history document individual contributions, engineering decisions, debugging activities and human evaluation of AI suggestions. Supporting evidence is available for the individual viva.

Can a change be recovered: Yes. GitHub preserves the project's commit history, pull requests and reviewed changes. The verified Stage 9 baseline `c871297` provides a known-good recovery reference, while the tested integrated commit `b76eec401bd23e3cbc4e505b3285a460cfdd05aa` passed all 157 automated tests. If a future change introduces a defect, the team can identify the affected commit, compare changes, restore or repair the relevant code and rerun focused and full regression tests.

Common decision / PG decision where different: READY WITH DOCUMENTED LIMITATIONS for the undergraduate release. All four members approved the release, and the integrated application, automated tests, manual demonstrations, documentation and submission package have been verified. PG-only Stages 10 and 11, including extended rescheduling and assurance requirements, are not applicable because all four members follow the undergraduate pathway.


## K Final tested release SHA

Exact common tested SHA: `b76eec401bd23e3cbc4e505b3285a460cfdd05aa` on `main`. On 9 November 2026, Tarnima pulled the latest integrated changes and ran `python -m pytest -q` from `project/`. All 157 tests passed in 1.05 seconds. The working tree was clean.
Exact PG tested SHA or not applicable: Not applicable. 
Final submitted SHA / repository URL: Final SHA -b9b56745abfdce70e54b7415fa9b378f04695210 Repository: https://github.com/u3325845/st1-assignment-3
Evidence-only later commit and difference explanation: Stage 12 documentation changes were integrated after Tarnima's tested commit. Final SHA -b9b56745abfdce70e54b7415fa9b378f04695210 The difference must be checked to confirm whether changes were documentation-only.
Executable changes after testing and re-verification: No executable changes were reported during Tarnima's verification. Changes after that commit must be checked; any executable changes require retesting.
Source ZIP name / SHA correspondence / extracted comparison: Novera will download the final source ZIP from the submitted commit and verify its contents against the repository. Final SHA -b9b56745abfdce70e54b7415fa9b378f04695210


## L Submission package verification

- [x] Feature freeze and scoped requirements traced.
- [x] Applicable full regressions, integrated demo and invalid paths verified.
- [x] Architecture/code quality and final AI/dependency checks complete.
- [x] Root README and project/README reproduced by another verifier.
- [x] Release notes, technical debt and limitations visible.
- [x] Independent human review, integration and release decision recorded.
- [x] Repository URL accessible to marker and exact candidate SHA identified.
- [x] One source ZIP from submitted commit with root README.md and .gitignore.
- [x] project/ source and all accumulated applicable tests included.
- [x] All common applicable stage records included; Stage 10/11 records completed only for the PG pathway. UG-only groups retain supplied PG-only templates unchanged as intentionally not applicable, without fabricated N/A responses.
- [x] No .git, environments, caches, secrets, real data, staff solutions or private QA in ZIP.
- [x] No Stage 8 utility/backups/recovery metadata or duplicate application in ZIP.
- [ ] Mixed-group common protection and candidate upload routing checked.
- [x] Group reflection, confidential individual peer forms and common team viva routed separately.

Confirmed assessment item/upload route:https://uclearn.canberra.edu.au/courses/20399/assignments/181220
Deadline/timezone: Monday 9 November 2026, 11:59 pm, Canberra time
Repository access arrangement: The repository is public at https://github.com/u3325845/st1-assignment-3, so the marker can access it; the exact candidate SHA is recorded in Section K.
Mixed-candidate upload arrangement: Not applicable; all four members follow the undergraduate pathway.
Oral/video recording/accessibility arrangements: Individually arranged
Remaining administration or release dependency: Each member submits their confidential individual peer form and reflection separately; the team viva is arranged separately; the source ZIP is uploaded as above.


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

Strongest evidence SmartCare is ready: The strongest evidence is the integrated undergraduate application passing all 157 automated tests, supported by manual console demonstrations and independent fresh-clone verification. The tests cover registration, lookup, booking, conflict prevention, cancellation, retained history, practitioner appointment listing and invalid-input recovery. The application also has documented setup instructions and known limitations.
Weakest area: SmartCare uses session-only storage, meaning all records are lost when the application exits. This is an accepted limitation because persistence (FR-10) was retired from the undergraduate requirements. The application also does not support rescheduling, appointment durations or concurrent users. Final submission verification and approval must be completed before release.
How AI use changed from Stage 1 to Stage 12: The team developed a more careful approach to using GitHub Copilot. Rather than treating AI suggestions as correct automatically, members compared recommendations with the requirements, inspected the existing code and verified decisions through tests and reviews. Suggestions involving unnecessary framework classes and persistent storage were rejected because they were outside the project scope.
Start doing — engineering and AI use: Start recording design decisions, test evidence and AI recommendations more consistently throughout development. Check AI suggestions against the current code and requirements before accepting them.
Stop doing — engineering and AI use: Stop relying on outdated AI feedback, making unnecessary architectural changes or leaving documentation updates until the final release stage.
Continue doing — engineering and AI use: Continue using feature branches, meaningful tests, independent pull request reviews and full regression testing. Continue treating AI as a supporting tool while keeping final engineering decisions and verification under human responsibility.
What worked / caused rework / future delivery improvement:  GitHub collaboration, clear module responsibilities, automated testing and independent reviews helped the team integrate SmartCare successfully. Some rework came from outdated documentation, changing requirements and reviewing AI suggestions against older versions of the code. In future projects, the team should update documentation alongside implementation and verify integration earlier.
One paragraph — If AI can write code why do we still need software engineers: Software engineers are still needed because writing code is only one part of software development. Engineers must understand requirements, design suitable solutions, identify defects, evaluate risks and verify that software behaves correctly. AI can suggest code or improvements, but its recommendations may be incorrect, outdated or unnecessary. In SmartCare, the team reviewed Copilot's suggestions and rejected additional frameworks and persistence because they did not match the undergraduate scope. This showed that human judgement, testing and accountability remain essential.

| Preparation item | Own explanation and evidence link |
|---|---|
| Problem and stakeholders | SmartCare is a small appointment-management application for patients, practitioners and administrative users. It supports registration, lookup, booking, cancellation and appointment history. Evidence: `project/README.md`; Stage 9 console demonstration. |
| Two requirements and acceptance criteria | FR-04/FR-05: Booking must use registered participants and reject two scheduled appointments for the same practitioner at the same date and time. FR-06/FR-07: A scheduled appointment can be cancelled, but its record must remain available for later lookup. Evidence: `project/smartcare/services.py`; `project/tests/test_services.py`; Stage 8 records. |
| Domain model and architecture | `domain.py` defines and validates domain objects, `data_store.py` manages in-memory records, `services.py` coordinates workflows, `queries.py` provides pure filtering and sorting functions, and `console.py` handles user interaction. Evidence: `project/smartcare/`. |
| Design trade-off | The team retained a simple shared in-memory store rather than introducing persistence or additional frameworks. This meets the undergraduate requirements and avoids unnecessary complexity, although records are lost after exit. Evidence: Stage 9 Section E; `project/README.md`. |
| Meaningful test and its limits / 100 percent coverage | `test_repeated_cancellation_is_rejected_and_history_is_kept` checks that an appointment can be cancelled, repeated cancellation is rejected and the cancelled appointment remains retrievable. It does not independently verify practitioner listing. Even 100% code coverage would not prove that every requirement or input case was tested correctly. Evidence: `project/tests/test_console_validation.py`. |
| Diagnosed defect and verification | Stage 8 defect F8-01 allowed conflicting scheduled appointments for the same practitioner at the same time. Rachel contributed to the repair and regression verification through PRs #27 and #28. Another defect, F8-02, prevented lookup of cancelled appointments; Novera corrected this through PR #26. Evidence: Stage 8 defect records and tests. |
| Shared store and session-state/query responsibilities | A shared `SmartCareDataStore` keeps patient, practitioner and appointment records consistent during one session. Services coordinate business rules, while pure query functions filter and sort appointment lists without modifying stored records. Evidence: `data_store.py`, `services.py`, `queries.py`. |
| What would break if session-state lookup/query responsibilities changed? | Separate stores could make newly registered records unavailable to other services. If queries modified stored appointments, filtering and ordering could accidentally change application data or retained history. Keeping these responsibilities separate protects consistency. |
| Why cancellation is domain behaviour / conflict coordination is service behaviour | Cancellation changes the state of an individual appointment, so it belongs to the appointment domain object. Booking conflicts require checking other appointments and coordinating the data store, so they belong in the service layer. Evidence: `domain.py`, `services.py`. |
| FR-07 retained history test | `test_cancelled_appointment_is_retained_and_findable` verifies that an appointment remains retrievable after cancellation and has status CANCELLED. It checks lookup and retained object identity, while practitioner listing is covered separately. Evidence: `project/tests/test_starter.py`; Stage 8 PR #26. |
| Actual AI change rejected/modified or honestly accepted with verification | Copilot suggested additional menu framework classes and persistent storage. The team rejected these because they were unnecessary for the undergraduate session-only requirements. Copilot also produced outdated feedback about query implementation, which was checked against the current source. Evidence: Stage 9 Section E; Stage 12 Section E. |
| Unresolved limitation / future production work | The application does not persist data, support rescheduling, handle concurrency or manage time zones. A production version would also need authentication, access controls and stronger operational safeguards. These are outside the current undergraduate scope. Evidence: `project/README.md`; Stage 12 Section G. |
| Personal implementation contribution | **Merlin:** Implemented FR-03 practitioner lookup and tests (PR #5), contributed practitioner domain/service tests (PR #20), improved booking validation (PR #30), and implemented Stage 9 pure appointment queries with 12 tests (PR #38). **Rachel:** Implemented FR-02 patient lookup (PR #3), contributed to the F8-01 booking conflict repair (PR #27), and implemented practitioner appointment listing (PR #40). **Tarnima:** Contributed appointment validation and construction (PRs #15 and #18) and implemented the interactive console (PR #41). **Novera:** Implemented appointment cancellation (PR #14), repaired cancelled-appointment lookup (PR #26), and contributed console validation tests (PR #44). |
| Personal test/review/design/integration contribution | **Merlin:** Reviewed and tested practitioner lookup, booking validation and pure queries; completed Stage 12 Sections A, B and I; verified a fresh clone using Python 3.14.3 with 157 passing tests (Issue #51); corrected README and release evidence. **Rachel:** Contributed patient lookup and booking regression tests, reviewed code quality and responsible-AI evidence, and completed Stage 12 Sections C, E and H, including 157 passing tests at `d14685d` (Stage 12 PR #53). **Tarnima:** Contributed validation and regression tests, demonstrated console workflows, and completed Stage 12 Sections D, J and M. **Novera:** Contributed cancellation-history and console validation tests, reviewed the F8-01 repair, supported Stage 9 integration, and completed Stage 12 Sections F and G. |
| PG agentic change and rescheduling verification | Not applicable. All four members follow the undergraduate pathway; PG-only rescheduling requirements are excluded. |
| PG responsible-AI risk/remediation or supported no finding | Not applicable. PG-only responsible-AI assurance requirements are excluded from the undergraduate release. |

Optional bounded-change practice only: validation rule, focused test, safe error-message change, explicit-input query or agreed status rule with test. Explain expected impact before editing, make a small change, run the test, and identify evidence to inspect if unsure. No live AI unless explicitly permitted. Preserve the submitted candidate.

Practice question/change and reasoning: not undertaken

Separate reflection / peer / common team viva evidence links and routing: This Section N records the shared reflection and viva preparation. Individual peer assessments and common team viva evidence will be submitted separately according to the confirmed assessment instructions. Final submission arrangements are confirmed.
No further coding stage. Later corrections use the published assessment process.
