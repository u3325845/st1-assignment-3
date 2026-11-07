# Stage 8 activities and evidence

UG and PG | One evolving group project | Complete this blank record using the Stage 8 handout.

All Assignment 3 stage materials are provided from the beginning. Complete this stage only after the previous applicable stage has been integrated, verified and recorded. Use this supplied record in stage08/ in your EXISTING repository. Preserve project/, all earlier tests, records and responses. Do not download another starter or copy staff solutions. The Stage 8 preparation utility is supplied or run by teaching staff when Stage 8 begins. Follow your tutor’s controlled workflow and the handout. If temporarily supplied, keep it outside the repository in a sibling Stage_8_Assets/ folder; exclude it from Git and the final submission.

Group/tutorial: Grp 2 tutorial Wed 4:30 - 6:30
Members and UG/PG cohorts: RachelUC, Merlin3313611, TarnimaKhan22, u3325845 (Novera)
Record owner / contribution links for each member:

Rachel – F8-01 practitioner conflict repair: https://github.com/u3325845/st1-assignment-3/pull/27

Novera – F8-02 cancelled appointment lookup repair: https://github.com/u3325845/st1-assignment-3/pull/26

Merlin – AppointmentService refactoring: https://github.com/u3325845/st1-assignment-3/pull/30

Tarnima – Refactoring PR #30 review and Stage 8 regression verification and documentation: https://github.com/u3325845/st1-assignment-3/pull/30 and https://github.com/u3325845/st1-assignment-3/pull/31

Use concise results and accessible artefact links rather than copying entire logs. Keep human-first entries before consulting GitHub Copilot. Link shared evidence once; do not repeat it across sections. No entries below are specimen answers or claimed results.

## A. Tutorial activities

### A.1 Classify all five statements
For each, choose symptom, evidence or hypothesis/opinion, and explain your reason. These are discussion statements, not confirmed diagnoses.
- Appointment disappears after cancellation.
- The data-store removal path is probably being called.
- The failing test shows store.find_appointment('A1') returns None.
- The service layer is badly designed.
- Traceback points to smartcare/services.py line 42 in the example.
The example line number is illustrative; inspect the actual line in your run. The removal hypothesis must be tested against the current project, which has no public delete operation.

Response and reason:

1. Appointment disappears after cancellation.

Classification: Symptom.

Reason: This describes the problem noticed by the user, but it does not explain why the appointment disappeared.

2. The data-store removal path is probably being called.

Classification: Hypothesis.

Reason: This is a possible explanation for the problem, but it needs to be checked against the code. The current project does not have a public delete operation.

3. The failing test shows store.find_appointment('A1') returns None.

Classification: Evidence.

Reason: This is an observed test result that can help investigate the failure.

4. The service layer is badly designed.

Classification: Opinion.

Reason: This is a judgement about the code without enough evidence to support it.

5. Traceback points to smartcare/services.py line 42 in the example.

Classification: Evidence.

Reason: The traceback shows where the failure was reported. However, line 42 is only an example and does not prove the root cause.



### A.2 Build a debugging record
Choose the cancelled-history scenario or a same-practitioner/time booking. Before changing code, record expected behaviour, observed behaviour, minimal reproduction, a hypothesis and evidence to inspect. Use a requirement to justify the expectation. Keep the initial hypothesis even if later evidence disproves it.

Response and reason:

Scenario: Cancelled appointment history is not retained.

Expected behaviour: According to FR-07, cancelling an appointment should change its status while keeping the appointment record available for future lookup.

Observed behaviour: The failing test showed that a cancelled appointment could not be found using the lookup operation.

Minimal reproduction: Create an appointment, cancel it, and attempt to retrieve it using its appointment ID.

Initial hypothesis: The cancellation process may be removing the appointment or preventing the lookup method from returning cancelled records.

Evidence to inspect: The failing test, cancellation service method, appointment lookup method, data-store code and FR-07 requirements.

Reason: Recording the expected and observed behaviour before changing code helps the team investigate the actual problem instead of guessing.

### A.3 Test defect or product defect
A test expects cancelled appointments to be deleted, but FR-07 says history must be retained. What should be changed? Explain why. Also decide whether a test expecting different practitioners at the same time to conflict reflects AC-04.2. Do not assume every failing test is correct.

Response and reason:
1. A test expects cancelled appointments to be deleted, but FR-07 requires history to be retained.

Response: The test should be corrected because it contradicts FR-07. Cancelled appointments must remain stored and available for lookup. The expected result should check that the appointment is retained with its cancelled status.

2. A test expects different practitioners at the same time to conflict.

