
import pytest

from smartcare.data_store import SmartCareDataStore
from smartcare.services import PatientService
from smartcare.domain import Patient

def test_find_existing_patient():
    store = SmartCareDataStore()
    service = PatientService(store)

    patient = service.register_patient("P1", "Alex")

    result = service.find_patient("P1")

    assert result is patient


def test_find_unknown_patient():
    store = SmartCareDataStore()
    service = PatientService(store)

    with pytest.raises(LookupError):
        service.find_patient("P999")


def test_find_blank_patient_id():
    store = SmartCareDataStore()
    service = PatientService(store)

    with pytest.raises(ValueError):
        service.find_patient("   ")



# Stage 7 - Patient Domain Tests


# TEST-PAT-01: Check that a patient is created with valid details.
def test_patient_created_with_valid_details():
    patient = Patient("P1", "Alex")

    assert patient.patient_id == "P1"
    assert patient.name == "Alex"


# TEST-PAT-02: Check that extra spaces are removed.
def test_patient_details_are_trimmed():
    patient = Patient("  P1  ", "  Alex  ")

    assert patient.patient_id == "P1"
    assert patient.name == "Alex"



# TEST-PAT-03: Check that empty and whitespace-only IDs are rejected.
@pytest.mark.parametrize("invalid_id", ["", "   ", "\t", "\n"])
def test_patient_rejects_blank_id(invalid_id):
    with pytest.raises(ValueError, match="Patient ID cannot be blank"):
        Patient(invalid_id, "Alex")



# TEST-PAT-04: Check that a name containing only spaces is rejected.
def test_patient_rejects_whitespace_name():
    with pytest.raises(ValueError, match="Patient name cannot be blank"):
        Patient("P1", "   ")




# TEST-PAT-05: Check that non-string details raise the correct error.
@pytest.mark.parametrize(
    "patient_id, name, expected_message",
    [
        (None, "Alex", "Patient ID cannot be blank"),
        (123, "Alex", "Patient ID cannot be blank"),
        ("P1", None, "Patient name cannot be blank"),
        ("P1", 123, "Patient name cannot be blank"),
    ],
)
def test_patient_rejects_non_string_details(patient_id, name, expected_message):
    with pytest.raises(ValueError, match=expected_message):
        Patient(patient_id, name)




# TEST-PAT-06: Check that the patient ID cannot be changed.
def test_patient_id_is_read_only():
    patient = Patient("P1", "Alex")

    with pytest.raises(AttributeError):
        patient.patient_id = "P2"

    assert patient.patient_id == "P1"


# TEST-PAT-07: Check that one-character details are accepted.
def test_patient_accepts_one_character_details():
    patient = Patient("P", "A")

    assert patient.patient_id == "P"
    assert patient.name == "A"
