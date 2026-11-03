import pytest

from smartcare.data_store import SmartCareDataStore
from smartcare.services import PatientService, PractitionerService


def test_patient_lookup_trims_surrounding_spaces():
    store = SmartCareDataStore()
    service = PatientService(store)
    patient = service.register_patient("P1", "Alex")

    result = service.find_patient("  P1  ")

    assert result is patient


def test_patient_lookup_is_case_sensitive():
    store = SmartCareDataStore()
    service = PatientService(store)
    patient = service.register_patient("P1", "Alex")

    with pytest.raises(LookupError):
        service.find_patient("p1")

    assert service.find_patient("P1") is patient


@pytest.mark.parametrize("invalid_id", ["", "   ", None, 123])
def test_patient_lookup_rejects_invalid_ids(invalid_id):
    store = SmartCareDataStore()
    service = PatientService(store)

    with pytest.raises(ValueError):
        service.find_patient(invalid_id)

    assert store.list_patients() == []


def test_patient_lookup_preserves_registered_records():
    store = SmartCareDataStore()
    service = PatientService(store)
    first = service.register_patient("P1", "Alex")
    second = service.register_patient("P2", "Sam")

    with pytest.raises(LookupError):
        service.find_patient("P999")

    assert store.list_patients() == [first, second]
    assert service.find_patient("P1") is first
    assert service.find_patient("P2") is second


@pytest.mark.parametrize("invalid_id", ["", "   ", None, 123])
def test_practitioner_lookup_rejects_invalid_ids(invalid_id):
    store = SmartCareDataStore()
    service = PractitionerService(store)

    with pytest.raises(ValueError):
        service.find_practitioner(invalid_id)

    assert store.list_practitioners() == []


def test_practitioner_lookup_preserves_registered_records():
    store = SmartCareDataStore()
    service = PractitionerService(store)
    first = service.register_practitioner(
        "D1", "Taylor", "General Practice"
    )
    second = service.register_practitioner(
        "D2", "Morgan", "Cardiology"
    )

    with pytest.raises(LookupError):
        service.find_practitioner("D999")

    assert store.list_practitioners() == [first, second]
    assert service.find_practitioner("D1") is first
    assert service.find_practitioner("D2") is second


def test_practitioner_lookup_trims_surrounding_spaces():
    store = SmartCareDataStore()
    service = PractitionerService(store)

    practitioner = service.register_practitioner(
        "D1",
        "Taylor",
        "General Practice",
    )

    result = service.find_practitioner("  D1  ")
    assert result is practitioner


def test_practitioner_lookup_is_case_sensitive():
    store = SmartCareDataStore()
    service = PractitionerService(store)

    practitioner = service.register_practitioner(
        "D1",
        "Taylor",
        "General Practice",
    )

    with pytest.raises(LookupError):
        service.find_practitioner("d1")

    assert service.find_practitioner("D1") is practitioner