Response: The test should be corrected if AC-04.2 defines conflicts for the same practitioner and time. Different practitioners should be able to have appointments at the same time, provided the other booking rules are satisfied.

Reason: Tests should follow the actual requirements. A failing test does not automatically mean the application code is wrong.

### A.4 Refactoring smell hunt
Consider a hypothetical 70-line AppointmentService method containing duplicate status strings, direct collection manipulation, printing, validation and four nested conditionals. Identify the smells and propose small refactorings that preserve required behaviour. The direct collection work replaces the old storage-specific scenario; use the existing SmartCareDataStore boundary. Do not implement an extra architecture.
Classify these proposed changes as refactoring, repair or feature: rename appt to appointment; extract a repeated conflict helper; add rescheduling; restore retained cancellation lookup; replace a magic status string with the existing enum. Explain the behaviour that must remain unchanged.

Response and reason:

Code smells identified in the hypothetical 70-line AppointmentService method:

Long method: The method handles too many responsibilities, making it difficult to read and maintain.

Duplicated status strings: Repeated status values can cause inconsistencies and make updates harder.

Direct collection manipulation: The service directly accesses collections instead of using the existing SmartCareDataStore boundary.

Printing inside service logic: Mixing output statements with business logic makes the code harder to test.

Deep nesting: Four nested conditionals make the code complicated and difficult to follow.

Proposed small refactorings:

Extract repeated validation and conflict-checking logic into private helper methods.

- Replace repeated status strings with the existing status enum.

- Move direct collection operations behind the existing SmartCareDataStore methods.

- Separate printing from the service logic.

- Simplify nested conditions using clearer checks and early returns where appropriate.

Classification of proposed changes:

Rename appt to appointment: Refactoring - improves readability without changing behaviour.

Extract a repeated conflict helper: Refactoring - reduces duplicated code while keeping the same conflict rules.

Add rescheduling: Feature - introduces new functionality.

Restore retained cancellation lookup: Repair - fixes incorrect behaviour so cancelled appointments remain available according to FR-07.

Replace a magic status string with the existing enum: Refactoring - improves consistency without changing the required status values.

Behaviour that must remain unchanged:

Existing booking rules, patient and practitioner validation, exception handling, conflict detection, appointment statuses and cancelled appointment history must continue working according to the requirements.

Reason:  Refactoring improves the internal code structure without changing external behaviour. A repair corrects an existing defect, while a feature adds new functionality.


### A.5 Traceback and hypothesis ranking
Using one actual failure, identify its exception/assertion, expected and observed values, test line, application call path and supporting requirement. List three plausible causes and rank them by fit with the available evidence. For each cause, name a check that could distinguish it from the others. Explain why a traceback alone does not establish the cause.

Response and reason:
Actual failure: F8-02 - cancelled appointment history is not findable.

Exception: LookupError: Appointment not found

Expected behaviour: After cancelling appointment A1, find_appointment("A1") should return the appointment with status CANCELLED.

Observed behaviour: SmartCareDataStore.find_appointment("A1") returned None, causing AppointmentService.find_appointment() to raise LookupError.

Failing test: project/tests/test_services.py::test_cancelled_appointment_is_retained_and_findable

Application failure location: smartcare/services.py, line 147.

Application call path: Test → AppointmentService.find_appointment() → SmartCareDataStore.find_appointment().

Supporting requirements: FR-06, FR-07, FR-08, BR-07 and AC-05.2.

Three possible causes, ranked:

Cancelled appointments are excluded by the data-store lookup - most likely.
Check: Inspect SmartCareDataStore.find_appointment() for a status filter. The condition appointment.status.value != "cancelled" confirmed this cause.

The cancellation method removes the appointment from storage.
Check: Run list_appointments() after cancellation. The result [('A1', 'cancelled')] showed that A1 was still stored, disproving this hypothesis.

The test uses an incorrect appointment ID or setup.
Check: Verify that A1 was created successfully and that the same ID was used for cancellation and lookup.

Why the traceback alone is not enough:

The traceback identifies where the error occurred but does not prove its root cause. The team inspected the data-store code and runtime results to confirm that cancelled appointments were being filtered out during lookup.

Confirmed root cause and repair:

The condition appointment.status.value != "cancelled" incorrectly excluded cancelled appointments. Removing this condition restored the required lookup behaviour without changing the handling of unknown appointment IDs.

Repair evidence: Commit e7fad56, PR #26. Both focused F8-02 tests passed.


### A.6 Exit question
Why is changing code immediately after seeing a failure often a poor debugging strategy?

Response and reason: Changing code immediately can lead to incorrect fixes because the real cause may not be understood. Engineers should first reproduce the failure, examine the evidence, check the requirements and test possible causes. This helps avoid introducing new defects.


