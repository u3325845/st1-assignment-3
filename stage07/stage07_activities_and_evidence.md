# Stage 7 Testing and Verification Record

Group/tutorial: Grp 2 tutorial Wed 4:30 - 6:30
Members/cohorts: RachelUC, Merlin3313611, TarnimaKhan22, u3325845 (Novera)
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
| FR-07 Retain cancelled history | Retrieve an appointment after cancellation. |  Cancel an appointment, then attempt to retrieve it to verify that cancellation has not incorrectly deleted the record. | The cancelled appointment remains retrievable with status CANCELLED. |

### Activity 2 Strong or weak assertion

For each, select Strong for stated behaviour or Weak/unclear and explain why. State the behaviour and limits.

`assert True`
Judgement: Weak/unclear    
Why: This assertion always passes, regardless of whether the program works correctly, as it does not check any required behaviour or expected result, so it provides no useful evidence of correctness.

`assert appointment is not None`
Judgement: Weak/unclear   
Why: This assertion only checks that an appointment object exists. It does not verify whether the appointment has the correct ID, practitioner, patient or status. Therefore, an incorrect appointment could still pass this test.

`assert appointment.status == AppointmentStatus.CANCELLED`
Judgement: Strong for stated behaviour   
Why: This assertion checks that the appointment has the expected CANCELLED status. It would fail if the appointment had a different status. However, it does not prove that the cancelled appointment remains stored or can be retrieved later.

`assert len(results) > 0`
Judgement: Weak/unclear    
Why:  This assertion only checks that the results contain at least one item. It does not verify whether the correct appointments were returned or whether the results contain incorrect or unexpected records; a wrong result could still pass.

`assert data_store.find_appointment('A1') is appointment`
Judgement: Strong for stated behaviour   
Why: This assertion checks that the data store retrieves the exact same appointment object using the ID A1. It provides strong evidence that the appointment remains stored and retrievable. However, it does not check whether the appointment has the correct status or other details.

### Activity 3 Boundary thinking

Design boundary or edge cases for blank identifiers, whitespace-only names, same-time practitioner bookings, cancelled appointments and invalid status transitions.
For each input/state, expected result and supporting contract: 


**1. Blank identifiers**

**Input/state:** An empty (`''`) or whitespace-only (`'   '`) patient, practitioner or appointment ID.

**Expected result:** The system raises `ValueError` and rejects the invalid identifier. No invalid record is created.

**Supporting contract:** Revision 2 validation contract - required IDs must be non-blank and are trimmed.

**2. Whitespace-only names**

**Input/state:** A patient or practitioner name containing only spaces.

**Expected result:** The system raises `ValueError` because the required name does not contain valid text.

**Supporting contract:** Required-field validation contract - names and practitioner specialties must contain non-whitespace text.

**3. Same-time practitioner bookings**

**Input/state:** Attempting to book a second appointment for the same practitioner at the exact same date and time as an existing `SCHEDULED` appointment.

**Expected result:** The second booking raises `ValueError`, and the original appointment remains unchanged. Bookings at different times or for different practitioners at the same time are allowed. A cancelled appointment also does not block that time slot.

**Supporting contract:** FR-05, AC-04.1 and AC-04.2 - prevent exact-time conflicts while allowing valid alternatives.

**4. Cancelled appointments**

**Input/state:** Attempting to cancel an appointment that already has the status `CANCELLED`.

**Expected result:** The system raises `ValueError`. The appointment remains stored and retrievable with its `CANCELLED` status.

**Supporting contract:** FR-06 (AC-05.3) - repeated cancellation is rejected; FR-07 (AC-05.2) — cancelled appointment history remains retrievable.

**5. Invalid status transitions**

**Input/state:** Attempting to cancel an appointment with the status `COMPLETED`.

**Expected result:** The system raises `ValueError` and leaves the appointment's existing status unchanged.

**Supporting contract:** Appointment cancellation guard - only `SCHEDULED` appointments can be cancelled; cancelling a `COMPLETED` appointment is rejected.


### Activity 4 Critique GitHub Copilot tests

GitHub Copilot generates five tests, all of which pass. Two only assert that objects are not None, one asserts True, and two assume SMS notifications exist. Identify what is wrong and rewrite the test intentions.

