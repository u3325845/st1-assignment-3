from datetime import datetime

import pytest

from smartcare.data_store import SmartCareDataStore
from smartcare.domain import AppointmentStatus
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


def test_cancelled_appointment_is_retained_and_findable():
    service, appointment = make_booked_appointment()

    service.cancel_appointment("A1")

    found = service.find_appointment("A1")
    assert found is appointment
    assert found.status == AppointmentStatus.CANCELLED


def test_cancel_already_cancelled_appointment_raises_value_error():
    service, appointment = make_booked_appointment()
    service.cancel_appointment("A1")

    with pytest.raises(ValueError):
        service.cancel_appointment("A1")

    assert appointment.status == AppointmentStatus.CANCELLED


def test_cancel_unknown_appointment_id_raises_lookup_error():
    service, appointment = make_booked_appointment()

    with pytest.raises(LookupError):
        service.cancel_appointment("A999")

    assert appointment.status == AppointmentStatus.SCHEDULED