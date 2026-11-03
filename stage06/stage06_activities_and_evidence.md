# Stage 6 activities and evidence

Complete this one group record. Link actual issues, diffs, tests and reviews; avoid copying entire histories. Blank fields are intentional. Duplicate rows as needed. Use synthetic data only. Every member records their own meaningful contribution. Do not invent results, reviews or Copilot use.

- Group/tutorial: Grp 2 tutorial Wed 4:30 - 6:30 
- Members, GitHub usernames and cohorts: RachelUC, Merlin3313611, TarnimaKhan22, u3325845 (Novera)
- Repository URL: https://github.com/u3325845/st1-assignment-3.git
- Starting SHA: 94b40f1a21882af9a65a1aa53a5f7374a9a0e258

## A Requirement to issue activities

### FR-02 Patient Search

- Title: Implement patient lookup (FR-02)
- Context: Patient registration is working, but the patient search function is incomplete.
- Requirement: Complete PatientService.find_patient() to search for a registered patient using their ID.
- Acceptance criteria: Return the same stored patient if found, raise LookupError for an unknown ID, and ValueError for a blank ID. Searching should not change stored data.
- Scope: Complete the patient lookup function and add tests.
- Definition of Done: The function is completed, tests pass, another member reviews and approves it, and the changes are merged into main.
- Owner: RachelUC
- Actual issue link: https://github.com/u3325845/st1-assignment-3/issues/2


### FR-03 Practitioner Lookup (Supporting Operation)