| Candidate | What is wrong | Rewritten test intention |
|---|--|--|
| 1 | The test only checks that an object is not None. This is a weak assertion because it does not verify whether the correct object or data was returned. | Register a patient with valid details and verify that the correct patient record is stored and can be retrieved using its ID. |
| 2 | The test only checks that an appointment object is not None. It could pass even if the appointment contains incorrect information or status. | Book a valid appointment and verify that it contains the correct patient, practitioner, appointment ID and SCHEDULED status. |
| 3 | The test uses assert True, which always passes regardless of the program's behaviour. It provides no meaningful evidence that the requirements are satisfied. | Attempt to register a patient with an existing ID and verify that ValueError is raised and the original patient record remains unchanged. |
| 4 | The test assumes that SMS notifications exist, even though this functionality is not included in the SmartCare requirements. It tests an unsupported feature instead of required behaviour. | Cancel an existing SCHEDULED appointment and verify that its status changes to CANCELLED. |
| 5 | The test assumes that an SMS notification is sent after cancellation. This introduces functionality that is not specified in the requirements. | Retrieve a cancelled appointment using its ID and verify that it remains stored with status CANCELLED. |

### Tutorial exit question

Why can 100% code coverage coexist with poor software verification?
100% code coverage only shows that every measured line of code was executed during testing, but it does not guarantee that the required behaviour was correctly verified. Tests may use weak assertions such as `assert True`, miss important boundary or negative cases, or check behaviours that are not part of the actual requirements. Coverage also cannot identify requirements that were never implemented. Therefore, even with full coverage, the software may still contain defects because code execution does not prove correctness.

## B Requirement to Test Traceability Matrix

Assign TEST IDs before implementation or generation. Use canonical AC IDs with their actual meaning; quote supporting revision 2 contracts when no canonical AC is assigned. Blank-ID validation is not AC-01.2. Identify supplied versus student-authored evidence.

| Requirement | Acceptance criterion | Test ID | Test type | Test name / location | Expected behaviour | Result / observed status | Supplied or student-authored |
|---|---|---|---|---|---|---|---|
| Patient domain validation | Patient ID and name must be valid, non-blank text. | TEST-PAT-01 | Unit – Positive | test_patient_created_with_valid_details() – tests/test_patient_lookup.py | A patient is created with the correct ID and name. | Passed | Student-authored |
| Patient domain validation | Surrounding spaces are removed from valid text. | TEST-PAT-02 | Unit – Positive | test_patient_details_are_trimmed() – tests/test_patient_lookup.py | Spaces are removed from the ID and name. | Passed | Student-authored |
| Patient domain validation | Blank patient IDs are rejected. | TEST-PAT-03 | Unit – Negative/Boundary | test_patient_rejects_blank_id() – tests/test_patient_lookup.py | Empty and whitespace-only IDs raise ValueError. | Passed (4 inputs) | Student-authored |
| Patient domain validation | Blank patient names are rejected. | TEST-PAT-04 | Unit – Negative | test_patient_rejects_whitespace_name() – tests/test_patient_lookup.py | A whitespace-only name raises ValueError. | Passed | Student-authored |
| Patient domain validation | Patient ID and name must be strings. | TEST-PAT-05 | Unit – Negative | test_patient_rejects_non_string_details() – tests/test_patient_lookup.py | Non-string inputs raise ValueError with the correct message. | Passed (4 inputs) | Student-authored |
| Patient identity | Patient ID is read-only after creation. | TEST-PAT-06 | Unit – Negative | test_patient_id_is_read_only() – tests/test_patient_lookup.py | Changing the patient ID raises AttributeError and leaves the ID unchanged. | Passed | Student-authored |
| Patient domain validation | Valid non-blank text has no additional minimum length. | TEST-PAT-07 | Unit – Boundary | test_patient_accepts_one_character_details() – tests/test_patient_lookup.py | A one-character ID and name are accepted. | Passed | Student-authored |

## C Test Design

Use descriptive test names such as test_cancel_changes_status() or test_blank_patient_id_is_rejected(). Explain what new evidence each case adds.

