# Stage 8 activities and evidence

UG and PG | One evolving group project | Complete this blank record using the Stage 8 handout.

All Assignment 3 stage materials are provided from the beginning. Complete this stage only after the previous applicable stage has been integrated, verified and recorded. Use this supplied record in stage08/ in your EXISTING repository. Preserve project/, all earlier tests, records and responses. Do not download another starter or copy staff solutions. The Stage 8 preparation utility is supplied or run by teaching staff when Stage 8 begins. Follow your tutor’s controlled workflow and the handout. If temporarily supplied, keep it outside the repository in a sibling Stage_8_Assets/ folder; exclude it from Git and the final submission.

Group/tutorial: Grp 2 tutorial Wed 4:30 - 6:30
Members and UG cohorts: RachelUC, Merlin3313611, TarnimaKhan22, u3325845 (Novera)
Record owner / contribution links for each member:
- Rachel: Stage 8 preparation, F8-01 diagnosis, repair, regression testing and test organisation. PR #27: https://github.com/u3325845/st1-assignment-3/pull/27
- Novera: F8-02 diagnosis, repair and regression testing. PR #26: https://github.com/u3325845/st1-assignment-3/pull/26
- Merlin: Stage 8 refactoring and verification (pending).
- Tarnima: Stage 8 review and integration evidence (pending).


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

Response and reason: [complete]

### A.2 Build a debugging record
Choose the cancelled-history scenario or a same-practitioner/time booking. Before changing code, record expected behaviour, observed behaviour, minimal reproduction, a hypothesis and evidence to inspect. Use a requirement to justify the expectation. Keep the initial hypothesis even if later evidence disproves it.

Response and reason: [complete]

### A.3 Test defect or product defect
A test expects cancelled appointments to be deleted, but FR-07 says history must be retained. What should be changed? Explain why. Also decide whether a test expecting different practitioners at the same time to conflict reflects AC-04.2. Do not assume every failing test is correct.

Response and reason: [complete]

### A.4 Refactoring smell hunt
Consider a hypothetical 70-line AppointmentService method containing duplicate status strings, direct collection manipulation, printing, validation and four nested conditionals. Identify the smells and propose small refactorings that preserve required behaviour. The direct collection work replaces the old storage-specific scenario; use the existing SmartCareDataStore boundary. Do not implement an extra architecture.
Classify these proposed changes as refactoring, repair or feature: rename appt to appointment; extract a repeated conflict helper; add rescheduling; restore retained cancellation lookup; replace a magic status string with the existing enum. Explain the behaviour that must remain unchanged.

Response and reason: [complete]

### A.5 Traceback and hypothesis ranking
Using one actual failure, identify its exception/assertion, expected and observed values, test line, application call path and supporting requirement. List three plausible causes and rank them by fit with the available evidence. For each cause, name a check that could distinguish it from the others. Explain why a traceback alone does not establish the cause.

Response and reason: [complete]

### A.6 Exit question
Why is changing code immediately after seeing a failure often a poor debugging strategy?

Response and reason: [complete]


