from datetime import datetime

import pytest

from smartcare.data_store import SmartCareDataStore
from smartcare.domain import Appointment, AppointmentStatus
from smartcare.services import (
    AppointmentService,
    PatientService,
    PractitionerService,
)


def make_booked_appointment():
    """Return the appointment service and one booked SCHEDULED appointment."""
    store = SmartCareDataStore()
    patients = PatientService(store)
    practitioners = PractitionerService(store)
    appointments = AppointmentService(store)

    patients.register_patient("P1", "Alex")
    practitioners.register_practitioner("D1", "Taylor", "General Practitioner")
    appointment = appointments.book_appointment(
        "A1", "P1", "D1", datetime(2026, 10, 1, 9, 0)
    )
    return appointments, appointment


def test_cancel_scheduled_appointment_sets_cancelled_and_returns_same_object():
    service, appointment = make_booked_appointment()

    result = service.cancel_appointment("A1")

    assert result is appointment
    assert result.status == AppointmentStatus.CANCELLED



def test_cancel_unknown_appointment_id_raises_lookup_error():
    service, appointment = make_booked_appointment()

    with pytest.raises(LookupError):
        service.cancel_appointment("A999")

    assert appointment.status == AppointmentStatus.SCHEDULED


def test_cancel_blank_id_raises_value_error():
    service, appointment = make_booked_appointment()

    with pytest.raises(ValueError):
        service.cancel_appointment("")

    assert appointment.status == AppointmentStatus.SCHEDULED


def test_cancel_spaces_only_id_raises_value_error():
    service, appointment = make_booked_appointment()

    with pytest.raises(ValueError):
        service.cancel_appointment("   ")

    assert appointment.status == AppointmentStatus.SCHEDULED


def test_cancel_none_id_raises_value_error():
    service, appointment = make_booked_appointment()

    with pytest.raises(ValueError):
        service.cancel_appointment(None)

    assert appointment.status == AppointmentStatus.SCHEDULED


def test_cancel_completed_appointment_raises_value_error():
    service, _ = make_booked_appointment()
    store = service.data_store
    patient = store.find_patient("P1")
    practitioner = store.find_practitioner("D1")
    time = datetime(2026, 10, 1, 10, 0)

    completed = Appointment(
        "A2", patient, practitioner, time, AppointmentStatus.COMPLETED
    )
    store.add_appointment(completed)

    with pytest.raises(ValueError):
        service.cancel_appointment("A2")

    assert completed.status == AppointmentStatus.COMPLETED


def test_cancelling_one_appointment_leaves_other_unchanged():
    service, first = make_booked_appointment()
    second = service.book_appointment(
        "A2", "P1", "D1", datetime(2026, 10, 1, 10, 0)
    )

    service.cancel_appointment("A1")

    assert first.status == AppointmentStatus.CANCELLED
    assert second.status == AppointmentStatus.SCHEDULED




# Stage 9 - Practitioner appointment listing

def test_list_practitioner_appointments_returns_booked_appointment():
    service, appointment = make_booked_appointment()

    result = service.list_practitioner_appointments("D1")

    assert result == [appointment]
    assert result[0] is appointment



def test_list_practitioner_appointments_no_appointments():
    store = SmartCareDataStore()
    practitioners = PractitionerService(store)
    service = AppointmentService(store)

    practitioners.register_practitioner("D1", "Taylor", "General")

    result = service.list_practitioner_appointments("D1")

    assert result == []


def test_list_practitioner_appointments_unknown_practitioner():
    service, appointment = make_booked_appointment()

    with pytest.raises(LookupError):
        service.list_practitioner_appointments("D999")

    assert service.find_appointment("A1") is appointment


def test_list_practitioner_appointments_blank_id():
    service, appointment = make_booked_appointment()

    with pytest.raises(ValueError):
        service.list_practitioner_appointments("   ")

    assert service.find_appointment("A1") is appointment


def test_list_practitioner_appointments_invalid_id():
    service, appointment = make_booked_appointment()

    with pytest.raises(ValueError):
        service.list_practitioner_appointments(None)

    assert service.find_appointment("A1") is appointment


def test_list_practitioner_appointments_invalid_status():
    service, appointment = make_booked_appointment()

    with pytest.raises(ValueError):
        service.list_practitioner_appointments("D1", "INVALID")

    assert service.find_appointment("A1") is appointment
    assert appointment.status == AppointmentStatus.SCHEDULED


def test_list_practitioner_appointments_filters_cancelled():
    service, first = make_booked_appointment()

    second = service.book_appointment(
        "A2", "P1", "D1", datetime(2026, 10, 1, 10, 0)
    )

    service.cancel_appointment("A1")

    result = service.list_practitioner_appointments(
        "D1", AppointmentStatus.CANCELLED
    )

    assert result == [first]
    assert first.status == AppointmentStatus.CANCELLED
    assert second.status == AppointmentStatus.SCHEDULED


def test_list_practitioner_appointments_includes_all_statuses():
    service, first = make_booked_appointment()

    second = service.book_appointment(
        "A2", "P1", "D1", datetime(2026, 10, 1, 10, 0)
    )

    service.cancel_appointment("A1")

    result = service.list_practitioner_appointments("D1")

    assert result == [first, second]
    assert first.status == AppointmentStatus.CANCELLED
    assert second.status == AppointmentStatus.SCHEDULED
    assert service.find_appointment("A1") is first



def test_list_practitioner_appointments_only_own_practitioner():
    service, first = make_booked_appointment()

    practitioners = PractitionerService(service.data_store)
    practitioners.register_practitioner("D2", "Alex", "General")

    second = service.book_appointment(
        "A2", "P1", "D2", datetime(2026, 10, 1, 10, 0)
    )

    result = service.list_practitioner_appointments("D1")

    assert result == [first]
    assert second not in result



def test_list_practitioner_appointments_filters_scheduled():
    service, first = make_booked_appointment()

    second = service.book_appointment(
        "A2", "P1", "D1", datetime(2026, 10, 1, 10, 0)
    )

    service.cancel_appointment("A1")

    result = service.list_practitioner_appointments(
        "D1", AppointmentStatus.SCHEDULED
    )

    assert result == [second]
    assert first not in result
    assert first.status == AppointmentStatus.CANCELLED
