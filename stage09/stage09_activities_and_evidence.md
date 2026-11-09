# Stage 9 activities and evidence

Common UG and PG record. All Assignment 3 stage materials are provided from the beginning. Complete this stage only after the previous applicable stage has been integrated, verified and recorded. Use this supplied record in stage09/ in your EXISTING repository. Preserve project/, all earlier tests, records and responses. Do not download another starter or copy staff solutions. Use the Stage 9 handout and Overview/revision 2 baseline. Keep responses concise and link accessible artefacts; do not paste entire logs or private peer ratings.

Group: <!-- complete -->
Members and responsibilities: <!-- complete -->
Stage 8 integrated SHA, command, working directory and actual result: 
- Stage 8 integrated SHA: 253a2d3
- Command: python -m pytest -q
- Working directory: project/
- Actual result: 113 passed

## A. Tutorial activities

### A1 Session state classification

| Information | Required session/domain or transient state? | Requirement or reason |
|---|---------------------------------------------|-----------------------|
| Patient identity | Required domain/session state               | Identifies patients for registration, lookup and appointments.                      |
| Appointment history |  Required domain/session state                                   | Keeps appointments available for lookup, including cancelled ones.                      |
| Temporary menu choice | Transient state                                            | Only needed to process the current menu action.                      |
| Practitioner specialty | Required domain/session state                                    | Part of the practitioner's registered information.                      |
| Debug print output |  Transient state                                           |Only used for debugging; not part of stored records.                       |
| Appointment status | Required domain/session state                                            | Tracks whether an appointment is SCHEDULED, CANCELLED or COMPLETED.                      |

What is intentionally lost on exit? 

All patient, practitioner and appointment records created during the console session are lost when the program exits because Stage 9 does not use persistent storage. Temporary menu inputs and printed output are also not saved.

### A2 Interface and domain data plan

Plan before AI. This replaces schema/key design; no database tables are required.

| Function or component | Explicit inputs and types | Outputs          | Responsibility and validation | Domain source / existing constraint |
|---|---|------------------|---|---|
| appointment_sort_key |appointment: Appointment | tuple[datetime, str] |Returns date/time and appointment ID for sorting. Does not change data. |Uses Appointment.date_time and appointment_id. |
| select_appointments |appointments: list[Appointment], practitioner_id: str, status: AppointmentStatus \| None | list[Appointment] |Filters by practitioner and optional status, then returns a new sorted list. No mutation or I/O. |Uses existing Appointment properties and AppointmentStatus. |
| Service listing |practitioner_id: str, status: AppointmentStatus \| None | list[Appointment]|Validates practitioner and status, gets appointments from the store and calls select_appointments. |Uses registered practitioners and existing stored appointments. |
| Console |User menu choice and entered IDs, names, dates and status values | Printed results or error messages |Handles user input/output, converts inputs and calls services. Does not implement domain rules. |Uses existing Patient, Practitioner, Appointment and service contracts. |

Relate patient ID/name, practitioner ID/name/specialty, and appointment ID/actual participants/date_time/status to the existing contracts:  

Patient ID and name identify each patient. Practitioner ID, name and specialty identify each practitioner. An appointment has its own ID and links to actual Patient and Practitioner objects, along with its date/time and status. Stage 9 reuses these existing domain contracts instead of creating new data structures or a database.

### A3 Responsibility violations

| Conceptual case | Violation | Correct boundary and reason |
|---|---|---|
| Appointment.cancel reads input |Domain object handles user input. |The console should read input. Appointment.cancel() should only check and change appointment status. |
| Service prints/reads the menu |Service mixes business logic with user interaction. |The console handles menus and printing. Services coordinate operations and validation. |
| Query sorts its source in place |Changes the original list and breaks the pure-query requirement. |The query should use sorted() to return a new list without changing the original. |
| Store prints Appointment saved |Data store handles output instead of just storing data. |The store should save and retrieve objects. The console should display confirmation messages. |

### A4 Sorting comparison

For `appointments.sort(key=appointment_sort_key)` and `result = sorted(appointments, key=appointment_sort_key)`, predict source order, return value and result identity. Give a meaningful mutation check:
- sort(): Changes the source list order directly. It returns None and keeps the same list object.

- sorted(): Keeps the source list order unchanged and returns a new sorted list with a different list identity. The Appointment objects inside are still the same objects.

- Mutation check: Save the original list order and appointment fields before calling the query. Afterwards, check that the source order and fields are unchanged and the result is a different list object.