Classification responses (1–5, each with reason): [complete]
Tutorial debugging record — expected; observed; reproduction; hypothesis; evidence to inspect: [complete]
Traceback — exception/assertion; expected/observed values; test line; call path; requirement; ranked causes and discriminating checks: [complete]



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
- Human hypothesis and intended checks: See Section E, F8-01.
- Root cause: The practitioner ID comparison in `SmartCareDataStore.has_practitioner_conflict()` used `!=` instead of `==`. This prevented the system from detecting bookings for the same practitioner at the same time.
- Smallest justified fix: Changed `!=` to `==` in `has_practitioner_conflict()`. No other application behaviour was changed.
- Repair SHA / focused verification result: `3c4ea3e` on `fix/stage08-f8-01` (PR #27). Focused test: 1 passed. Full suite: 111 passed, 2 failed (both related to F8-02).


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
|---|---|---|---|
| F8-01 before repair | `e6319d8` | `python -m pytest tests/test_starter.py::test_conflict_rule_and_different_practitioner -v` from `project/` | 1 failed in 0.02s; expected `ValueError` was not raised. |
| F8-01 after repair | `3c4ea3e` | Focused test above, then `python -m pytest -q` from `project/` | Focused: 1 passed in 0.01s. Full suite: 111 passed, 2 failed (F8-02). |
| F8-02 before repair | `ec3fc09` | `python -m pytest -q tests/test_services.py::test_cancelled_appointment_is_retained_and_findable` from `project/` | 1 failed with `LookupError: Appointment not found`. |
| F8-02 after repair | `e7fad56` | Both F8-02 tests in `tests/test_services.py`, then `python -m pytest -q` from `project/` | Focused: 2 passed. Full suite: 112 passed, 1 failed (F8-01). |
| Full suite after both repairs, before refactor | `8c70964` | `python -m pytest -q` from `project/` | 113 passed in 0.05s. Both repairs integrated into `debug/stage08`. |

**Stage 8 test organisation:** After both repairs were merged, the two F8-02 regression tests were moved from `tests/test_services.py` to `tests/test_starter.py`. The original tests were removed from `test_services.py` to avoid duplication. The full suite still contained 113 tests, and all passed in 0.06s.

Explain how the assertions detect each relevant incorrect result and protect previous behaviour: The F8-01 test rejects double bookings for the same practitioner while allowing different practitioners at the same time. The F8-02 tests confirm that cancelled appointments remain findable and cannot be cancelled twice. The full suite checks that previous behaviour is preserved.

Unrelated failures investigated / resolution: No unrelated failures remained. The full suite passed with 113 tests.

## H. Refactoring decision and before/after verification

Smell and exact location: project/smartcare/services.py, AppointmentService.book_appointment(). The method handles several responsibilities, including participant lookup, validation, conflict checking and appointment creation, making it harder to read.
Small proposed structural change / why justified: Extract the patient and practitioner lookup and missing-record checks into a small private helper method. This will simplify book_appointment() without changing its functionality. Issue: https://github.com/u3325845/st1-assignment-3/issues/29
External behaviour to preserve / relevant tests: Preserve existing validation rules, exception types, error messages, validation order, booking behaviour, and conflict detection; verify using the existing appointment service tests and the full regression suite.
Before results: 113 passed in 0.30s, using python -m pytest -q from project/ on debug/stage08 (SHA 8c70964), before refactoring.
Actual change / diff / separate refactor SHA: Extracted the patient and practitioner lookup and missing-record checks from AppointmentService.book_appointment() into a private helper, _get_registered_participants(). Only project/smartcare/services.py was changed in the application code. Refactor SHA: cca6971.
Focused and full after-refactor commands / working directory / results / evidence: From project/, ran python -m pytest -q tests/test_services.py — 9 passed in 0.03s. Ran python -m pytest -q — 113 passed in 0.19s. git diff --check returned no errors.
Result — accepted, revised or rejected / reason / behaviour-preservation conclusion: Accepted. The refactoring separates participant lookup and validation from booking logic without intentionally changing behaviour. The focused tests and full regression suite passed, supporting that existing functionality was preserved.

## I. Git, human review and integration

Issues for both defects / refactor scope and owners: F8-01 – Rachel, Issue #24, PR #27. F8-02 – Novera, PR #26. Refactoring – Merlin (pending).

Branch / prepared, repair and refactor checkpoints: Prepared branch `debug/stage08`, faulty-state SHA `ec3fc09`. F8-01 repair SHA `3c4ea3e`. F8-02 repair SHA `e7fad56`. Integrated repair SHA `8c70964`. Refactor pending.

PR link and another member's reviewer identity: F8-01 PR #27: https://github.com/u3325845/st1-assignment-3/pull/27 (Merlin and Tarnima requested as reviewers). F8-02 PR #26: https://github.com/u3325845/st1-assignment-3/pull/26 (reviewed and approved by Rachel).

Key human feedback, difference from Copilot findings and response/outcome: Both defects were investigated by group members before consulting Copilot. Copilot's suggested causes were checked against the code and failing tests. Both repairs were limited to the confirmed root causes. Further human review feedback for F8-01 is pending.

Actual review approval / merge evidence: Rachel reviewed and approved F8-02 PR #26. Both repair PRs were merged into `debug/stage08`. F8-01's requested reviews were not completed before its merge; any later review will be recorded separately.

Integrated code SHA and team pull/retest command / working directory / result: `8c70964`. Rachel pulled `debug/stage08` and ran `python -m pytest -q` from `project/`. Result: 113 passed in 0.05s.

Evidence-only later SHA / explanation if different: Pending Stage 8 test organisation and documentation commit. This commit reorganises existing regression tests and updates the evidence record without changing application behaviour.

Each member's substantive contribution and artefact: Rachel – preparation, F8-01 diagnosis and repair, PR #27, and Stage 8 test organisation. Novera – F8-02 diagnosis and repair, PR #26. Merlin – refactoring pending. Tarnima – review and integration evidence pending.

## J. Required reflections

1. Which Copilot diagnosis appeared convincing but lacked evidence?

For F8-02, Copilot suggested that the program might be loading a different version of the code. This seemed possible, but checking the module path and Git history showed that the correct faulty version was running. We rejected this explanation.

2. What evidence changed your group's view?

The failing tests and code inspection helped us confirm both faults. For F8-01, changing the incorrect practitioner comparison made the test pass. For F8-02, we confirmed that cancelled appointments were still stored but were being excluded from lookup.

3. How did regression tests protect the refactoring? [complete]


## K. Ten formative questions

1. What should an engineer do before changing code in response to a failure?

First understand the problem, reproduce the failure, check the requirements and collect evidence before making changes.

2. Where should expected behaviour come from during debugging?

Expected behaviour should come from the project requirements, acceptance criteria and agreed business rules.

3. What is a debugging hypothesis?

A debugging hypothesis is a possible explanation for a problem that needs to be checked using evidence.

4. What is a regression test and why is it retained?

A regression test checks that a previously fixed problem does not happen again. It is retained to protect the code from future changes.

5. What is meant by root cause?

The root cause is the actual underlying reason why a problem occurs.

6. What is refactoring?

Refactoring means improving the structure or readability of code without changing how it behaves.

7. What is a swallowed exception?

A swallowed exception happens when an error is caught but ignored, making the problem harder to notice or debug.

8. What is a code smell?

A code smell is a sign that some code may be difficult to understand, maintain or improve.

9. How should GitHub Copilot-generated debugging diagnoses be treated?

Copilot suggestions should be treated as possible explanations, not confirmed facts. We should check them against the code, tests and requirements.

10. What is the Stage 8 engineering rule?

Understand the failure, collect evidence, confirm the root cause, make the smallest justified repair and verify it with regression tests. Refactoring should be separate and must preserve behaviour.


## L. Completion and handover

- [ ] Existing project, earlier tests and stage records preserved.
- [ ] Passing Stage 7 SHA and safe preparation details recorded.
- [ ] Both defects reproduced with meaningful failing tests.
- [ ] Both human hypotheses recorded before Copilot; actual suggestions evaluated with evidence.
- [ ] Supported causes and minimal repairs explained; focused and full regression results recorded.
- [ ] One genuine refactor verified under passing before/after tests.
- [ ] Human PR review, feedback resolution and integrated retest recorded.
- [ ] Tutorial, three reflections and ten formative responses complete.
- [ ] Local recovery metadata excluded from submitted source.
- [ ] Same project and full suite ready for Stage 9 after Stage 8 integration, verification and recording.

Verified integrated code SHA / result: see I.
Submitted SHA and evidence-only difference if any: [complete]
Unresolved issues or incomplete checks / owner / next action: [complete]
Handover note: [complete]
