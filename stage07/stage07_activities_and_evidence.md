# Stage 7 Testing and Verification Record

Group/tutorial: [complete]  Members/cohorts: [complete]
Requirements baseline: SmartCare A3 Requirements Baseline 2026, revision 2.
Use the same project/. Link actual evidence; keep responses concise. Blank fields are for your group. Copy rows only as needed.

All Assignment 3 stage materials are provided from the beginning. Complete this stage only after the previous applicable stage has been integrated, verified and recorded. Use this supplied record in stage07/ in your EXISTING repository. Preserve project/, all earlier tests, records and responses. Do not download another starter or copy staff solutions.

## A Tutorial Activities

### Activity 1 Requirement to test

For each requirement, propose one positive test, one negative test and the key assertion.

| Requirement | Positive test | Negative test | Key assertion |
|---|---|---|---|
| FR-01 Register patient | [response] | [response] | [response] |
| FR-05 Prevent practitioner conflict | [response] | [response] | [response] |
| FR-06 Cancel appointment | [response] | [response] | [response] |
| FR-07 Retain cancelled history | [response] | [response] | [response] |

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
[response]

2. What question does validation answer?
[response]

3. What is a unit test?
[response]

4. What is a pytest fixture?
[response]

5. What is parametrisation in pytest?
[response]

6. What is regression testing?
[response]

7. What does code coverage tell us, and what does it not prove?
[response]

8. What makes an assertion weak?
[response]

9. What is the appropriate role of GitHub Copilot as a test assistant?
[response]

10. What is the Stage 7 engineering rule?
[response]

## O Stage Completion

Tested Stage 7 main SHA: [complete]
Full-suite result: [complete]
Unresolved defects and effect on baseline: [complete or none]
Clean working tree and integration evidence: [complete]
Stage 8 handover status: [complete; no Stage 8 work assigned]
All tutorial/formative responses and traceability/Copilot decisions complete: [confirm]