Score-example prediction and explanation of passing the named key: 

If appointments have different date/times, the earlier one comes first. If two appointments have the same date/time, the smaller appointment ID comes first. The named key appointment_sort_key returns (date_time, appointment_id), so Python sorts using both values. We pass key=appointment_sort_key without () because Python calls the function for each appointment during sorting. For example, if the scores are [85, 60, 95, 70], using sort() changes the original list to [60, 70, 85, 95] and returns None. Using sorted() creates a new sorted list without changing the original scores.

### A5 Exit question

Explain cancellation versus deletion, and checks for same-session lookup, all-status listing and SCHEDULED-only exclusion:

Cancelling an appointment changes its status from SCHEDULED to CANCELLED, but deleting would remove the appointment from the records. SmartCare keeps cancelled appointments to preserve appointment history.

To verify this, cancel an appointment and check that:
1. It can still be found using its appointment ID in the same session.
2. It appears in the practitioner's all-status appointment list.
3. It does not appear when filtering for SCHEDULED appointments.

This confirms that cancellation preserves history while removing the appointment from scheduled results.

## B. Human design and contracts

Complete before GitHub Copilot. Record any interface/integrity decision and its reasoning: 
- We will reuse the existing SmartCare domain classes, data store, and services rather than creating new structures. The query functions will filter and sort appointments without modifying the original list or objects. The service will validate practitioner IDs and statuses before calling the query. The console will handle user input, output, and errors while using the same data store throughout the session. This keeps responsibilities separate and preserves appointment history.

| Requirement | Input / session data | Operation and responsible component | Expected result or error | Test / evidence |
|---|---|---|---|---|
| QRY-01 | Appointment list and practitioner ID | `select_appointments()` filters by practitioner | Only that practitioner's appointments are returned | Test with appointments from two practitioners |
| QRY-02 | Appointment list and optional `AppointmentStatus` | `select_appointments()` filters by status | `None` returns all statuses; an enum value returns matching appointments | Test SCHEDULED, CANCELLED, COMPLETED and `None` |
| QRY-03 | Appointments with different and equal date/times | `appointment_sort_key()` and `select_appointments()` sort results | Earlier appointments first; equal times sorted by appointment ID | Test chronological order and equal-time tie-break |
| QRY-04 | Registered practitioner ID and optional status | `AppointmentService.list_practitioner_appointments()` validates and retrieves appointments | Sorted list; unknown ID raises `LookupError`, invalid ID/status raises `ValueError` | Test known, unknown, invalid and empty practitioner cases |
| FP-01 | Original appointment list and objects | `select_appointments()` must not modify its inputs | Original list order and appointment fields remain unchanged | Compare source order and fields before and after |
| FP-02 | Same appointment list, practitioner ID and status | Repeated calls to `select_appointments()` | Same results every time with no side effects | Call twice and compare results and source data |
| FP-03 | Empty, already-sorted and unsorted appointment lists | `select_appointments()` returns a new sorted list | Result is a different list object, even when empty | Check `result is not appointments` for each case |
| UI-01 | Menu choices 0–8, user inputs and shared session data | Console calls the existing services using one shared store | Registration, lookup, booking, cancellation and listing work until exit | Automated workflow tests and interactive menu demonstration |
| UI-02 | Invalid menu choices, IDs, dates and statuses | Console catches expected errors and returns to the menu | Clear error message, no crash and unchanged stored data | Invalid-input tests followed by a successful operation |
| FR-01–FR-03 | Patient and practitioner registration details and lookup IDs | Existing domain classes, store and services handle registration and lookup | Valid participants are registered and found; duplicate or invalid data is rejected | Existing registration and lookup tests |
| FR-04–FR-05 | Patient ID, practitioner ID, appointment ID and date/time | Appointment service books appointments and checks practitioner conflicts | Valid booking succeeds; same practitioner at the same time is rejected | Existing booking and conflict tests |
| FR-06–FR-07 | Appointment ID and current status | Appointment service cancels through the domain object and retains history | SCHEDULED becomes CANCELLED; repeated or invalid cancellation is rejected without deleting history | Existing cancellation and history tests |
| FR-08–FR-09 | Appointment ID, practitioner ID and optional status | Appointment lookup service and new practitioner listing service retrieve records | Known appointments can be found; practitioner listing returns matching appointments in sorted order | Existing lookup tests and new listing tests |