Classification responses (1–5, each with reason): Completed in Section A.1.
Tutorial debugging record — expected; observed; reproduction; hypothesis; evidence to inspect: Completed in Section A.2 using the F8-02 cancelled appointment scenario.
Traceback — exception/assertion; expected/observed values; test line; call path; requirement; ranked causes and discriminating checks: Completed in Section A.5 using F8-02. The exact test assertion line was not recorded; the application failure was reported at smartcare/services.py line 147.


## B. Stage 7 baseline and safe preparation

- Stage 7 code SHA and requirement baseline: `c384995f7ba8bf12679f59720700037b04411291`. Requirements baseline: SmartCare Assignment 3 Revision 2.
- Baseline test command / working directory / observed result / evidence: The Stage 7 baseline was identified by Git SHA `c384995`. The original baseline test result was not separately recorded during Stage 8 preparation. The prepared faulty-state test result is recorded below.
- Clean preparation SHA if a record-only commit followed Stage 7: No separate record-only commit was confirmed.
- Branch and preparer / how teammates obtained this branch: Rachel prepared and pushed `debug/stage08` to GitHub. Teammates can access it using `git fetch origin` and `git switch --track origin/debug/stage08`.
- Downloaded tool version, source SHA256 and --check outcome: Stage 8 preparation tool version 1.1. Script SHA256: `cd9a6786cd9fb518376716fb15a33be63ccbb80282600b453fbf6095b3754f30`. The `--check` command reported preflight PASS, verified both proposed faults in a temporary copy and left the project unchanged.
- --apply and --verify output summaries / artifact references: The `--apply` command introduced F8-01 (practitioner conflict) and F8-02 (retained-history lookup). The tool confirmed 2 expected failures. The `--verify` command later confirmed exactly 2 expected failures with both approved fault signatures present.
- Bounded diff inspected and recovery location (not committed): Compared the original and faulty versions of `project/smartcare/data_store.py`. The changes were limited to `find_appointment()` and `has_practitioner_conflict()`. The debugging tool saved backup and recovery information in `.stage8_faults`. Confirmed using `git ls-files` that these recovery files are not tracked by Git.
- Prepared faulty-state commit SHA: `ec3fc09` on `debug/stage08`, pushed to GitHub. Evidence: https://github.com/u3325845/st1-assignment-3/commit/ec3fc09
- Preparation or recovery issues and resolution, if any: The first verification attempt failed because the script path was incorrect. After locating the script in `Stage_8_Assets` outside the repository, verification completed successfully.
- Initial prepared full-suite command / result / key failures: Ran `python -m pytest -q` from the `project/` directory. Result: **110 passed, 3 failed (113 total)**. Two tests failed because cancelled appointments could not be found (`LookupError`). One practitioner conflict test failed because the expected `ValueError` was not raised. These three test failures relate to the two introduced faults.

## C. F8-01 diagnosis and repair

- Fault: F8-01 – Practitioner conflict.
- Branch: `fix/stage08-f8-01`.
- Starting SHA: `e6319d8`.
- Failing test: `tests/test_starter.py::test_conflict_rule_and_different_practitioner`.
- Command: `python -m pytest tests/test_starter.py::test_conflict_rule_and_different_practitioner -v`
- Working directory: `project/`.
- Expected behaviour: Booking another appointment for the same practitioner at the same date and time should raise `ValueError`.
- Observed behaviour: The expected `ValueError` was not raised.
- Result: 1 failed in 0.02s.
- Failure location: `tests/test_starter.py:127`.
- Supported root cause: The practitioner ID comparison in SmartCareDataStore.has_practitioner_conflict() incorrectly used != instead of ==. This prevented the system from detecting overlapping appointments for the same practitioner.
- Smallest justified repair: Changed the practitioner ID comparison from != to ==, restoring the required conflict detection without changing unrelated booking behaviour.
- Repair SHA / verification: `3c4ea3e`, PR #27. The focused test passed after the repair. At this checkpoint, the full suite had 111 passed and 2 failed (both related to F8-02). After both defects were repaired and integrated at SHA `8c70964`, the full suite passed with 113 tests.

## D. F8-02 diagnosis and repair