| Test ID | Requirement | Acceptance criterion | Positive / Negative / Boundary | Test intention | Observable result expected | Added evidence beyond supplied tests |
|---|---|---|---|---|---|---|
| TEST-PAT-01 | Patient domain validation | Valid patient ID and name | Positive | Create a patient using a valid ID and name. | Patient is created with the correct ID and name. | Checks both patient details, not just whether the object exists. |
| TEST-PAT-02 | Patient domain validation | Surrounding spaces are removed | Positive | Create a patient with spaces around the ID and name. | Both values are stored without extra spaces. | Checks trimming of both fields during construction. |
| TEST-PAT-03 | Patient domain validation | Blank patient IDs are rejected | Negative / Boundary | Try creating a patient with an empty ID, spaces, a tab and a newline. | Each input raises ValueError with the correct message. | Checks different types of blank input at the Patient class level. |
| TEST-PAT-04 | Patient domain validation | Blank patient names are rejected | Negative | Create a patient with a name containing only spaces. | ValueError is raised with the correct message. | Checks that an invalid name is rejected during construction. |
| TEST-PAT-05 | Patient domain validation | Patient details must be strings | Negative | Try creating patients with None or integer values for the ID or name. | Each input raises ValueError with the correct message. | Checks invalid types for both fields and identifies which field caused the error. |
| TEST-PAT-06 | Patient identity | Patient ID is read-only | Negative | Create a patient and try changing its ID. | AttributeError is raised and the original ID remains unchanged. | Checks that patient identity cannot be changed through the property. |
| TEST-PAT-07 | Patient domain validation | Non-blank text is accepted | Boundary | Create a patient with a one-character ID and name. | Patient is created and both values are stored correctly. | Checks the smallest valid non-blank text input. |

## D Arrange Act Assert Record

Arrange test data; act on one meaningful behaviour; assert the required observable outcome. Use the specific current exception with pytest.raises where needed.

| Test ID | Arrange | Act | Assert | Why meaningful / why assertion proves criterion |
|---|---|---|---|---|
| TEST-PAT-01 | Use valid patient ID "P1" and name "Alex". | Create a Patient object. | Check patient_id == "P1" and name == "Alex". | Confirms that both patient details are stored correctly. |
| TEST-PAT-02 | Use ID "  P1  " and name "  Alex  ". | Create a Patient object with surrounding spaces. | Check patient_id == "P1" and name == "Alex". | Confirms that extra spaces are removed from both fields. |
| TEST-PAT-03 | Prepare empty ID, spaces, tab and newline as inputs. | Try creating a Patient with each invalid ID. | Check that ValueError is raised with "Patient ID cannot be blank". | Confirms that different blank ID inputs are rejected correctly. |
| TEST-PAT-04 | Use valid ID "P1" and name containing only spaces. | Try creating a Patient object. | Check that ValueError is raised with "Patient name cannot be blank". | Confirms that a whitespace-only patient name is rejected. |
| TEST-PAT-05 | Prepare None and integer inputs for patient ID and name. | Try creating a Patient with each invalid input. | Check that ValueError is raised with the correct message for the invalid field. | Confirms that non-string values are rejected and the correct field is identified. |
| TEST-PAT-06 | Create a Patient with ID "P1" and name "Alex". | Try changing patient_id to "P2". | Check that AttributeError is raised and patient_id remains "P1". | Confirms that the patient ID cannot be changed through its read-only property. |
| TEST-PAT-07 | Use one-character ID "P" and name "A". | Create a Patient object. | Check patient_id == "P" and name == "A". | Confirms that the smallest valid non-blank text values are accepted. |


## E Domain Test Evidence

Cover Patient/Practitioner construction and validation; Appointment construction, initial status, cancellation and illegal/repeated transitions. Preserve the four reference intentions described in handout Part C.

