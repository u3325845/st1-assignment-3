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

| Issue link | Requirement                                     | Owner | Acceptance criteria or precise link | Status |
|---|-------------------------------------------------|---|-|---|
| [issue 1] | [response]                                      | [response] | [response] | [response] |
| [Issue #6](https://github.com/u3325845/st1-assignment-3/issues/6) | FR-03 supporting operation -Practitioner lookup | Merlin3313611 | Return the original stored practitioner for a valid ID; raise `LookupError` for unknown IDs and `ValueError` for invalid IDs; ignore surrounding spaces; do not modify stored data.| Closed - completed in [PR #5](https://github.com/u3325845/st1-assignment-3/pull/5) |

## G Pull request evidence

Repeat this block per PR. Record actual events, not planned approvals.

- PR link and title: [response]
- Linked issue and requirement: [response]
- Feature branch: [response]
- Changed behaviour: [response]
- Meaningful commits: [links]
- Test command, directory and observed result: [response]
- Another-member reviewer: [response]
- Human observations recorded before Copilot: [link and time]
- Requirement, responsibilities, test assertions and unrelated-scope checks: [response]
- Key feedback: [response]
- Author response/change and verification: [response]
- Reviewer recheck and approval: [link]
- Merge outcome and SHA: [response]
- Significant Copilot assistance: [summary or none]
- Linked issue closure: [response]
- Each member updated main: [member and confirmation]
- Integrated verification after merge: [command, directory, result and code SHA]


#### Practitioner Lookup 

- **PR link and title:** [PR #5 - Implement practitioner lookup and add tests](https://github.com/u3325845/st1-assignment-3/pull/5)
- **Linked issue and requirement:** [Issue #6](https://github.com/u3325845/st1-assignment-3/issues/6) - FR-03 supporting operation, practitioner lookup. Issue documented after implementation.
- **Feature branch:** `feature/fr03-practitioner-lookup`
- **Changed behaviour:** Implemented `PractitionerService.find_practitioner()` to return the existing stored practitioner by ID. Unknown IDs raise `LookupError`, while blank or invalid IDs raise `ValueError` through the data store's existing validation.
- **Meaningful commits:** [`1cc43b5`](https://github.com/u3325845/st1-assignment-3/commit/1cc43b5) - Implement practitioner lookup and add tests.
- **Test command, directory and observed result:** `python -m pytest` from `project/` — 16 tests passed.
- **Another-member reviewer:** RachelUC.
- **Human observations recorded before Copilot:**  I checked the practitioner lookup implementation, data store validation and five tests manually. No Copilot review was performed for this PR.
- **Requirement, responsibilities, test assertions and unrelated-scope checks:** Checked the service and data store responsibilities. Added five tests covering existing, unknown, blank, whitespace-padded and case-sensitive IDs. PR changed only the practitioner service implementation and its test file.
- **Key feedback:** No specific change-request feedback recorded in the evidence available.
- **Author response/change and verification:** Verified the implementation with 16 passing tests.
- **Reviewer recheck and approval:** RachelUC approved [PR #5](https://github.com/u3325845/st1-assignment-3/pull/5).
- **Merge outcome and SHA:** PR #5 merged into `main`; integrated `main` SHA: `fed883f`.
- **Significant Copilot assistance:** None. GitHub Copilot was not used for this PR.
- **Linked issue closure:** Issue #6 closed, with a link to completed PR #5.
- **Each member updated main:** Merlin3313611, RachelUC and TarnimaKhan22 confirmed they pulled the latest `main`. u3325845 (Novera) - confirmation pending.
- **Integrated verification after merge:** `python -m pytest` from `project/` — 16 tests passed on `main` at `fed883f`. Working tree clean.

## H Copilot collaboration record

Record meaningful required use, not every trivial completion. Repeat per significant interaction.

- Member and task: [response]
- Prompt/purpose and relevant issue/diff: [response]
- Summary of output: [response]
- Human check against actual code, requirements and tests: [response]
- Decision — Accept / Modify / Reject: [select]
- Reason: [response]
- Verification/evidence: [link and result]


#### Practitioner Lookup

- **Member and task:** Merlin3313611 - GitHub Copilot review of practitioner lookup, PR #5.
- **Prompt/purpose and relevant issue/diff:** Asked Copilot to review [PR #5](https://github.com/u3325845/st1-assignment-3/pull/5) for requirement compliance, error handling, service responsibilities, test coverage and unrelated changes.
- **Summary of output:** Copilot found no blocking functional defects. It identified three improvements: an outdated docstring mentioning `NotImplementedError`, missing tests for empty and non-string IDs, and missing assertions that failed lookups do not modify stored records.
- **Human check against actual code, requirements and tests:** Confirmed that the data store already handles ID validation and whitespace trimming. My original five tests covered existing, unknown, whitespace-only, whitespace-padded and case-sensitive IDs. TarnimaKhan22's approved additional tests cover empty and non-string IDs and confirm that failed lookups preserve registered practitioners.
- **Decision - Accept / Modify / Reject:** Accept Copilot's suggestions for additional test coverage, which TarnimaKhan22's approved tests address. Accept the suggestion to update the outdated docstring as a future improvement. No duplicate validation is needed in the service because the data store already handles it.
- **Reason:** Copilot found no functional defects. The additional approved tests address both coverage gaps. The outdated docstring remains a minor documentation issue.
- **Verification/evidence:** [PR #5](https://github.com/u3325845/st1-assignment-3/pull/5). All 16 tests passed when the PR was merged. Copilot reviewed the PR after it was merged; its suggestions were not part of the original approval.

## I Human versus Copilot review comparison

- Human reviewer noticed before consulting Copilot: [response]
- Copilot noticed: [response]
- Overlap: [response]
- What did the human reviewer notice that Copilot did not: [response]
- What did Copilot identify that the human reviewer initially missed: [response]
- Unsupported or incorrect Copilot suggestion: [response or none identified with explanation]
- Human judgement accepted, modified or rejected, and why: [response]
- Which evidence justified merge approval: [response]



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

- Member: [response]
- Implementation: [work and evidence]
- Testing: [work and evidence]
- Review: [work and evidence]
- Issue refinement: [work and evidence]
- Design and responsibility discussion: [work and evidence]
- Debugging or integration: [work and evidence]
- Documentation or team support: [work and evidence]


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