Cover QRY-01–04, FP-01–03, UI-01–02 and relevant FR-01–09. Explain empty versus unknown versus invalid, enum conversion, actual object identity, error handling and unchanged state on rejection: 

An empty result means the practitioner exists but has no matching appointments, so the service returns `[]`. An unknown practitioner ID means no registered practitioner was found, so the service raises `LookupError`. An invalid ID, such as a blank value, or an invalid status raises `ValueError`.

The console converts valid status input into an `AppointmentStatus` enum before passing it to the service. The query returns a new list, but the Appointment objects inside remain the same objects as those in the original list. It does not create copies or modify their fields.

The console catches expected errors, displays a clear message and allows the user to try again. Rejected operations must leave the stored records unchanged, including appointment statuses and cancellation history.

## C. Implementation and query verification

| Requirement / test ID   | Code location                                   | Case and meaningful assertion | Actual result | Evidence link |
|-------------------------|-------------------------------------------------|---|---|--|
| QRY-03 / TEST-QRY-01    | `smartcare/queries.py`, `tests/test_queries.py` | Sorting key returns `(date_time, appointment_id)`. | PASS | [Query tests](../project/tests/test_queries.py) |
| QRY-01 / TEST-QRY-02    | `smartcare/queries.py`, `tests/test_queries.py` | Returns only appointments for the requested practitioner. | PASS | [Query tests](../project/tests/test_queries.py) |
| QRY-02 / TEST-QRY-03    | `smartcare/queries.py`, `tests/test_queries.py` | CANCELLED filter excludes SCHEDULED appointments. | PASS | [Query tests](../project/tests/test_queries.py) |
| QRY-03 / TEST-QRY-04    | `smartcare/queries.py`, `tests/test_queries.py` | Sorts appointments in chronological order. | PASS | [Query tests](../project/tests/test_queries.py) |
| QRY-03 / TEST-QRY-05    | `smartcare/queries.py`, `tests/test_queries.py` | Equal-time appointments are ordered by appointment ID. | PASS | [Query tests](../project/tests/test_queries.py) |
| FP-01 / TEST-QRY-06     | `smartcare/queries.py`, `tests/test_queries.py` | Original list order remains unchanged; returned list is new and contains the original objects. | PASS | [Query tests](../project/tests/test_queries.py) |
| QRY-01 / TEST-QRY-07    | `smartcare/queries.py`, `tests/test_queries.py` | Returns an empty list when no practitioner appointments match. | PASS | [Query tests](../project/tests/test_queries.py) |
| QRY-02 / TEST-QRY-08    | `smartcare/queries.py`, `tests/test_queries.py` | Default status filter includes scheduled and cancelled appointments. | PASS | [Query tests](../project/tests/test_queries.py) |
| FP-03 / TEST-QRY-09     | `smartcare/queries.py`, `tests/test_queries.py` | Empty input produces a separate empty list. | PASS | [Query tests](../project/tests/test_queries.py) |
| FP-02 / TEST-QRY-10     | `smartcare/queries.py`, `tests/test_queries.py` | Repeated calls return consistent results and separate lists. | PASS | [Query tests](../project/tests/test_queries.py)|
| QRY-02 / TEST-QRY-11    | `smartcare/queries.py`, `tests/test_queries.py` | Every enum status filters correctly; default includes all statuses. | PASS | [Query tests](../project/tests/test_queries.py) |
| FP-03 / TEST-QRY-12     | `smartcare/queries.py`, `tests/test_queries.py` | Already-sorted input returns a fresh list containing the same appointment objects. | PASS | [Query tests](../project/tests/test_queries.py) |
| Regression verification | `project/tests/` (full test suite) | `python -m pytest -q` | 125 passed in 0.22s | Local pytest output |
| QRY-04 / TEST-SVC-01 | `smartcare/services.py`, `tests/test_services.py` | Registered practitioner returns their stored appointment. | PASS | [Service tests](../project/tests/test_services.py) |
| QRY-04 / TEST-SVC-02 | `smartcare/services.py`, `tests/test_services.py` | Registered practitioner with no appointments returns an empty list. | PASS | [Service tests](../project/tests/test_services.py) |
| QRY-04 / TEST-SVC-03 | `smartcare/services.py`, `tests/test_services.py` | Unknown practitioner raises `LookupError` without changing stored appointments. | PASS | [Service tests](../project/tests/test_services.py) |
| QRY-04 / TEST-SVC-04 | `smartcare/services.py`, `tests/test_services.py` | Blank practitioner ID raises `ValueError`. | PASS | [Service tests](../project/tests/test_services.py) |
| QRY-04 / TEST-SVC-05 | `smartcare/services.py`, `tests/test_services.py` | Invalid practitioner ID (`None`) raises `ValueError`. | PASS | [Service tests](../project/tests/test_services.py) |
| QRY-04 / TEST-SVC-06 | `smartcare/services.py`, `tests/test_services.py` | Invalid appointment status raises `ValueError` without changing appointment status. | PASS | [Service tests](../project/tests/test_services.py) |
| QRY-02 / TEST-SVC-07 | `smartcare/services.py`, `tests/test_services.py` | CANCELLED filter returns only cancelled appointments. | PASS | [Service tests](../project/tests/test_services.py) |
| QRY-02 / TEST-SVC-08 | `smartcare/services.py`, `tests/test_services.py` | Default listing includes scheduled and cancelled appointments, preserving history. | PASS | [Service tests](../project/tests/test_services.py) |
| QRY-04 / TEST-SVC-09 | `smartcare/services.py`, `tests/test_services.py` | Listing appointments for D1 excludes appointments belonging to D2. | PASS | [Service tests](../project/tests/test_services.py) |
| QRY-02 / TEST-SVC-10 | `smartcare/services.py`, `tests/test_services.py` | SCHEDULED filter returns only scheduled appointments and excludes cancelled appointments. | PASS | [Service tests](../project/tests/test_services.py) |
| Final service regression verification | `project/tests/` | `python -m pytest -q` | 135 passed | Local pytest output |

