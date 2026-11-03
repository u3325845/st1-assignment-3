import pytest

from smartcare.data_store import SmartCareDataStore
from smartcare.services import PractitionerService


def test_find_existing_practitioner():
    store = SmartCareDataStore()
    service = PractitionerService(store)

    practitioner = service.register_practitioner(
        "D1", "Taylor", "General Practice"
    )

    result = service.find_practitioner("D1")

    assert result is practitioner


def test_find_unknown_practitioner():
    store = SmartCareDataStore()
    service = PractitionerService(store)

    with pytest.raises(LookupError):
        service.find_practitioner("D999")

def test_find_blank_practitioner_id():
    store = SmartCareDataStore()
    service = PractitionerService(store)

    with pytest.raises(ValueError):
        service.find_practitioner("   ")


def test_find_practitioner_with_spaces():
    store = SmartCareDataStore()
    service = PractitionerService(store)

    practitioner = service.register_practitioner(
        "D1", "Taylor", "General Practice"
    )

    result = service.find_practitioner("  D1  ")

    assert result is practitioner

def test_find_practitioner_case_sensitive():
    store = SmartCareDataStore()
    service = PractitionerService(store)

    service.register_practitioner(
        "D1", "Taylor", "General Practice"
    )

    with pytest.raises(LookupError):
        service.find_practitioner("d1")


# Stage 7

def test_duplicate_practitioner_id_rejected():
    store = SmartCareDataStore()
    service = PractitionerService(store)

    original = service.register_practitioner(
        "D1", "Taylor", "General Practice"
    )

    with pytest.raises(ValueError):
        service.register_practitioner(
            "D1", "Morgan", "Cardiology"
        )

    assert service.find_practitioner("D1") is original
    assert store.list_practitioners() == [original]

def test_practitioner_rejects_whitespace_only_name():
        store = SmartCareDataStore()
        service = PractitionerService(store)

        with pytest.raises(ValueError):
            service.register_practitioner(
                "D2", "   ", "Cardiology"
            )

        assert store.list_practitioners() == []

def test_practitioner_rejects_whitespace_only_specialty():
    store = SmartCareDataStore()
    service = PractitionerService(store)

    with pytest.raises(ValueError):
        service.register_practitioner(
            "D3", "Morgan", "   "
        )

    assert store.list_practitioners() == []


def test_failed_practitioner_registration_preserves_records():
    store = SmartCareDataStore()
    service = PractitionerService(store)

    original = service.register_practitioner(
        "D1", "Taylor", "General Practice"
    )

    with pytest.raises(ValueError):
        service.register_practitioner(
            "D2", "   ", "Cardiology"
        )

    assert service.find_practitioner("D1") is original
    assert store.list_practitioners() == [original]

def test_practitioner_registration_stores_correct_details():
    store = SmartCareDataStore()
    service = PractitionerService(store)

    practitioner = service.register_practitioner(
        "D5", "Taylor", "General Practice"
    )

    assert practitioner.practitioner_id == "D5"
    assert practitioner.name == "Taylor"
    assert practitioner.specialty == "General Practice"
    assert service.find_practitioner("D5") is practitioner
    assert store.list_practitioners() == [practitioner]
    assert store.list_practitioners() == [practitioner]