| Test ID | Behaviour | Test file/function | Result |
|---|---|---|---|
| TEST-PAT-01 | Create a patient with valid ID and name. | `tests/test_patient_lookup.py::test_patient_created_with_valid_details` | Passed |
| TEST-PAT-02 | Remove surrounding spaces from patient ID and name. | `tests/test_patient_lookup.py::test_patient_details_are_trimmed` | Passed |
| TEST-PAT-03 | Reject empty and whitespace-only patient IDs. | `tests/test_patient_lookup.py::test_patient_rejects_blank_id` | Passed (4 inputs) |
| TEST-PAT-04 | Reject a whitespace-only patient name. | `tests/test_patient_lookup.py::test_patient_rejects_whitespace_name` | Passed |
| TEST-PAT-05 | Reject non-string patient details with the correct error message. | `tests/test_patient_lookup.py::test_patient_rejects_non_string_details` | Passed (4 inputs) |
| TEST-PAT-06 | Prevent changes to the patient's read-only ID. | `tests/test_patient_lookup.py::test_patient_id_is_read_only` | Passed |
| TEST-PAT-07 | Accept one-character patient ID and name. | `tests/test_patient_lookup.py::test_patient_accepts_one_character_details` | Passed |


## F Service Test Evidence

Use fresh shared SmartCareDataStore state, registered objects and completed Stage 6 services.

| Test ID | Behaviour | Requirement / criterion | Test file/function | Result |
|---|---|---|---|---|
| S6-PAT-01 | Find an existing registered patient. | FR-02 Patient Lookup – return the matching patient. | `tests/test_patient_lookup.py::test_find_existing_patient` | Passed (retained Stage 6 test) |
| S6-PAT-02 | Reject a patient ID that does not exist. | FR-02 Patient Lookup – unknown ID raises LookupError. | `tests/test_patient_lookup.py::test_find_unknown_patient` | Passed (retained Stage 6 test) |
| S6-PAT-03 | Reject a blank patient ID. | FR-02 Patient Lookup – blank ID raises ValueError. | `tests/test_patient_lookup.py::test_find_blank_patient_id` | Passed (retained Stage 6 test) |


## G Negative and Boundary Cases

Connect cases to actual contracts and verify unchanged state after rejection.

| Behaviour | Boundary/invalid input | Expected result | Test ID |
|---|---|---|---|
| Patient ID validation | Empty ID, spaces, tab or newline | ValueError is raised with "Patient ID cannot be blank". | TEST-PAT-03 |
| Patient name validation | Name containing only spaces | ValueError is raised with "Patient name cannot be blank". | TEST-PAT-04 |
| Patient details validation | None or integer used as patient ID or name | ValueError is raised with the correct message for the invalid field. | TEST-PAT-05 |
| Patient identity | Attempt to change patient_id from "P1" to "P2" | AttributeError is raised and the original patient ID remains unchanged. | TEST-PAT-06 |
| Minimum valid text | One-character ID "P" and name "A" | Patient is created successfully with both values unchanged. | TEST-PAT-07 |



## H GitHub Copilot Test Design

Select ONE real acceptance criterion. Complete human-first fields before using Copilot. Do not require an accepted generated test.

Requirement: Patient domain validation.

Acceptance criterion: Patient ID and name must be valid, non-blank text. Invalid values raise ValueError.

Behaviour to test: Check that invalid patient IDs and names are rejected with the correct error messages.

Human-first test idea/categories: Before using Copilot, I designed seven Patient tests covering valid details, trimming spaces, blank IDs, blank names, non-string inputs, read-only patient ID and one-character values. I recorded my test ideas in GitHub Issue #13 before asking Copilot.

Human-first evidence: https://github.com/u3325845/st1-assignment-3/issues/13#issuecomment-6603849473

Prompt and purpose: I asked GitHub Copilot to review my Patient tests against the Patient class and identify missing cases or weak assertions. I wanted to improve my original tests and check whether they matched the actual requirements.

Copilot conversation: https://github.com/copilot/c/ef849b60-0a91-4c25-bfab-a5c73971846d

For each significant candidate, copy this entry as needed:

### Candidate 1 – Whitespace-only Patient IDs

- Copilot test idea/candidate: Add more whitespace-only ID inputs, including tabs and newlines.
- What it claims to verify: Different types of blank patient IDs are rejected.
- Requirement trace: Patient domain validation – patient IDs must be non-blank text.
- Assertion quality: Strong because it checks both ValueError and the correct error message.
- Human critique: My original test did not include tabs and newlines, so these were useful boundary cases.
- Decision: Modify
- Reason: I updated my original test using pytest.mark.parametrize to check four invalid IDs.
- Final test reference if accepted/modified: TEST-PAT-03 – `tests/test_patient_lookup.py::test_patient_rejects_blank_id`
- Actual verification result: Passed (4 inputs).

