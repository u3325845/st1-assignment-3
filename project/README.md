# SmartCare Stage 6 starter

Requirements baseline: SmartCare A3 2026 revision 2. Python 3.13 and pytest 8.3.5 verified. Runtime uses only the standard library.

From this directory, using a Python environment with the development dependency installed:

```sh
python main.py
python -m pytest
```

If needed in your approved environment: `python -m pip install -r requirements-dev.txt`.

The demo registers synthetic records and books/finds an appointment. All supplied tests pass. Data exists only in this session and is lost on exit; FR-10 restart persistence is retired. Use synthetic information only.

`domain.py` contains the entities, status and guarded cancellation. `data_store.py` holds three dictionaries through add/find/list methods. The three services share that object. Supplied registration, booking, appointment lookup and conflict checking work. IDs are trimmed, non-blank and case-sensitive. Properties provide read-only identity/appointment state; changes go through domain methods. No special architecture terminology is required.


Stage 6 patient/practitioner lookup and appointment cancellation are implemented. Stage 9 pure appointment queries and the named sort key are implemented. 
The interactive console menu and practitioner appointment listing service are implemented and integrated. Listing supports optional status filtering and retains cancelled appointment history. No PG rescheduling or assurance solution is supplied.

Service booking accepts IDs and a `datetime` (local, minute precision). Console parser accepts exactly `YYYY-MM-DD HH:MM`. Store lookups return None when absent; service lookups raise LookupError. Invalid values, duplicates, conflicts and illegal transitions raise ValueError. Lists are new containers holding the stored objects. No age, duration, patient-conflict or past-date rules apply.


## Stage 9 Interactive Console

### Interactive console

Start the interactive SmartCare menu from the project directory:

```sh
python main.py --interactive
```

The menu provides the following options:

- 0 — Exit
- 1 — Register patient
- 2 — Find patient
- 3 — Register practitioner
- 4 — Find practitioner
- 5 — Book appointment
- 6 — Cancel appointment
- 7 — Find appointment
- 8 — List practitioner appointments

The console uses one shared in-memory data store for each session.
Records remain available between menu operations but are lost when
the application exits. No database or file persistence is provided.

Enter booking dates in the exact format `YYYY-MM-DD HH:MM`.

Appointment listing supports an optional status filter:
`scheduled`, `cancelled`, or `completed`. Leave the filter blank
to request all statuses, including cancelled appointments.

Invalid menu choices and expected input errors are reported without
ending the session. The console delegates registration, lookup,
booking, cancellation, and listing to the existing services.

Use synthetic patient and practitioner information only.

### Workflow tests

Run the Stage 9 console workflow tests with:

```sh
python -m pytest tests/test_workflows.py -q
```

Run the complete test suite with:

```sh
python -m pytest -q
```