- Symptom / observed behaviour: After A1 is cancelled, the store's find_appointment("A1") returns None, so AppointmentService.find_appointment raises LookupError: Appointment not found. As a result, a second cancel_appointment("A1") also raises LookupError instead of ValueError.
- Expected behaviour and requirement: A cancelled appointment stays stored and findable with status CANCELLED, and a repeated cancellation is rejected with ValueError. Requirements: FR-06, FR-07, FR-08, BR-07 and AC-05.2 (cancelled appointments are retained as history and lookup still finds them).
- Minimal synthetic reproduction steps: (1) register patient P1 and practitioner D1;
(2) book A1 for P1 with D1 on 1 Oct 2026 at 09:00;
(3) cancel A1 with service.cancel_appointment("A1");
(4) look it up with service.find_appointment("A1");
(5) observe LookupError instead of the cancelled appointment.

- Meaningful failing test path/name and exact relevant failure: project/tests/test_services.py::test_cancelled_appointment_is_retained_and_findable fails with LookupError: Appointment not found at smartcare/services.py line 147. Related: test_cancel_already_cancelled_appointment_raises_value_error fails with the same LookupError.
- Human hypothesis and intended checks: see E, F8-02.
- Supported root cause and inspected code/runtime evidence: The condition `appointment.status.value != "cancelled"` in SmartCareDataStore.find_appointment skips cancelled appointments, so the loop ends and returns None. Evidence: the code in data_store.py; runtime check after booking and cancelling A1 printed [('A1', 'cancelled')] for list_appointments() and None for find_appointment("A1"); `git diff c384995 ec3fc09 -- project/smartcare/data_store.py` shows the prepared commit replaced the Stage 7 dictionary lookup with this filtering loop. This contradicts FR-07 and AC-05.2.
- Smallest justified fix / diff / why other behaviour is preserved: Removed `and appointment.status.value != "cancelled"` from the condition in SmartCareDataStore.find_appointment, a one-line change (1 insertion, 2 deletions). The ID check, the blank-ID ValueError and None for an unknown ID are unchanged, so lookup now finds a stored appointment whatever its status (FR-07, AC-05.2, FR-08).