### Candidate 2 – Error Messages for Non-String Inputs

- Copilot test idea/candidate: Check the specific error messages when patient details are not strings.
- What it claims to verify: Non-string patient IDs and names raise the correct errors.
- Requirement trace: Patient domain validation – patient ID and name must be valid text.
- Assertion quality: Strong because it checks which field caused the error, not just whether an exception occurred.
- Human critique: My original test only checked ValueError. Checking the message makes the test more meaningful.
- Decision: Modify
- Reason: I added expected error messages for each invalid input using pytest.mark.parametrize.
- Final test reference if accepted/modified: TEST-PAT-05 – `tests/test_patient_lookup.py::test_patient_rejects_non_string_details`
- Actual verification result: Passed (4 inputs).

### Candidate 3 – Changing Patient Name After Creation

- Copilot test idea/candidate: Add a test for changing the patient's name after construction.
- What it claims to verify: Invalid name changes are rejected.
- Requirement trace: No documented requirement states that the name must be validated again after construction.
- Assertion quality: Weak for the current requirement because it assumes behaviour that is not specified.
- Human critique: The Patient class validates the name during construction, but the name can be changed afterwards. I should not add a test for a rule that is not required.
- Decision: Reject
- Reason: The suggested test does not match the documented Patient class behaviour.
- Final test reference if accepted/modified: Not retained.
- Actual verification result: Not run because the suggestion was rejected.

Before accepting: traces to a requirement/criterion; can fail for the right reason; assertion checks required behaviour; no invented business rule; no unnecessary private implementation dependence. Reject/modify weak assertions, invented requirements, excessive mocking, duplicates, wrong exceptions, obsolete architecture and unnecessary dependencies.

## I Weak Copilot Test Reflection

Which Copilot-generated test looked convincing but was weak?
Copilot suggested testing whether invalid patient names could be rejected after creating a Patient object.

Why was it weak?
The Patient class validates the name during construction, but there is no documented requirement to validate name changes afterwards.

How did you strengthen it?
I rejected the suggestion because it did not match the documented requirement. I also improved my existing tests by adding whitespace-only ID cases and checking specific error messages for non-string inputs.

Accepted / modified / rejected test decisions and evidence:
I modified TEST-PAT-03 and TEST-PAT-05 and rejected the name-change suggestion. My decisions are recorded in Section H.

Copilot review: https://github.com/copilot/c/ef849b60-0a91-4c25-bfab-a5c73971846d

## J Regression Run

Run python -m pytest from project/. Retain all accumulated tests. Record the tested SHA accurately.

| Command | Working directory | Code SHA | Passed | Failed | Failure summary | Product defect / test defect / unresolved | Evidence and interpretation |
|---|---|---|---|---|---|---|---|
| `python -m pytest -v` | `project/` | `d2db485` | 47 | 0 | No failures | None | Full regression run after integrating the latest Stage 6 changes into the Stage 7 Patient branch. All 47 tests passed. Evidence: [PR #16](https://github.com/u3325845/st1-assignment-3/pull/16). |


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
| [Issue #13](https://github.com/u3325845/st1-assignment-3/issues/13) – Patient domain tests | `test/stage7-patient` | [PR #16](https://github.com/u3325845/st1-assignment-3/pull/16) | Merlin3313611 and TarnimaKhan22 (review requested) | Awaiting feedback | 47 tests passed; PR open and awaiting review. |


## M Contribution Evidence

Record actual work in test design, implementation, review, traceability, diagnosis, necessary fixes and integration. Do not include confidential peer ratings.

| Member | Actual contribution | Evidence link |
|---|---|---|
| RachelUC | Designed and implemented seven Patient domain tests covering valid details, whitespace, invalid IDs and names, non-string inputs, read-only patient ID and boundary values. Improved two tests after Copilot feedback and rejected one unsupported suggestion. Retained Stage 6 Patient Lookup tests, ran the full regression suite (47 passed) and documented test evidence. | [Issue #13](https://github.com/u3325845/st1-assignment-3/issues/13), [PR #16](https://github.com/u3325845/st1-assignment-3/pull/16) |


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
