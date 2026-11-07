# Stage 9 - Query Tests (Merlin)
# QRY-01 to QRY-04 and FP-01 to FP-03

from datetime import datetime

from smartcare.domain import Appointment, Patient, Practitioner, AppointmentStatus
from smartcare.queries import appointment_sort_key, select_appointments

# T9-QRY-01: Verify the sorting key returns date/time and appointment ID.
def test_appointment_sort_key():
    patient = Patient("P1", "Alex")
    practitioner = Practitioner("DR1", "Taylor", "General")

    appointment = Appointment(
        "A1",
        patient,
        practitioner,
        datetime(2026, 11, 10, 9, 30),
    )

    result = appointment_sort_key(appointment)

    assert result == (datetime(2026, 11, 10, 9, 30), "A1")


# TEST-QRY-02: Return only appointments for the selected practitioner.
def test_select_appointments_filters_by_practitioner():
    patient = Patient("P1", "Alex")
    doctor1 = Practitioner("D1", "Taylor", "General")
    doctor2 = Practitioner("D2", "Smith", "Cardiology")

    appointment1 = Appointment(
        "A1", patient, doctor1, datetime(2026, 11, 10, 9, 30)
    )
    appointment2 = Appointment(
        "A2", patient, doctor2, datetime(2026, 11, 10, 10, 30)
    )

    result = select_appointments([appointment1, appointment2], "D1")

    assert result == [appointment1]



# TEST-QRY-03: Filter appointments by status.
def test_select_appointments_filters_by_status():
    patient = Patient("P1", "Alex")
    practitioner = Practitioner("D1", "Taylor", "General")

    appointment1 = Appointment(
        "A1", patient, practitioner, datetime(2026, 11, 10, 9, 30)
    )
    appointment2 = Appointment(
        "A2", patient, practitioner, datetime(2026, 11, 10, 10, 30)
    )

    appointment2.cancel()

    result = select_appointments(
        [appointment1, appointment2],
        "D1",
        AppointmentStatus.CANCELLED
    )

    assert result == [appointment2]



# TEST-QRY-04: Sort appointments by date and time.
def test_select_appointments_sorts_by_datetime():
    patient = Patient("P1", "Alex")
    practitioner = Practitioner("D1", "Taylor", "General")

    appointment1 = Appointment(
        "A1", patient, practitioner, datetime(2026, 11, 10, 11, 30)
    )
    appointment2 = Appointment(
        "A2", patient, practitioner, datetime(2026, 11, 10, 9, 30)
    )
    appointment3 = Appointment(
        "A3", patient, practitioner, datetime(2026, 11, 10, 10, 30)
    )

    result = select_appointments(
        [appointment1, appointment2, appointment3], "D1"
    )

    assert result == [appointment2, appointment3, appointment1]



# TEST-QRY-05: Sort by appointment ID when date and time are equal.
def test_select_appointments_sorts_by_id_when_times_equal():
    patient = Patient("P1", "Alex")
    practitioner = Practitioner("D1", "Taylor", "General")

    appointment_b = Appointment(
        "A2", patient, practitioner, datetime(2026, 11, 10, 9, 30)
    )
    appointment_a = Appointment(
        "A1", patient, practitioner, datetime(2026, 11, 10, 9, 30)
    )

    result = select_appointments(
        [appointment_b, appointment_a], "D1"
    )

    assert result == [appointment_a, appointment_b]



# TEST-QRY-06: Return a new list without changing the original.
def test_select_appointments_does_not_modify_original_list():
    patient = Patient("P1", "Alex")
    practitioner = Practitioner("D1", "Taylor", "General")

    appointment1 = Appointment(
        "A1", patient, practitioner, datetime(2026, 11, 10, 11, 30)
    )
    appointment2 = Appointment(
        "A2", patient, practitioner, datetime(2026, 11, 10, 9, 30)
    )

    original = [appointment1, appointment2]

    result = select_appointments(original, "D1")

    assert original == [appointment1, appointment2]
    assert result == [appointment2, appointment1]
    assert result is not original
    assert result[0] is appointment2
    assert result[1] is appointment1


# TEST-QRY-07: Return an empty list when no appointments match.
def test_select_appointments_returns_empty_list():
    patient = Patient("P1", "Alex")
    practitioner = Practitioner("D1", "Taylor", "General")

    appointment = Appointment(
        "A1", patient, practitioner, datetime(2026, 11, 10, 9, 30)
    )

    result = select_appointments([appointment], "D2")

    assert result == []



# TEST-QRY-08: Include all statuses when no status filter is given.
def test_select_appointments_includes_all_statuses():
    patient = Patient("P1", "Alex")
    practitioner = Practitioner("D1", "Taylor", "General")

    scheduled = Appointment(
        "A1", patient, practitioner, datetime(2026, 11, 10, 9, 30)
    )
    cancelled = Appointment(
        "A2", patient, practitioner, datetime(2026, 11, 10, 10, 30)
    )

    cancelled.cancel()

    result = select_appointments(
        [scheduled, cancelled], "D1"
    )

    assert result == [scheduled, cancelled]
    assert cancelled.status is AppointmentStatus.CANCELLED



# TEST-QRY-09: Return an empty list when the input list is empty.
def test_select_appointments_with_empty_input():
    appointments = []

    result = select_appointments(appointments, "D1")

    assert result == []
    assert result is not appointments
