# SmartCare

SmartCare is a small appointment application for a clinic (Assessment 3, Stage 9 checkpoint). It registers patients and practitioners, books and cancels appointments, finds records and lists a practitioner's appointments. All data is synthetic and exists only for the current session.

Requirements baseline: SmartCare A3 2026 revision 2. The program uses only the Python standard library. Tests use pytest 8.3.5 and were run on Python 3.14.7.

## Setup

From the repository root, create and activate a virtual environment, then install the test dependency:

```sh
python -m venv .venv
.venv\Scripts\Activate.ps1
cd project
python -m pip install -r requirements-dev.txt
```

On macOS or Linux, activate with `source .venv/bin/activate` instead.

## Running the program

Run all commands from the `project/` directory.

```sh
python main.py
python main.py --interactive
```

- `python main.py` runs a short demonstration that registers synthetic records and books one appointment.
- `python main.py --interactive` starts the interactive menu.

## Interactive menu

| Option | Action |
|---|---|
| 1 | Register patient |
| 2 | Find patient |
| 3 | Register practitioner |
| 4 | Find practitioner |
| 5 | Book appointment |
| 6 | Cancel appointment |
| 7 | Find appointment |
| 8 | List practitioner appointments |
| 0 | Exit |

Enter booking dates in the exact format `YYYY-MM-DD HH:MM`. Listing accepts an optional status filter (`scheduled`, `cancelled` or `completed`); leave it blank to list all statuses, including cancelled appointments.

Invalid menu choices and expected input errors (blank, unknown or duplicate IDs, malformed or impossible dates, an invalid status, repeated cancellation) show a clear message, do not change stored data, and return to the menu.

Example session:

```text
Choose an option: 1
Patient ID: P1
Patient name: Alex
Patient registered: P1 - Alex
```

## Features

- Register and find patients and practitioners (IDs are trimmed, non-blank and case-sensitive).
- Book appointments with a practitioner at a date and time; a practitioner cannot have two SCHEDULED appointments at the same time, but a different practitioner can.
- Cancel a SCHEDULED appointment. Cancelled appointments stay in the session history and can still be found and listed. A freed time slot can be booked again.
- Find an appointment by ID.
- List one practitioner's appointments in date/time order (ties by appointment ID), optionally filtered by status.

## How the code is organised

- `smartcare/domain.py`: Patient, Practitioner and Appointment, the appointment status values and the guarded cancellation rule.
- `smartcare/data_store.py`: the session store with add, find and list methods.
- `smartcare/services.py`: the services that coordinate the store and domain objects.
- `smartcare/queries.py`: pure functions that filter and sort appointments without changing them.
- `smartcare/console.py`: the interactive menu, date parser and appointment formatter.

Store lookups return `None` for a valid missing ID; service lookups raise `LookupError`. Invalid values, duplicates, conflicts and illegal status changes raise `ValueError`.

## Running the tests

From `project/`:

```sh
python -m pytest -q                                       # full suite
python -m pytest tests/test_workflows.py -q               # console workflow tests
python -m pytest tests/test_console_validation.py -q      # console error-recovery tests
python -m pytest tests/test_queries.py -q                 # query tests
```

## Limitations

- Data is stored in memory only and is lost when the program exits. There is no database and no file persistence.
- There is no rescheduling, no past-date rule, no appointment duration and no patient-conflict rule.
- Use synthetic patient and practitioner information only.