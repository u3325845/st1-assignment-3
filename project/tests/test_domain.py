import pytest
from datetime import datetime, timezone

from smartcare.domain import Patient, Practitioner, Appointment, AppointmentStatus
# Stage 7 - Patient Domain Tests (Rachel)


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



# Stage 7 - Practitioner Domain Tests (Merlin)

# TEST-PRAC-DOM-01: Check valid practitioner details.
def test_practitioner_created_with_valid_details():
    practitioner = Practitioner("D1", "Dr Smith", "General Practice")

    assert practitioner.practitioner_id == "D1"
    assert practitioner.name == "Dr Smith"
    assert practitioner.specialty == "General Practice"


# TEST-PRAC-DOM-02: Check that extra spaces are removed.
def test_practitioner_details_are_trimmed():
    practitioner = Practitioner("  D1  ", "  Dr Smith  ", "  Cardiology  ")

    assert practitioner.practitioner_id == "D1"
    assert practitioner.name == "Dr Smith"
    assert practitioner.specialty == "Cardiology"


# TEST-PRAC-DOM-03: Check that blank IDs are rejected.
@pytest.mark.parametrize("invalid_id", ["", "   ", "\t", "\n"])
def test_practitioner_rejects_blank_id(invalid_id):
    with pytest.raises(ValueError, match="Practitioner ID cannot be blank"):
        Practitioner(invalid_id, "Dr Smith", "Cardiology")


# TEST-PRAC-DOM-04: Check that whitespace-only names are rejected.
@pytest.mark.parametrize("invalid_name", ["", "   ", "\t", "\n"])
def test_practitioner_rejects_whitespace_name(invalid_name):
    with pytest.raises(ValueError, match="Practitioner name cannot be blank"):
        Practitioner("D1", invalid_name, "Cardiology")

# TEST-PRAC-DOM-05: Check that whitespace-only specialties are rejected.
@pytest.mark.parametrize("invalid_specialty", ["", "   ", "\t", "\n"])
def test_practitioner_rejects_whitespace_specialty(invalid_specialty):
    with pytest.raises(ValueError, match="Specialty cannot be blank"):
        Practitioner("D1", "Taylor", invalid_specialty)


# TEST-PRAC-DOM-06: Check that non-string fields are rejected.
@pytest.mark.parametrize(
    "practitioner_id, name, specialty, expected_message",
    [
        (None, "Dr Smith", "Cardiology", "Practitioner ID cannot be blank"),
        (123, "Dr Smith", "Cardiology", "Practitioner ID cannot be blank"),
        ("D1", None, "Cardiology", "Practitioner name cannot be blank"),
        ("D1", 123, "Cardiology", "Practitioner name cannot be blank"),
        ("D1", "Dr Smith", None, "Specialty cannot be blank"),
        ("D1", "Dr Smith", 123, "Specialty cannot be blank"),
    ],
)
def test_practitioner_rejects_non_string_details(
    practitioner_id, name, specialty, expected_message
):
    with pytest.raises(ValueError, match=expected_message):
        Practitioner(practitioner_id, name, specialty)


# TEST-PRAC-DOM-07: Check that practitioner ID is read-only.
def test_practitioner_id_is_read_only():
    practitioner = Practitioner("D1", "Dr Smith", "Cardiology")

    with pytest.raises(AttributeError):
        practitioner.practitioner_id = "D2"

    assert practitioner.practitioner_id == "D1"


# TEST-PRAC-DOM-08: Check that one-character fields are accepted.
def test_practitioner_accepts_one_character_details():
    practitioner = Practitioner("D", "A", "C")

    assert practitioner.practitioner_id == "D"
    assert practitioner.name == "A"
    assert practitioner.specialty == "C"


# TEST-PRAC-DOM-09: Practitioner trims mixed whitespace
def test_practitioner_trims_mixed_whitespace():
    practitioner = Practitioner(
        "\tD1\n",
        "\tDr Smith \n",
        "\nCardiology\t"
    )

    assert practitioner.practitioner_id == "D1"
    assert practitioner.name == "Dr Smith"
    assert practitioner.specialty == "Cardiology"


# Stage 7 - Appointment Domain Tests (Tarnima)

# T7-TK-01: Verify valid Appointment construction.
def test_appointment_construction_preserves_valid_details():
    patient = Patient("P1", "Alex")
    practitioner = Practitioner("D1", "Taylor", "General")
    appointment_time = datetime(2026, 11, 10, 9, 30)

    appointment = Appointment(
        "A1", patient, practitioner, appointment_time
    )

    assert appointment.appointment_id == "A1"
    assert appointment.patient is patient
    assert appointment.practitioner is practitioner
    assert appointment.date_time == appointment_time


