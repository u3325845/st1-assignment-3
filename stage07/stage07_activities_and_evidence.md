# Stage 7 Testing and Verification Record

Group/tutorial: [complete]  Members/cohorts: [complete]
Requirements baseline: SmartCare A3 Requirements Baseline 2026, revision 2.
Use the same project/. Link actual evidence; keep responses concise. Blank fields are for your group. Copy rows only as needed.

All Assignment 3 stage materials are provided from the beginning. Complete this stage only after the previous applicable stage has been integrated, verified and recorded. Use this supplied record in stage07/ in your EXISTING repository. Preserve project/, all earlier tests, records and responses. Do not download another starter or copy staff solutions.

## A Tutorial Activities

### Activity 1 Requirement to test

For each requirement, propose one positive test, one negative test and the key assertion.

| Requirement | Positive test | Negative test | Key assertion |
|---|--|--|--|
| FR-01 Register patient | Register a patient with valid details and a new ID. | Register another patient using an existing ID. | Patient is stored; duplicate raises ValueError and original remains unchanged. |
| FR-05 Prevent practitioner conflict | Book appointments at different times for the same practitioner. | Book two appointments for the same practitioner at a conflicting time. | Valid bookings succeed; conflicting booking is rejected without creating another appointment. |
| FR-06 Cancel appointment | Cancel an existing scheduled appointment. | Attempt to cancel an already cancelled appointment. | Status changes to CANCELLED; repeated cancellation is rejected without changing the record. |
| FR-07 Retain cancelled history | Retrieve an appointment after cancellation. | Check that cancellation has not deleted the appointment. | Appointment remains retrievable with status CANCELLED. |

### Activity 2 Strong or weak assertion

For each, select Strong for stated behaviour or Weak/unclear and explain why. State the behaviour and limits.

`assert True`
Judgement: [Strong for stated behaviour / Weak/unclear]  Why: [response]

`assert appointment is not None`
Judgement: [Strong for stated behaviour / Weak/unclear]  Why: [response]

`assert appointment.status == AppointmentStatus.CANCELLED`
Judgement: [Strong for stated behaviour / Weak/unclear]  Why: [response]

`assert len(results) > 0`
Judgement: [Strong for stated behaviour / Weak/unclear]  Why: [response]

`assert data_store.find_appointment('A1') is appointment`
Judgement: [Strong for stated behaviour / Weak/unclear]  Why: [response]

### Activity 3 Boundary thinking

Design boundary or edge cases for blank identifiers, whitespace-only names, same-time practitioner bookings, cancelled appointments and invalid status transitions.
For each input/state, expected result and supporting contract: [response]

### Activity 4 Critique GitHub Copilot tests

GitHub Copilot generates five tests, all of which pass. Two only assert that objects are not None, one asserts True, and two assume SMS notifications exist. Identify what is wrong and rewrite the test intentions.

| Candidate | What is wrong | Rewritten test intention |
|---|---|---|
| 1 | [response] | [response] |
| 2 | [response] | [response] |
| 3 | [response] | [response] |
| 4 | [response] | [response] |
| 5 | [response] | [response] |

### Tutorial exit question

Why can 100% code coverage coexist with poor software verification?
[response]

## B Requirement to Test Traceability Matrix

Assign TEST IDs before implementation or generation. Use canonical AC IDs with their actual meaning; quote supporting revision 2 contracts when no canonical AC is assigned. Blank-ID validation is not AC-01.2. Identify supplied versus student-authored evidence.

| Requirement | Acceptance criterion | Test ID | Test type | Test name / location | Expected behaviour | Result / observed status | Supplied or student-authored |
|---|---|---|---|---|---|---|---|
| [complete] | [complete] | [complete] | [complete] | [complete] | [complete] | [complete] | [complete] |

## C Test Design

Use descriptive test names such as test_cancel_changes_status() or test_blank_patient_id_is_rejected(). Explain what new evidence each case adds.

| Test ID | Requirement | Acceptance criterion | Positive / Negative / Boundary | Test intention | Observable result expected | Added evidence beyond supplied tests |
|---|---|---|---|---|---|---|
| [complete] | [complete] | [complete] | [complete] | [complete] | [complete] | [complete] |

## D Arrange Act Assert Record

Arrange test data; act on one meaningful behaviour; assert the required observable outcome. Use the specific current exception with pytest.raises where needed.

| Test ID | Arrange | Act | Assert | Why meaningful / why assertion proves criterion |
|---|---|---|---|---|
| [complete] | [complete] | [complete] | [complete] | [complete] |

## E Domain Test Evidence

Cover Patient/Practitioner construction and validation; Appointment construction, initial status, cancellation and illegal/repeated transitions. Preserve the four reference intentions described in handout Part C.

| Test ID | Behaviour | Test file/function | Result |
|---|---|---|---|
| [complete] | [complete] | [complete] | [complete] |

## F Service Test Evidence

Use fresh shared SmartCareDataStore state, registered objects and completed Stage 6 services.

| Test ID | Behaviour | Requirement / criterion | Test file/function | Result |
|---|---|---|---|---|
| [complete] | [complete] | [complete] | [complete] | [complete] |

## G Negative and Boundary Cases

Connect cases to actual contracts and verify unchanged state after rejection.

| Behaviour | Boundary/invalid input | Expected result | Test ID |
|---|---|---|---|
| [complete] | [complete] | [complete] | [complete] |

## H GitHub Copilot Test Design

Select ONE real acceptance criterion. Complete human-first fields before using Copilot. Do not require an accepted generated test.