- Repair SHA / focused verification result: e7fad56 on fix/stage08-f8-02 (PR #26). Focused: the two F8-02 tests pass (2 passed). Full suite: 112 passed, 1 failed (test_conflict_rule_and_different_practitioner, F8-01).

## E. Human-first hypotheses

Complete both entries BEFORE Copilot. C/D supply observed/expected/reproduction/test; retain those initial facts and link them here.

### F8-01 human entry

Likely cause and why plausible: The practitioner ID comparison in `has_practitioner_conflict()` uses `!=` instead of `==`. This checks different practitioners instead of the same practitioner, which explains why a conflicting booking is allowed.

Evidence intended to inspect / competing explanation / discriminating check: Inspected `has_practitioner_conflict()` in `data_store.py` and `test_conflict_rule_and_different_practitioner()` in `test_starter.py`. Another possible cause was an incorrect date/time or appointment status comparison. The test checks that two appointments for D1 at the same time should raise `ValueError`, while D2 should be allowed at the same time. The incorrect practitioner ID comparison is the most likely cause.

Member and saved sequence/time or commit showing this preceded consultation: Rachel – Initial F8-01 investigation saved in commit `8e07d5f`, before consulting GitHub Copilot.

### F8-02 human entry
Likely cause and why plausible: The store's find_appointment loops over the stored appointments but only returns an appointment if appointment.status.value != "cancelled". A cancelled A1 therefore fails the condition, the loop ends and the method returns None. This is plausible because the failure appears only after cancelling and only in lookup, and the condition contradicts FR-07 / AC-05.2.

Evidence intended to inspect / competing explanation / discriminating check: Inspect find_appointment, list_appointments and add_appointment in data_store.py. Competing explanation: the cancelled appointment is no longer in the store, or list_appointments() leaves it out. Discriminating check: book and cancel A1, then print list_appointments() and find_appointment("A1"). Result on 5 Nov 2026, 21:51: [('A1', 'cancelled')] and None. A1 is still stored but the lookup does not return it, so the competing explanation is not supported.
Member and saved sequence/time or commit showing this preceded consultation: Novera. Hypothesis committed on fix/stage08-f8-02 before consulting Copilot: e95806d. I identified the condition by reading the code and ran the check above before consulting Copilot.

## F. GitHub Copilot prompts, findings and human decisions

Use the full handout prompt separately for BOTH defects, after E. Keep each actual prompt or accessible reference; include observed behaviour, expected behaviour, reproduction, failing test, human hypothesis, relevant code, three ranked causes and discriminating checks, with the no-rewrite/no-invented-requirements constraints.


### F8-01 Copilot review

**Actual prompt / output reference and member:** Rachel used GitHub Copilot after recording the human-first hypothesis in commit `8e07d5f`. The investigation included the observed behaviour (double booking allowed), expected behaviour (`ValueError` for the same practitioner and time), reproduction using A1 and A2 for D1 at the same time, failing test `tests/test_starter.py::test_conflict_rule_and_different_practitioner`, initial hypothesis and relevant code in `has_practitioner_conflict()`. Copilot was asked for three ranked causes with supporting evidence and checks, without rewriting code or inventing requirements.

**Copilot conversation:** https://github.com/copilot/share/8a1b1200-0064-8025-b902-480c84f629b6

| Ranked suggestion                      | Evidence check | Observed evidence | Evaluation | Human decision and reason |
|----------------------------------------|---|---|---|---|
| 1. Incorrect practitioner comparison   | Inspect the `!=` comparison and rerun the focused test after correction. | The code used `!=`. Changing it to `==` made the focused test pass. | Correct | **Accept.** This confirmed the root cause. |
| 2. Booking service not handling conflicts | Check whether `book_appointment()` calls the conflict function and raises `ValueError`. | The focused test passed without changing the booking service. | Wrong as main cause | **Reject.** No booking service changes were needed. |
| 3. Datetime or status mismatch         | Compare booking times and check appointment status. | The test used the same datetime, and the one-line fix resolved the failure. | Wrong as main cause | **Reject.** The practitioner comparison caused the failure. |

Final human conclusion and comparison with initial hypothesis: My initial hypothesis was correct. The practitioner ID comparison used `!=` instead of `==`, which prevented the system from detecting double bookings for the same practitioner. Copilot's first suggestion supported my hypothesis, and the focused test passed after correcting the comparison.

### F8-02 Copilot review
Actual prompt / output reference and member: Observed behaviour:
After booking and then cancelling appointment A1, the data store's find_appointment("A1") returns None. AppointmentService.find_appointment then raises LookupError: Appointment not found. A second cancel_appointment("A1") also raises LookupError instead of ValueError.

Expected behaviour:
A cancelled appointment stays stored and findable with status CANCELLED (FR-07, AC-05.2: cancelled appointments are retained as history). Repeated cancellation should raise ValueError.

Steps to reproduce:
1. Register patient P1 and practitioner D1.
2. Book appointment A1 (P1, D1, 2026-10-01 09:00).
3. Cancel A1 with cancel_appointment("A1").
4. Look it up with find_appointment("A1").
5. LookupError: Appointment not found (services.py line 147).

Failing test:
tests/test_services.py::test_cancelled_appointment_is_retained_and_findable
LookupError: Appointment not found

My hypothesis:
The store's find_appointment skips cancelled appointments because of the condition appointment.status.value != "cancelled", so the loop ends and returns None. A competing explanation is that the cancelled appointment is no longer stored or list_appointments() leaves it out. My check printed list_appointments() after cancelling and got [('A1', 'cancelled')], while find_appointment("A1") returned None.

Relevant code:
def find_appointment(self, appointment_id: str) -> Appointment | None:
    if not isinstance(appointment_id, str) or not appointment_id.strip():
        raise ValueError("Appointment ID cannot be blank")
    for appointment in self.list_appointments():
        if (appointment.appointment_id == appointment_id.strip()
                and appointment.status.value != "cancelled"):
            return appointment
    return None

def list_appointments(self) -> list[Appointment]:
    return list(self._appointments.values())

Task:
Rank the three most likely causes. For each, identify
the evidence I should inspect to distinguish it from
the other possible causes.
Do not rewrite the entire application.
Do not invent requirements.
Treat all suggested explanations as hypotheses. Consulted 5 Nov 2026 in a separate Copilot chat for F8-02, after my hypothesis commit e95806d.
Chat link: https://github.com/copilot/share/02194300-0840-8080-8051-ce4dc4b049e8
1. Ranked suggestion / evidence check / observed evidence / correct, partly correct or wrong / accept, modify or reject with reason: Copilot: find_appointment filters out cancelled records, so the appointment is in list_appointments() but the status.value != "cancelled" condition stops it being returned; the second cancel then raises LookupError before appointment.cancel() can raise ValueError. Suggested check: inspect the ID and status at the loop and whether the ID matches. Observed evidence: the code in data_store.py contains `and appointment.status.value != "cancelled"`; my runtime check printed [('A1', 'cancelled')] for list_appointments() and None for find_appointment("A1"); the second-cancel test fails at services.py line 157 through the same failed lookup. Correct. Accept: it matches my hypothesis and the evidence.
2. Ranked suggestion / evidence check / observed evidence / correct, partly correct or wrong / accept, modify or reject with reason:  Copilot: the runtime is loading different code from the repository version it inspected (it described a plain dictionary lookup with no cancelled filter). Suggested check: verify the loaded module path, working directory, import path and commit. Observed evidence: smartcare.data_store.__file__ is ...\st1-assignment-3\project\smartcare\data_store.py on branch fix/stage08-f8-02; `git diff c384995 ec3fc09 -- project/smartcare/data_store.py` shows the Stage 7 find_appointment was a plain dictionary lookup (self._appointments.get(required_text(...))), replaced in the prepared commit ec3fc09 by a loop that skips cancelled appointments. Wrong as a cause of my failure (it accurately describes the unprepared Stage 7 code, which is not the code under test). Reject as a cause: the code I ran is the prepared faulty file in my repo, so the failure comes from the planted change.
3. Ranked suggestion / evidence check / observed evidence / correct, partly correct or wrong / accept, modify or reject with reason: Copilot: the list and the lookup do not observe the same store state or exact key (different store instances, a mock, or an ID mismatch). Suggested check: confirm service.data_store is the store used for the list call and compare repr of the stored ID with the lookup argument. Observed evidence: `a.data_store is s` printed True; repr(x.appointment_id) printed 'A1' and `x.appointment_id == 'A1'` printed True; find_appointment('A1') still printed None. Wrong. Reject: the service, list and lookup use the same store and the same key, so neither explains the failure.

Final human conclusion and comparison with initial hypothesis: My initial hypothesis (saved before Copilot in commit e95806d) was that the store's find_appointment skips cancelled appointments because of status.value != "cancelled". Copilot's top suggestion agreed; I checked it against the code and my runtime output. Suggestions 2 and 3 were plausible but contradicted by evidence. Root cause: the condition `appointment.status.value != "cancelled"` in SmartCareDataStore.find_appointment, which contradicts FR-07 and AC-05.2 by hiding retained cancelled appointments from lookup. Copilot did not change my diagnosis; it confirmed the hypothesis and added two alternatives that I had to rule out.

## G. Failing to passing regression evidence

| Checkpoint | Code SHA or precise diff | Command and working directory | Actual result and artefact reference |
|---|-------------------|-|-|
| F8-01 before repair | e6319d8 | `python -m pytest tests/test_starter.py::test_conflict_rule_and_different_practitioner -v`, run from `project/` on `fix/stage08-f8-01` | 1 failed in 0.02s. The expected `ValueError` was not raised for a same-practitioner/time booking (`tests/test_starter.py:127`). See Section C. |
| F8-01 after repair | 3c4ea3e | `python -m pytest tests/test_starter.py::test_conflict_rule_and_different_practitioner -v`, run from `project/` on `fix/stage08-f8-01` | Focused test passed after correcting the practitioner ID comparison from `!=` to `==`. Rachel recorded the passing result in Section F. Repair commit: `3c4ea3e`, PR #27. |
| F8-02 before repair | ec3fc09           | python -m pytest -q tests/test_services.py::test_cancelled_appointment_is_retained_and_findable, run from project/ on fix/stage08-f8-02|1 failed, LookupError: Appointment not found (services.py:147). Full-suite failure summary recorded in B (3 failed, 110 passed) |
| F8-02 after repair | e7fad56                  | python -m pytest -q tests/test_services.py::test_cancelled_appointment_is_retained_and_findable tests/test_services.py::test_cancel_already_cancelled_appointment_raises_value_error, then python -m pytest -q, run from project/ on fix/stage08-f8-02 | Focused: 2 passed. Full suite: 112 passed, 1 failed (test_conflict_rule_and_different_practitioner, F8-01, not part of this fix) |
| Full suite after both repairs, before refactor | 8c70964 | `python -m pytest -q`, run from `project/` on `debug/stage08` | 113 passed, 0 failed in 0.30s. Both F8-01 and F8-02 repairs were integrated before refactoring. See Section H. |

Explain how the assertions detect each relevant incorrect result and protect previous behaviour: The F8-01 test checks that booking two appointments for the same practitioner at the same date and time raises `ValueError`, while allowing different practitioners to be booked at that time. This protects the practitioner conflict rule. The F8-02 tests verify that cancelled appointments remain findable with `CANCELLED` status and that attempting to cancel an already-cancelled appointment raises `ValueError`. Additional tests check that unknown appointment IDs raise `LookupError` and blank IDs raise `ValueError`. Together, these assertions help detect the reintroduction of both defects while protecting existing booking, cancellation and lookup behaviour.

Unrelated failures investigated / resolution: Not applicable. The three failures in the prepared faulty state were associated with F8-01 and F8-02. After both repairs and the refactoring, the full regression suite passed with 113 passed and 0 failed at commit `91f2d4f`. No unrelated test failures were observed in this verification.

## H. Refactoring decision and before/after verification

Smell and exact location: project/smartcare/services.py, AppointmentService.book_appointment(). The method handles several responsibilities, including participant lookup, validation, conflict checking and appointment creation, making it harder to read.

Small proposed structural change / why justified: Extract the patient and practitioner lookup and missing-record checks into a small private helper method. This will simplify book_appointment() without changing its functionality. Issue: https://github.com/u3325845/st1-assignment-3/issues/29

External behaviour to preserve / relevant tests: Preserve existing validation rules, exception types, error messages, validation order, booking behaviour and practitioner conflict detection. Verify behaviour using the existing appointment service tests and the full regression suite.

Before results: 113 passed in 0.30s, using python -m pytest -q from project/ on debug/stage08 (SHA 8c70964), before refactoring.

Actual change / diff / separate refactor SHA: Extracted the patient and practitioner lookup and missing-record checks from AppointmentService.book_appointment() into a private helper, _get_registered_participants(). Only project/smartcare/services.py was changed in the application code. Refactor SHA: cca6971.

Focused and full after-refactor commands / working directory / results / evidence: From project/, ran python -m pytest -q tests/test_services.py — 9 passed in 0.03s. Ran python -m pytest -q — 113 passed in 0.19s. git diff --check returned no errors.

Result — accepted, revised or rejected / reason / behaviour-preservation conclusion: Accepted. The refactoring separates participant lookup and validation from booking logic without intentionally changing behaviour. The focused tests and full regression suite passed, supporting that existing functionality was preserved.

## I. Git, human review and integration

Issues for both defects / refactor scope and owners: F8-01 practitioner conflict - Rachel (fix/stage08-f8-01). F8-02 cancelled appointment lookup - Novera (fix/stage08-f8-02). Appointment booking validation refactoring - Merlin, Issue #29.

Branch / prepared, repair and refactor checkpoints:Prepared faulty-state SHA: ec3fc09 on debug/stage08. F8-01 repair SHA: 3c4ea3e. F8-02 repair SHA: e7fad56. Both repairs were integrated before refactoring (SHA 8c70964). Refactoring branch: refactor/stage08; refactoring SHA: cca6971. Evidence update SHA: 189f23b. See Sections B, C, D and H.

PR link and another member's reviewer identity: F8-01: PR #27 (Rachel) reviewed by Novera. F8-02: PR #26 (Novera) reviewed by Rachel. Refactoring: PR #30, created by Merlin and reviewed by Tarnima

Key human feedback, difference from Copilot findings and response/outcome: Tarnima reviewed and approved Merlin's refactoring PR #30 without requesting changes. The refactoring extracted participant lookup and validation into `_get_registered_participants()` while preserving the existing booking behaviour. The recorded focused and full regression tests passed, supporting the decision to approve. Unlike the Copilot debugging suggestions in Section F, which required investigation and evidence-based acceptance or rejection, this human review evaluated the actual refactoring and its test results. PR #30 was subsequently merged into `debug/stage08` at commit `c2f6485`.

**Actual review approval / merge evidence:** PR #26 (Novera), PR #27 (Rachel) and PR #30 (Merlin) were merged into `debug/stage08`. Review and merge evidence is available at:
- https://github.com/u3325845/st1-assignment-3/pull/26
- https://github.com/u3325845/st1-assignment-3/pull/27
- https://github.com/u3325845/st1-assignment-3/pull/30

Integrated code SHA and team pull/retest command / working directory / result: c2f6485 on debug/stage08. Ran git switch debug/stage08, git pull --ff-only origin debug/stage08, then python -m pytest -q from project/. Result: 113 passed in 0.23s.

Evidence-only later SHA / explanation if different: 91f2d4f is the Stage 8 documentation integration commit from PR #31, following the refactoring integration at c2f6485. No further application-code changes were introduced by the documentation update. Tarnima verified the three focused regression tests (3 passed in 0.02s) and the full regression suite (113 passed in 0.16s) on test/stage08-regression at 91f2d4f.

Each member's substantive contribution and artefact:

Rachel - Investigated and repaired F8-01 practitioner conflict. Recorded the human-first hypothesis, evaluated Copilot's suggestions and verified the repair using the focused regression test. PR #27, repair SHA 3c4ea3e.

Novera - Investigated and repaired F8-02 cancelled appointment lookup. PR #26.

Merlin - Refactored participant lookup and validation in AppointmentService.book_appointment(). Issue #29, PR #30, SHA cca6971. Verified 9 focused tests and 113 full-suite tests.

Tarnima - Reviewed Merlin's refactoring PR #30 and supported Stage 8 integration and regression verification. Created `test/stage08-regression` from `debug/stage08` and independently verified the three focused F8-01/F8-02 regression tests (3 passed in 0.02s) and the complete test suite (113 passed in 0.16s) at commit `91f2d4f`. Completed the missing Section G regression evidence using the team's recorded repair results and Git history.

## J. Required reflections

1. Which Copilot diagnosis appeared convincing but lacked evidence?

For F8-02, Copilot suggested that the application might be loading a different version of the code. This seemed possible because the code Copilot described did not contain the cancelled-appointment filter. However, checking the loaded module path and Git history confirmed that the correct faulty version was being executed. The actual cause was the condition that excluded cancelled appointments from lookup. Therefore, the suggestion was rejected because it did not match the observed evidence.


2. What evidence changed your group's view?

For F8-02, the team initially considered whether cancellation removed the appointment from storage. However, the runtime check showed that appointment A1 was still present in list_appointments(), while find_appointment() returned None. Inspecting the data-store code confirmed that cancelled appointments were being excluded during lookup. For F8-01, the failing test and code inspection showed that the practitioner ID comparison used != instead of ==. These findings helped the team identify the actual causes and make small, justified repairs instead of changing unrelated code.

3. How did regression tests protect the refactoring?

Regression tests helped the team confirm that Merlin's refactoring did not change the existing booking behaviour. Before refactoring, the full test suite passed with 113 tests. After extracting participant lookup and validation into a separate helper method, all 9 focused service tests and 113 regression tests passed. These tests checked that existing validation, booking, conflict detection and cancellation behaviour continued working. This provided evidence that the internal code structure was improved without introducing new defects.


## K. Ten formative questions

1. What should an engineer do before changing code in response to a failure?

Response: They should first reproduce the failure, read the error message and traceback, and identify what is causing the problem. They should avoid changing code without understanding the failure.

2. Where should expected behaviour come from during debugging?

Response: Expected behaviour should come from the project requirements, acceptance criteria, specifications and existing tests, rather than assumptions.

3. What is a debugging hypothesis?

Response: A debugging hypothesis is a possible explanation for why a failure is happening. It should be tested using evidence before deciding on a fix.

4. What is a regression test and why is it retained?

Response: A regression test checks that a previously fixed problem does not happen again. It is retained to prevent future changes from reintroducing the same defect.

5. What is meant by root cause?

Response: The root cause is the underlying reason a problem occurs, rather than just the visible error or symptom.

6. What is refactoring?

Response: Refactoring means improving the internal structure, readability or maintainability of code without changing its external behaviour.

7. What is a swallowed exception?

Response: A swallowed exception happens when an error is caught but ignored without proper handling or reporting. This can hide problems and make debugging harder.

8. What is a code smell?

Response: A code smell is a sign that code may have a design or maintainability problem, such as duplicated code, long methods or unclear names. It does not always mean the code is incorrect.

9. How should GitHub Copilot-generated debugging diagnoses be treated?

Response: Copilot's suggestions should be treated as possible explanations, not confirmed facts. Engineers must check them against the code, requirements and test results before accepting them.

10. What is the Stage 8 engineering rule?

Response: Reproduce and understand the failure before making changes, fix the root cause with a small justified change, and run focused and regression tests to confirm the fix. Refactoring should preserve existing behaviour.

## L. Completion and handover

- [x] Existing project, earlier tests and stage records preserved.
- [x] Passing Stage 7 SHA and safe preparation details recorded.
- [x] Both defects reproduced with meaningful failing tests.
- [x] Both human hypotheses recorded before Copilot; actual suggestions evaluated with evidence.
- [x] Supported causes and minimal repairs explained; focused and full regression results recorded.
- [x] One genuine refactor verified under passing before/after tests.
- [x] Human PR review, feedback resolution and integrated retest recorded.
- [x] Tutorial, three reflections and ten formative responses complete.
- [x] Local recovery metadata excluded from submitted source.
- [x] Same project and full suite ready for Stage 9 after Stage 8 integration, verification and recording.

Verified integrated code SHA / result: c2f6485 on debug/stage08. The full regression suite passed with 113 tests in 0.23s after integration. Following the documentation merge at 91f2d4f, the team verified 3 focused regression tests (3 passed in 0.02s) and the full suite (113 passed in 0.16s) on test/stage08-regression.
Submitted SHA and evidence-only difference if any: 91f2d4f. Subsequent changes are documentation-only; final commit SHA will be available in the PR.

Unresolved issues or incomplete checks / owner / next action: No unresolved code defects or test failures. Stage 8 documentation awaits final review and integration.

Handover note: Both defects repaired, refactoring integrated and 113 regression tests passed. The verified project is ready for Stage 9.