# T7-TK-02: Verify a new Appointment defaults to SCHEDULED.
def test_new_appointment_defaults_to_scheduled():
    patient = Patient("P1", "Alex")
    practitioner = Practitioner("D1", "Taylor", "General")

    appointment = Appointment(
        "A1",
        patient,
        practitioner,
        datetime(2026, 11, 10, 9, 30)
    )

    assert appointment.status is AppointmentStatus.SCHEDULED


# T7-TK-03: Reject blank and whitespace-only Appointment IDs.
@pytest.mark.parametrize("invalid_id", ["", "   ", "\t", "\n"])
def test_appointment_rejects_blank_id(invalid_id):
    patient = Patient("P1", "Alex")
    practitioner = Practitioner("D1", "Taylor", "General")
    appointment_time = datetime(2026, 11, 10, 9, 30)

    with pytest.raises(ValueError, match="Appointment ID cannot be blank"):
        Appointment(
            invalid_id,
            patient,
            practitioner,
            appointment_time
        )


# T7-TK-04: Verify surrounding whitespace is removed from Appointment IDs.
def test_appointment_id_is_trimmed():
    patient = Patient("P1", "Alex")
    practitioner = Practitioner("D1", "Taylor", "General")

    appointment = Appointment(
        "  A1  ",
        patient,
        practitioner,
        datetime(2026, 11, 10, 9, 30)
    )

    assert appointment.appointment_id == "A1"


# T7-TK-05: Reject invalid Patient objects in Appointment construction.
@pytest.mark.parametrize("invalid_patient", [None, "P1", 123])
def test_appointment_rejects_invalid_patient(invalid_patient):
    practitioner = Practitioner("D1", "Taylor", "General")
    appointment_time = datetime(2026, 11, 10, 9, 30)

    with pytest.raises(
        ValueError, match="Appointment requires a Patient object"
    ):
        Appointment(
            "A1",
            invalid_patient,
            practitioner,
            appointment_time
        )


# T7-TK-06: Reject invalid Practitioner objects in Appointment construction.
@pytest.mark.parametrize("invalid_practitioner", [None, "D1", 123])
def test_appointment_rejects_invalid_practitioner(invalid_practitioner):
    patient = Patient("P1", "Alex")
    appointment_time = datetime(2026, 11, 10, 9, 30)

    with pytest.raises(
        ValueError, match="Appointment requires a Practitioner object"
    ):
        Appointment(
            "A1",
            patient,
            invalid_practitioner,
            appointment_time
        )


# T7-TK-07: Reject invalid Appointment status values.
@pytest.mark.parametrize("invalid_status", [None, "scheduled", 123])
def test_appointment_rejects_invalid_status(invalid_status):
    patient = Patient("P1", "Alex")
    practitioner = Practitioner("D1", "Taylor", "General")
    appointment_time = datetime(2026, 11, 10, 9, 30)

    with pytest.raises(ValueError, match="Invalid appointment status"):
        Appointment(
            "A1",
            patient,
            practitioner,
            appointment_time,
            status=invalid_status
        )

# T7-TK-08: Reject invalid date/time types.
@pytest.mark.parametrize(
    "invalid_date_time",
    [None, "2026-11-10 09:30", 123]
)
def test_appointment_rejects_invalid_date_time_type(invalid_date_time):
    patient = Patient("P1", "Alex")
    practitioner = Practitioner("D1", "Taylor", "General")

    with pytest.raises(
        ValueError, match="Date/time must be a datetime value"
    ):
        Appointment(
            "A1",
            patient,
            practitioner,
            invalid_date_time
        )


# T7-TK-09: Reject date/time values that violate minute precision or local-time rules.
@pytest.mark.parametrize(
    "invalid_time",
    [
        datetime(2026, 11, 10, 9, 30, 15),
        datetime(2026, 11, 10, 9, 30, 0, 500),
        datetime(2026, 11, 10, 9, 30, tzinfo=timezone.utc),
    ],
)
def test_appointment_rejects_invalid_time_precision(invalid_time):
    patient = Patient("P1", "Alex")
    practitioner = Practitioner("D1", "Taylor", "General")

    with pytest.raises(
        ValueError, match="Use a local date/time at minute precision"
    ):
        Appointment("A1", patient, practitioner, invalid_time)