Requirement: [complete]
Acceptance criterion: [quote]
Behaviour to test: [complete]
Human-first test idea/categories: [complete]
Prompt and purpose: [complete or link]

For each significant candidate, copy this entry as needed:
- Copilot test idea/candidate: [complete]
- What it claims to verify: [complete]
- Requirement trace: [complete]
- Assertion quality: [complete]
- Human critique: [complete]
- Decision: [Accept / Modify / Reject]
- Reason: [complete]
- Final test reference if accepted/modified: [link or not retained]
- Actual verification result: [complete; do not claim an unrun test passed]

Before accepting: traces to a requirement/criterion; can fail for the right reason; assertion checks required behaviour; no invented business rule; no unnecessary private implementation dependence. Reject/modify weak assertions, invented requirements, excessive mocking, duplicates, wrong exceptions, obsolete architecture and unnecessary dependencies.

## I Weak Copilot Test Reflection

Which Copilot-generated test looked convincing but was weak? [response]
Why was it weak? [response]
How did you strengthen it? [response]
Accepted / modified / rejected test decisions and evidence: [link actual decisions in H]

## J Regression Run

Run python -m pytest from project/. Retain all accumulated tests. Record the tested SHA accurately.

| Command | Working directory | Code SHA | Passed | Failed | Failure summary | Product defect / test defect / unresolved | Evidence and interpretation |
|---|---|---|---|---|---|---|---|
| [complete] | [complete] | [complete] | [complete] | [complete] | [complete] | [complete] | [complete] |

Individual test runs and changed-order independence evidence: [commands, results, links]
Optional tutor-led demonstration notes: [optional; leave blank if not used]
A meaningful test should detect a relevant incorrect result. Students do not have to perform the demonstration or submit failure/restoration evidence for assessment. The tutor restores the example and reruns its tests. This is not a Stage 8 fault activity.
Requirement → test → failure/observation → diagnosis → change → verification: [concise links where applicable]

## K What the Suite Still Does Not Prove

What does your test suite still not prove? [response]
Coverage if used: [result or not used]
Which uncovered areas matter, and why does coverage percentage alone not establish correctness? [response]
Optional fixtures/parametrisation used and why, if any: [response or not used]

## L Git and Review Evidence

Use links rather than copying GitHub history. Continue the Stage 6 workflow; no commit/PR count, conflict or individual test quota is imposed.

| Issue/task | Branch | PR | Reviewer | Key feedback | Outcome |
|---|---|---|---|---|---|
| [complete] | [complete] | [complete] | [complete] | [complete] | [complete] |

## M Contribution Evidence

Record actual work in test design, implementation, review, traceability, diagnosis, necessary fixes and integration. Do not include confidential peer ratings.

| Member | Actual contribution | Evidence link |
|---|---|---|
| [complete] | [complete] | [complete] |

## N Formative Questions

1. What question does verification answer?

Verification answers, "Are we building the product correctly?" It checks whether the software follows the specified requirements and contracts. For example, tests verify that SmartCare performs the required actions and handles invalid inputs correctly.

2. What question does validation answer?

Validation answers, "Are we building the right product?" It checks whether the software meets the intended needs of its users. A system may meet its technical requirements but still fail to provide what users actually need.

3. What is a unit test?

A unit test checks a small part of a program, such as a function or method, to verify that it behaves as expected. It focuses on a specific behaviour using controlled test data. Each test should have a clear expected result and run independently.

4. What is a pytest fixture?

A pytest fixture is a reusable setup function that prepares data or objects needed for testing. Tests can request a fixture by including its name as a function parameter. Function-scoped fixtures provide fresh setup for each test, helping prevent tests from affecting one another.

5. What is parametrisation in pytest?

Parametrisation allows one test function to run with multiple sets of inputs and expected results. It reduces repeated code and makes it easier to test different scenarios. Pytest reports each parameter set as a separate test case.

6. What is regression testing?

Regression testing involves rerunning existing tests after changes to the software. Its purpose is to check that new features or fixes have not broken previously working functionality. Tests for corrected defects should also be retained to detect if the same problems return.

7. What does code coverage tell us, and what does it not prove?

Code coverage measures how much of the program's code is executed during testing. It helps identify areas that have not been tested. However, high coverage does not guarantee correctness because tests may execute code without checking the required behaviour through meaningful assertions.

8. What makes an assertion weak?

An assertion is weak when it can pass even if the program produces an incorrect result. For example, assert True does not check any behaviour, while assert appointment is not None only checks that an object exists. Strong assertions verify specific expected outcomes, such as the correct appointment status or stored object.

9. What is the appropriate role of GitHub Copilot as a test assistant?

GitHub Copilot can assist developers by suggesting test cases, generating test code and identifying possible edge cases. However, developers should design their own test intentions first and review Copilot's suggestions against the actual requirements. They must decide whether to accept, modify or reject the suggestions and run the tests before recording results.

10. What is the Stage 7 engineering rule?

The main question is, "What required behaviour does this test actually prove?". The engineering rule is that tests must be traceable to a specific requirement or acceptance criterion, must contain meaningful assertions that would fail if the required behaviour were broken, and must not rely on weak assertions (like assert True or is not None), invented rules, or passing counts/screenshots as evidence of correctness.


## O Stage Completion

Tested Stage 7 main SHA: [complete]
Full-suite result: [complete]
Unresolved defects and effect on baseline: [complete or none]
Clean working tree and integration evidence: [complete]
Stage 8 handover status: [complete; no Stage 8 work assigned]
All tutorial/formative responses and traceability/Copilot decisions complete: [confirm]