- **Title:** Implement practitioner lookup (FR-03 supporting operation)
- **Context:** Practitioner registration is already working in SmartCare, but the practitioner lookup function needed to be completed.
- **Requirement:** Complete `PractitionerService.find_practitioner()` to search for a registered practitioner using their ID.
- **Acceptance criteria:** Return the same stored practitioner if found, raise `LookupError` for an unknown ID and `ValueError` for a blank or invalid ID. Ignore surrounding spaces and do not change stored data.
- **Scope:** Complete the practitioner lookup function and add tests.
- **Definition of Done:** The function is completed, tests pass, another member reviews and approves it, and the changes are merged into `main`.
- **Owner:** Merlin3313611
- **Actual issue link:** [Issue #6](https://github.com/u3325845/st1-assignment-3/issues/6)

### FR-06 Appointment Cancellation with FR-07 retained history

- Title: [response]
- Context: [response]
- Requirement: [response]
- Acceptance criteria: [response]
- Scope: [response]
- Definition of Done: [response]
- Owner: [response]
- Actual issue link: [response]

## B Commit quality

| Original example | Strong or Weak | Reason |
|---|---|---|
| changes | [select] | [response] |
| final version | [select] | [response] |
| Add patient search by ID | [select] | [response] |
| fix stuff | [select] | [response] |
| Prevent cancellation of completed appointments | [select] | [response] |

## C Over scoped PR review

A cancellation PR also renames unrelated patient fields, restructures unrelated code and adds a new dependency.

- Scope concerns: [response]
- Responsibility and architecture concerns: [response]
- Testing and review concerns: [response]
- Changes to remove or separate, with reasons: [response]

## D Challenge a weak Copilot review

GitHub Copilot says: "Looks good; tests pass."

- Missing evidence: [response]
- Follow-up review question 1: [response]
- Follow-up review question 2: [response]
- Follow-up review question 3: [response]
- Follow-up review question 4: [response]
- Follow-up review question 5: [response]
- Additional questions if useful: [response]

## E Team workflow agreement

| Practice | Team agreement |
|---|---|
| Branch naming | [response] |
| Commit message convention | [response] |
| PR size | [response] |
| Another-member review requirement | [response] |
| Merge rule | [response] |
| Significant Copilot disclosure rule | [response] |

## F Issue and backlog index

Create at least two focused issues. Add a linked practitioner-lookup issue or an explicit supporting criterion with the tutor if needed to cover all three service targets.

| Issue link | Requirement | Owner | Acceptance criteria or precise link | Status |
|---|---|---|---|---|
| [Issue #2](https://github.com/u3325845/st1-assignment-3/issues/2) | FR-02 Patient Lookup | RachelUC | Return stored patient; unknown ID raises `LookupError`; blank ID raises `ValueError`. | Completed (PR #3 merged) |
| [Issue #6](https://github.com/u3325845/st1-assignment-3/issues/6) | FR-03 supporting operation — Practitioner lookup | Merlin3313611 | Return the original stored practitioner for a valid ID; raise `LookupError` for unknown IDs and `ValueError` for invalid IDs; ignore surrounding spaces; do not modify stored data. | Closed — completed in [PR #5](https://github.com/u3325845/st1-assignment-3/pull/5) |
| [issue 2] | [response] | [response] | [response] | [response] |
## G Pull request evidence

Repeat this block per PR. Record actual events, not planned approvals.

### PR #3 – Patient Lookup (FR-02)

- PR link and title: https://github.com/u3325845/st1-assignment-3/pull/3 – Patient Lookup
- Linked issue and requirement: Issue #2 – FR-02
- Feature branch: `feature/fr02-patient-lookup`
- Changed behaviour: Implemented patient lookup by ID, returning the stored patient and raising errors for unknown or blank IDs.
- Meaningful commit: `93dbbf6`
- Test command, directory and observed result: `python -m pytest -v` from `project/` – 11 tests passed.
- Another-member reviewer: `Merlin3313611`
- Human observations recorded before Copilot: Retrospective human review of FR-02 Patient Lookup, recorded on 3 November 2026, after PR #3 was merged and before the additional Copilot review. Evidence: https://github.com/u3325845/st1-assignment-3/issues/2#issuecomment-6599736615
- Requirement, responsibilities, test assertions and unrelated-scope checks: Checked the patient lookup requirements, including returning the same stored object, handling unknown and blank IDs, and keeping the changes focused on FR-02.
- Key feedback: The reviewer commented "looks good" and approved the changes. No issues or changes were requested.
- Author response/change and verification: No changes were needed after the review. All 11 tests had passed before merging.
- Reviewer recheck and approval: https://github.com/u3325845/st1-assignment-3/pull/3 – Approved by Merlin3313611.
- Merge outcome and SHA: Successfully merged into main, SHA e744281.
- Significant Copilot assistance: A retrospective GitHub Copilot review was completed on 3 November 2026. Copilot confirmed that Patient Lookup meets the main FR-02 requirements but suggested additional tests for whitespace trimming, case sensitivity, empty-string IDs and unchanged stored data. It also identified an outdated docstring reference. These suggestions will be considered in Stage 7. No code changes were made during the review. Evidence: [GitHub Copilot review](https://github.com/copilot/share/407b5392-0860-80a1-a952-d804843600e5).
- Linked issue closure: Issue #2 – Closed. https://github.com/u3325845/st1-assignment-3/issues/2
- Each member updated main: RachelUC, Merlin3313611 and TarnimaKhan22 – confirmed. u3325845 (Novera) – awaiting confirmation.
- Integrated verification after merge: Patient Lookup verification: `python -m pytest -v` from `project/` – 11 tests passed. Merge SHA: `e744281`. Final integrated test run after merge not separately recorded.


#### Practitioner Lookup 

- **PR link and title:** [PR #5 - Implement practitioner lookup and add tests](https://github.com/u3325845/st1-assignment-3/pull/5)
- **Linked issue and requirement:** [Issue #6](https://github.com/u3325845/st1-assignment-3/issues/6) - FR-03 supporting operation, practitioner lookup. Issue documented after implementation.
- **Feature branch:** `feature/fr03-practitioner-lookup`
- **Changed behaviour:** Implemented `PractitionerService.find_practitioner()` to return the existing stored practitioner by ID. Unknown IDs raise `LookupError`, while blank or invalid IDs raise `ValueError` through the data store's existing validation.
- **Meaningful commits:** [`1cc43b5`](https://github.com/u3325845/st1-assignment-3/commit/1cc43b5) - Implement practitioner lookup and add tests.
- **Test command, directory and observed result:** `python -m pytest` from `project/` — 16 tests passed.
- **Another-member reviewer:** RachelUC.
- **Human observations recorded before Copilot:** I manually checked the practitioner lookup implementation, data store validation, test coverage and scope before PR #5 was merged. RachelUC reviewed and approved PR #5. The additional Copilot review was conducted retrospectively on 3 November 2026, after the PR had been merged.
- **Requirement, responsibilities, test assertions and unrelated-scope checks:** Checked the service and data store responsibilities. Added five tests covering existing, unknown, blank, whitespace-padded and case-sensitive IDs. PR changed only the practitioner service implementation and its test file.
- **Key feedback:** RachelUC reviewed and approved PR #5, commenting that the changes looked good. No specific defects or changes were requested.
- **Author response/change and verification:** Verified the implementation with 16 passing tests.
- **Reviewer recheck and approval:** RachelUC approved [PR #5](https://github.com/u3325845/st1-assignment-3/pull/5).
- **Merge outcome and SHA:** PR #5 merged into `main`; integrated `main` SHA: `fed883f`.
- **Significant Copilot assistance:** GitHub Copilot was not used during the original implementation or approval of PR #5. A retrospective Copilot review was conducted on 3 November 2026. It found no blocking functional defects but suggested additional tests for invalid IDs and unchanged stored data, as well as updating an outdated docstring. The findings and human decisions are recorded in Sections H and I.
- **Linked issue closure:** Issue #6 closed, with a link to completed PR #5.
- **Each member updated main:** Merlin3313611, RachelUC and TarnimaKhan22 confirmed they pulled the latest `main`. u3325845 (Novera) - confirmation pending.
- **Integrated verification after merge:** `python -m pytest` from `project/` — 16 tests passed on `main` at `fed883f`. Working tree clean.

## H Copilot collaboration record

Record meaningful required use, not every trivial completion. Repeat per significant interaction.

- Member and task: RachelUC – FR-02 Patient Lookup review.
- Prompt/purpose and relevant issue/diff: Asked Copilot to review my Patient Lookup implementation and tests against FR-02 requirements. [PR #3](https://github.com/u3325845/st1-assignment-3/pull/3).
- Summary of output: Copilot found the implementation correct but suggested extra tests for whitespace, case sensitivity, empty IDs and unchanged stored data. It also noticed an outdated docstring.
- Human check against actual code, requirements and tests: I compared Copilot's suggestions with my code and tests. My earlier human review had also identified missing whitespace and case-sensitivity tests.
- Decision — Accept / Modify / Reject: Modify
- Reason: I accepted the additional testing suggestions for Stage 7 but kept my working Stage 6 code unchanged.
- Verification/evidence: [GitHub Copilot review](https://github.com/copilot/share/407b5392-0860-80a1-a952-d804843600e5). Retrospective review completed on 3 November 2026. Earlier test result: 11 passed.



#### Practitioner Lookup

- **Member and task:** Merlin3313611 - GitHub Copilot review of practitioner lookup, PR #5.
- **Prompt/purpose and relevant issue/diff:** Asked Copilot to review [PR #5](https://github.com/u3325845/st1-assignment-3/pull/5) for requirement compliance, error handling, service responsibilities, test coverage and unrelated changes.
- **Summary of output:** Copilot found no blocking functional defects. It identified three improvements: an outdated docstring mentioning `NotImplementedError`, missing tests for empty and non-string IDs, and missing assertions that failed lookups do not modify stored records.
- **Human check against actual code, requirements and tests:** Confirmed that the data store already handles ID validation and whitespace trimming. My original five tests covered existing, unknown, whitespace-only, whitespace-padded and case-sensitive IDs. TarnimaKhan22's approved additional tests cover empty and non-string IDs and confirm that failed lookups preserve registered practitioners.
- **Decision - Accept / Modify / Reject:** Accept Copilot's suggestions for additional test coverage, which TarnimaKhan22's approved tests address. Accept the suggestion to update the outdated docstring as a future improvement. No duplicate validation is needed in the service because the data store already handles it.
- **Reason:** Copilot found no functional defects. The additional approved tests address both coverage gaps. The outdated docstring remains a minor documentation issue.
- **Verification/evidence:** [PR #5](https://github.com/u3325845/st1-assignment-3/pull/5). All 16 tests passed when the PR was merged. Copilot reviewed the PR after it was merged; its suggestions were not part of the original approval.

## I Human versus Copilot review comparison

- Human reviewer noticed before consulting Copilot: The existing tests did not explicitly cover whitespace trimming or case sensitivity. Recorded retrospectively after merging. [Human review evidence](https://github.com/u3325845/st1-assignment-3/issues/2#issuecomment-6599736615).
- Copilot noticed: Missing tests for whitespace, case sensitivity, empty IDs and unchanged stored data, along with an outdated docstring.
- Overlap: Both identified missing whitespace and case-sensitivity tests.
- What did the human reviewer notice that Copilot did not: No additional issue was identified in my human review.
- What did Copilot identify that the human reviewer initially missed: Additional tests for empty IDs and unchanged stored data, and the outdated docstring.
- Unsupported or incorrect Copilot suggestion: None identified from the review.
- Human judgement accepted, modified or rejected, and why: I accepted the extra testing suggestions for Stage 7 because they would improve test coverage. I kept the Stage 6 implementation unchanged because it was already working.
- Which evidence justified merge approval: The original three Patient Lookup tests passed, the full suite reported 11 passed, and Merlin3313611 approved PR #3. The Copilot review was completed after merging and did not contribute to the original approval.



#### Practitioner Lookup 

- **Human reviewer noticed before consulting Copilot:** RachelUC reviewed and approved PR #5, commenting that the changes looked good. No specific defects were recorded.
- **Copilot noticed:** No blocking functional defects. Copilot identified an outdated `NotImplementedError` docstring, missing tests for empty and non-string IDs, and missing explicit assertions that failed lookups preserve stored records.
- **Overlap:** Both reviews found no blocking problems with the practitioner lookup implementation.
- **What did human notice Copilot did not:** No additional findings were documented in RachelUC's review.
- **What did Copilot identify human initially missed:** The outdated docstring and two test coverage gaps were not mentioned in RachelUC's review.
- **Unsupported or incorrect Copilot suggestion:** None identified. Copilot correctly recognised that input validation belongs in the data store and should not be duplicated in the service.
- **Human judgement accepted, modified or rejected, and why:** Accepted the additional test coverage suggestions, which TarnimaKhan22's approved tests address. Accepted the docstring update as a future improvement. No changes to the lookup implementation were required.
- **Which evidence justified merge approval:** RachelUC's approval of [PR #5](https://github.com/u3325845/st1-assignment-3/pull/5), the focused code changes and 16 passing tests. Copilot's review occurred after the merge and did not contribute to the original approval.


## J Contributions

Repeat per member. Include only categories that describe actual work; write not applicable where appropriate. Pairing or mentoring can be supported by a short corroborated note.

### Member: RachelUC (u3331755)

- Member: RachelUC
- Implementation: Implemented `PatientService.find_patient()` to search for registered patients and handle invalid or unknown IDs. Evidence: PR #3.
- Testing: Created three tests for existing, unknown and blank patient IDs in `test_patient_lookup.py`. All 11 tests passed.
- Review: Submitted PR #3, which was reviewed and approved by Merlin3313611.
- Issue refinement: Created Issue #2 for FR-02 with acceptance criteria and Definition of Done.
- Design and responsibility discussion: Used the shared data store for patient lookup and kept the changes focused on FR-02.
- Debugging or integration: Pulled the latest `main` after merging my Patient Lookup changes.
- Documentation or team support: Completed the FR-02 requirements and evidence in the Stage 6 Markdown, including a retrospective human and Copilot review.


#### Practitioner Lookup

- **Member:** Merlin3313611
- **Implementation:** Implemented `PractitionerService.find_practitioner()` in `project/smartcare/services.py`. The function returns the stored practitioner and raises `LookupError` for unknown IDs. Evidence: [PR #5](https://github.com/u3325845/st1-assignment-3/pull/5).
- **Testing:** Added five tests covering existing IDs, unknown IDs, blank IDs, surrounding spaces and case sensitivity. Ran `python -m pytest` from `project/` — 16 tests passed.
- **Review:** Reviewed and approved RachelUC's and TarnimaKhan22's pull requests, including code, tests and Stage 6 documentation.
- **Issue refinement:** Created [Issue #6](https://github.com/u3325845/st1-assignment-3/issues/6) for practitioner lookup as an FR-03 supporting operation and linked it to PR #5.
- **Design and responsibility discussion:** Checked that the service uses the data store for validation and lookup instead of duplicating validation logic.
- **Debugging or integration:** Pulled the updated `main` after PR #5 was merged and confirmed all 16 tests passed.
- **Documentation or team support:** Added my practitioner lookup evidence to Sections A, F, G, H, I and J. Reviewed RachelUC's Stage 6 documentation and checked TarnimaKhan22's additional tests against Copilot's findings.

## K Exit question

Why is a high commit count not necessarily evidence of strong contribution?

[response]

## L Stage 6 formative questions

1. What is version control?

[response]

2. Why is a feature branch useful?

[response]

3. What makes a commit a good engineering commit?

[response]

4. What is a pull request?

[response]

5. What is the purpose of code review?

[response]

6. What does a Git diff show?

[response]

7. What is a Definition of Done?

[response]

8. What is the appropriate role of GitHub Copilot in pull-request review?

[response]

9. Why should individual contribution not be judged only by commit count?

[response]

10. What is the Stage 6 engineering rule?

[response]

## M Completion and handover

- Starting SHA: [response]
- Final Stage 6 code SHA: [response]
- Test command: [response]
- Working directory: [response]
- Observed result: [response]
- PR and another-member reviewer: [links]
- Unresolved issue or none: [response]
- Stage 7 handover status: [ready for tutor checkpoint / unresolved work]
- Final submitted SHA if later than tested SHA: [response and evidence-only difference]

- [ ] Three Stage 6 service targets completed and checked.
- [ ] Original supplied tests retained and passing.
- [ ] At least two focused issues link requirements and acceptance criteria.
- [ ] Feature work reviewed by another member using the actual diff.
- [ ] Human-first review and required Copilot comparison recorded.
- [ ] Feedback resolved and approval recorded before merge.
- [ ] Everyone pulled main and integrated checks passed.
- [ ] Required activities, quiz responses and contribution notes completed.
- [ ] Only synthetic data included; confidential peer material kept out.
- [ ] Tutor can trace a requirement through issue, code, tests, PR and checkpoint.

Do not write a file's own future commit SHA into that file. Record the tested code SHA first, then commit the evidence; explain the difference when submitting.