Include practitioner isolation, every enum status/default all, equal-time ID tie-break, named-key reuse, repeated calls, empty/already-sorted fresh lists, unchanged source order/fields, known-empty/unknown/invalid service cases and retained history.

Purity explanation from code inspection, including absence of hidden state and I/O: 

The two functions in `smartcare/queries.py` are pure collection-processing functions. `appointment_sort_key()` returns the appointment date/time and appointment ID as a tuple. `select_appointments()` filters appointments using a list comprehension and returns a new list using `sorted()` with the named sorting key. Neither function changes the original list or appointment objects. Code inspection shows no global mutable state, data-store access, printing, user input, file operations, or other I/O. The results depend on the supplied appointments and parameters.

What the tests do and do not establish: 

The 12 query tests verify practitioner isolation, filtering by all three appointment statuses, default inclusion of all statuses, chronological sorting, appointment ID tie-breaking, empty results, repeated calls, and returning fresh lists without changing the original list order. Code inspection also confirms that `select_appointments()` reuses the named sorting key.

The full regression suite passed with 125 tests. However, the tests do not prove that every possible input is handled correctly or independently verify that every appointment field remains unchanged. Service-level validation for known-empty, unknown, and invalid practitioner IDs must be verified separately. Retained cancellation history also needs service or integration evidence.

## D. Integrated console and workflow evidence

