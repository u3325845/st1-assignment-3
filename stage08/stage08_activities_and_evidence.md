# Stage 8 activities and evidence

UG and PG | One evolving group project | Complete this blank record using the Stage 8 handout.

All Assignment 3 stage materials are provided from the beginning. Complete this stage only after the previous applicable stage has been integrated, verified and recorded. Use this supplied record in stage08/ in your EXISTING repository. Preserve project/, all earlier tests, records and responses. Do not download another starter or copy staff solutions. The Stage 8 preparation utility is supplied or run by teaching staff when Stage 8 begins. Follow your tutor’s controlled workflow and the handout. If temporarily supplied, keep it outside the repository in a sibling Stage_8_Assets/ folder; exclude it from Git and the final submission.

Group/tutorial: [complete]
Members and UG/PG cohorts: [complete]
Record owner / contribution links for each member: [complete]

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

- Symptom / observed behaviour: [complete]
- Expected behaviour and requirement: [complete]
- Minimal synthetic reproduction steps: [complete]
- Meaningful failing test path/name and exact relevant failure: [complete]
- Human hypothesis and intended checks: see E, F8-01.
- Supported root cause and inspected code/runtime evidence: [complete after diagnosis]
- Smallest justified fix / diff / why other behaviour is preserved: [complete]
- Repair SHA / focused verification result: [complete]

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
- Supported root cause and inspected code/runtime evidence: [complete]
- Smallest justified fix / diff / why other behaviour is preserved: [complete]
- Repair SHA / focused verification result: [complete]

## E. Human-first hypotheses

Complete both entries BEFORE Copilot. C/D supply observed/expected/reproduction/test; retain those initial facts and link them here.

### F8-01 human entry
Likely cause and why plausible: [complete]
Evidence intended to inspect / competing explanation / discriminating check: [complete]
Member and saved sequence/time or commit showing this preceded consultation: [complete]

### F8-02 human entry
Likely cause and why plausible: The store's find_appointment loops over the stored appointments but only returns an appointment if appointment.status.value != "cancelled". A cancelled A1 therefore fails the condition, the loop ends and the method returns None. This is plausible because the failure appears only after cancelling and only in lookup, and the condition contradicts FR-07 / AC-05.2.

Evidence intended to inspect / competing explanation / discriminating check: Inspect find_appointment, list_appointments and add_appointment in data_store.py. Competing explanation: the cancelled appointment is no longer in the store, or list_appointments() leaves it out. Discriminating check: book and cancel A1, then print list_appointments() and find_appointment("A1"). Result on 5 Nov 2026, 21:51: [('A1', 'cancelled')] and None. A1 is still stored but the lookup does not return it, so the competing explanation is not supported.
Member and saved sequence/time or commit showing this preceded consultation: Novera. Hypothesis committed on fix/stage08-f8-02 before consulting Copilot: e95806d. I identified the condition by reading the code and ran the check above before consulting Copilot.

## F. GitHub Copilot prompts, findings and human decisions

Use the full handout prompt separately for BOTH defects, after E. Keep each actual prompt or accessible reference; include observed behaviour, expected behaviour, reproduction, failing test, human hypothesis, relevant code, three ranked causes and discriminating checks, with the no-rewrite/no-invented-requirements constraints.

### F8-01 Copilot review
Actual prompt / output reference and member: [complete]
1. Ranked suggestion / evidence check / observed evidence / correct, partly correct or wrong / accept, modify or reject with reason: [complete]
2. Ranked suggestion / evidence check / observed evidence / correct, partly correct or wrong / accept, modify or reject with reason: [complete]
3. Ranked suggestion / evidence check / observed evidence / correct, partly correct or wrong / accept, modify or reject with reason: [complete]
Final human conclusion and comparison with initial hypothesis: [complete]

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
|---|--|-|-|
| F8-01 before repair | [complete] | [complete] | [complete] |
| F8-01 after repair | [complete] | [complete] | [complete] |
| F8-02 before repair | ec3fc09 | python -m pytest -q tests/test_services.py::test_cancelled_appointment_is_retained_and_findable, run from project/ on fix/stage08-f8-02|1 failed, LookupError: Appointment not found (services.py:147). Full-suite failure summary recorded in B (3 failed, 110 passed) |
| F8-02 after repair | [complete] | [complete] | [complete] |
| Full suite after both repairs, before refactor | [complete] | [complete] | [complete] |

Explain how the assertions detect each relevant incorrect result and protect previous behaviour: [complete]
Unrelated failures investigated / resolution: [complete or not applicable with reason]

## H. Refactoring decision and before/after verification

Smell and exact location: [complete]
Small proposed structural change / why justified: [complete before editing]
External behaviour to preserve / relevant tests: [complete]
Before result: see G, full passing suite.
Actual change / diff / separate refactor SHA: [complete]
Focused and full after-refactor commands / working directory / results / evidence: [complete]
Result — accepted, revised or rejected / reason / behaviour-preservation conclusion: [complete]

## I. Git, human review and integration

Issues for both defects / refactor scope and owners: [complete]
Branch / prepared, repair and refactor checkpoints: [link B/C/D/H]
PR link and another member's reviewer identity: [complete]
Key human feedback, difference from Copilot findings and response/outcome: [complete]
Actual review approval / merge evidence: [complete]
Integrated code SHA and team pull/retest command / working directory / result: [complete]
Evidence-only later SHA / explanation if different: [complete or not applicable]
Each member's substantive contribution and artefact: [complete]

## J. Required reflections

1. Which Copilot diagnosis appeared convincing but lacked evidence? [complete; report honestly if none and discuss the least-supported real suggestion]
2. What evidence changed your group's view? [complete]
3. How did regression tests protect the refactoring? [complete]

## K. Ten formative questions

1. What should an engineer do before changing code in response to a failure?

Response: [complete]

2. Where should expected behaviour come from during debugging?

Response: [complete]

3. What is a debugging hypothesis?

Response: [complete]

4. What is a regression test and why is it retained?

Response: [complete]

5. What is meant by root cause?

Response: [complete]

6. What is refactoring?

Response: [complete]

7. What is a swallowed exception?

Response: [complete]

8. What is a code smell?

Response: [complete]

9. How should GitHub Copilot-generated debugging diagnoses be treated?

Response: [complete]

10. What is the Stage 8 engineering rule?

Response: [complete]

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