| Scenario / acceptance ID | Reproducible inputs / artefact | Expected result | Observed result and state check | Evidence link |
|---|---|---|---|---|
| UI-01 full menu workflow (manual) | Run `python main.py --interactive` from `project/` on 9 Nov 2026 (branch `test/stage09-console-validation`, commit 7cdc625; console code unchanged from integration `b13eddd`). Register P1 (Alex), DR1 (Taylor), P2 (Sam), DR2 (Lee); find P1 and DR1; book A1 (P1, DR1, 2026-11-20 09:00); try A2 (P2, DR1, same time); book A2 with DR2 at the same time; cancel A1; find A1; list DR1's appointments with blank, `scheduled` and `cancelled`; book A3 (P2, DR1) in the freed slot; exit with 0. | Registration, lookup, booking and cancellation work in one shared session. Same-practitioner double-booking is rejected; a different practitioner at the same time is allowed. Cancelled A1 stays findable and listable, and its slot can be booked again. | PASS. A1 booked as scheduled; A2 for DR1 rejected with `Error: Practitioner already has a SCHEDULED appointment at this time`; A2 for DR2 booked. A1 cancelled and still found with status cancelled. Blank listing and `cancelled` listing showed A1; `scheduled` listing showed `No matching appointments found.` A3 was booked into the freed slot. Exit printed the session-only message. | [Manual transcript](https://github.com/u3325845/st1-assignment-3/pull/44#issuecomment-6730481905), [Workflow tests](../project/tests/test_workflows.py) |
| UI-02 invalid-input recovery (manual) | In the same session: menu choice `99`; blank patient ID; duplicate patient P1; date `not-a-date`; date `2026-02-30 09:00`; find unknown A9; cancel A1 again; status filter `archived`; then find P1 and exit. | Each invalid input shows a clear error, the menu returns, stored data is unchanged, and a later valid operation succeeds. | PASS. `Invalid menu option. Please choose 0-8.`; `Error: Patient ID cannot be blank`; `Error: Patient ID already exists`; `Error: Use date/time format YYYY-MM-DD HH:MM`; `Error: Invalid calendar date/time; use YYYY-MM-DD HH:MM`; `Error: Appointment not found`; `Error: Only SCHEDULED appointments may be cancelled`; `Error: 'archived' is not a valid AppointmentStatus`. After the errors, `Find patient P1` still returned `P1 - Alex`. One earlier booking attempt with mistyped input (wrong ID and unknown patient) produced `Error: Patient not found` and stored nothing; it was an accidental entry, not a planned step. | [Manual transcript](https://github.com/u3325845/st1-assignment-3/pull/44#issuecomment-6730481905), [Console validation tests](../project/tests/test_console_validation.py) |
| Automated console validation (UI-02) | `python -m pytest -q tests\test_console_validation.py` and `python -m pytest -q` from `project/` at commit 7cdc625. 16 tests cover bad menu choices, blank/duplicate/unknown IDs, malformed and impossible dates, invalid status, double-booking, repeated cancellation, freed slot and unknown practitioners. | Errors are handled without crashing; rejected operations leave stored data unchanged; the menu continues. | PASS. Focused: 16 passed. Full suite: 157 passed. | [Console validation tests](../project/tests/test_console_validation.py), https://github.com/u3325845/st1-assignment-3/pull/44#issuecomment-6730481905 |

Include registration/find, booking, conflict rejection, different-practitioner booking, cancellation, retrieval, listing/filtering, freed slot and exit; duplicate/unknown/blank IDs, malformed/impossible date, invalid status, unknown choice and repeated cancellation. Identify before/after state and subsequent successful action.

## E. GitHub Copilot review and human decisions


Human design completed before AI: Section B, Human design and contracts.
Actual prompt/context supplied: Asked GitHub Copilot to review the proposed `run_menu()` design using one shared `SmartCareDataStore`, existing services, menu options 0–8, `parse_date_time()`, `format_appointment()`, optional `AppointmentStatus` filtering and expected error recovery. Requested essential versus optional suggestions without code generation.
Actual response: Copilot supported the shared-store design, separation of console and service responsibilities, date parsing, appointment formatting and expected error handling. It recommended testing session continuity, invalid-input recovery and appointment listing. It also flagged unfinished query and service dependencies, although the query functions had already been integrated. Additional framework classes and persistence were unnecessary.


| AI finding | Code/test evidence | Severity | Accept/Modify/Reject and reason | Change or no change | Actual verification                                                                                                                              |
|---|---|---|---|---|--------------------------------------------------------------------------------------------------------------------------------------------------|
| Shared session data store | `smartcare/console.py`, `tests/test_workflows.py` | Essential | Accept — one shared store preserves records between menu operations without persistence. | Created one `SmartCareDataStore` and reused it across all three services in `run_menu()`. | Registration followed by lookup passed in the automated workflow tests.                                                                          |
| Separation of responsibilities | `smartcare/console.py`, `smartcare/services.py` | Essential | Accept — the console should handle input/output while existing services enforce business rules. | Used service methods for registration, lookup, booking and cancellation instead of duplicating domain logic in the console. | Six automated workflow tests passed, full regression suite passed with 141 tests.                                                                |
| Input validation and error recovery | `smartcare/console.py`, `tests/test_workflows.py` | Essential | Accept — invalid inputs should display an error without terminating the session. | Caught expected `ValueError` and `LookupError` exceptions and displayed an error message before returning to the menu. | Invalid menu choice recovery passed in automated tests. Malformed date, unknown records, invalid status and repeated cancellation were manually verified. |
| Query and service dependencies | `smartcare/queries.py`, `smartcare/services.py`, `tests/test_workflows.py` | Essential | Modify — Copilot reviewed an older commit and incorrectly identified the query functions as unfinished. The queries were already integrated, while Rachel's listing service was integrated later. | Reused the existing query functions and merged Rachel's practitioner listing service into the console branch without duplicating functionality. | Manual console listing and status filtering passed. The automated listing workflow test passed, and the full regression suite passed with 141 tests. |
| Unnecessary complexity | `smartcare/console.py`, `project/README.md` | Optional | Reject — additional menu framework classes and persistent storage are outside the Stage 9 requirements. | Used a simple `run_menu()` loop with the existing services and session-only data store. No additional framework or persistence was introduced. |  Code inspection confirmed the simple session-based implementation. The full regression suite passed with 141 tests.                             |


Responsibility check: explain how domain invariants, shared-store collections, service coordination, pure queries and console effects remain separate:

The domain classes enforce appointment rules and status changes. The shared data store manages patient, practitioner and appointment collections. Services coordinate registration, lookup, booking, cancellation and listing. Pure query functions filter and sort appointments without modifying stored data. The console handles user input, output, date and status conversion, and expected errors. This separation avoids duplicating business rules and keeps session data consistent.


## F. Required reflections

1. Which integration concern was architectural rather than a filtering/sorting detail?

The main architectural concern was maintaining one shared data store and keeping responsibilities separate. The console reuses the store across menu operations, services coordinate and validate actions, and pure query functions handle filtering and sorting without changing stored data.

2. Which Copilot suggestion did you reject as over-engineering, and why?

For the console review, I rejected additional menu framework classes and persistent storage because Stage 9 only requires session-based interaction. For the service review, Rachel accepted the suggested practitioner isolation and SCHEDULED filtering tests because they directly verified the requirements.

3. How did you prove cancelled appointments remain retrievable and listable in the same session?

The console workflow booked appointment A1, cancelled it and retrieved it again, confirming that its CANCELLED status was retained. I then listed DR1's appointments without a status filter and confirmed that A1 still appeared. Filtering by SCHEDULED returned no matching appointments, while filtering by CANCELLED returned A1. Rachel's service tests and my automated console workflow test also verified this behaviour. The full regression suite passed with 141 tests.


## G. Ten formative answers

1. What makes select_appointments pure, and what side effect breaks purity? <!-- response -->
2. Which explicit inputs are needed, and why avoid a global store? <!-- response -->
3. How can a new list reuse Appointment objects safely? <!-- response -->
4. Why use a named key, and what breaks equal-time ties? <!-- response -->
5. How do default and explicit status filters differ? <!-- response -->
6. How do empty, unknown practitioner and invalid filter cases differ? <!-- response -->
7. Which console errors recover, and how is unchanged state checked? <!-- response -->
8. What is data integrity for registered participants, conflicts and history? <!-- response -->
9. What is Copilot's review role, and who verifies findings? <!-- response -->
10. How do pure functions and OOP responsibilities work together? <!-- response -->

## H. Review, completion and common handover

Issues and bounded branches: Stage 9 console implementation and workflow tests were developed on `feature/stage09-console`, based on `stage09/integration`. Merlin's query implementation and Rachel's practitioner listing service were merged into the console branch. The local merge commit is `53a00e8`.
PR/diff and another-member human reviewer: 
Review responses and Copilot comparison: GitHub Copilot reviewed the proposed console design before implementation. I accepted its recommendations on shared session data, separation of responsibilities, error recovery and workflow testing. I rejected additional menu framework classes and persistent storage because they were unnecessary for Stage 9. The review findings and decisions are recorded in Section E.
Integrated common Stage 9 SHA: 
Full regression command, working directory, actual count/result and evidence: `python -m pytest -q` from `project/` — 141 passed in 0.18s. Evidence: [Workflow tests](../project/tests/test_workflows.py) and local pytest output.
README run instructions and scope/limitations: [Project README](../project/README.md). The console runs using `python main.py --interactive` and supports registration, lookup, booking, cancellation and practitioner appointment listing. Records remain in memory and are lost when the session ends.
Unresolved issues and support/action:
UG common candidate / PG future branch plan:

- [x] Query contracts, purity, new lists and named-key ordering verified.
- [x] Service empty/unknown/invalid cases and cancellation history verified.
- [ ] Every console command and invalid-input recovery demonstrated.
- [x] Query and workflow tests plus all previous tests pass; actual evidence linked.
- [ ] Human design, Copilot critique, review and integration recorded honestly.
- [ ] Reflections and ten formative responses completed.
- [x] README updated; earlier code/tests/records preserved.
- [ ] Common SHA protected for UG Stage 12; PG Stage 10/11 work deferred until approved.

No persistence, rescheduling or assurance implementation is part of Stage 9. UG: 6→7→8→9→12. PG: 6→7→8→9→10→11→12. Mixed groups keep one repository and protect the common candidate.
