"""Stage 9 console validation and error-recovery tests (UI-02).

Each test feeds a list of typed answers to run_menu(), then checks the
printed messages. Every test ends with a successful action or a lookup to
show that the menu kept working and that rejected input changed nothing.
"""

from unittest.mock import patch

from smartcare.console import run_menu

# Typed answer that register patient P1 and practitioner DR1.

REGISTER_P1_AND_DR1 = [
    "1", "P1", "Alex",
    "3", "DR1", "Taylor", "General Practice",
]

# Typed answers that also book appointment A1 for P1 with DR1.
BOOK_A1 = REGISTER_P1_AND_DR1 + [
    "5", "A1", "P1", "DR1", "2026-11-20 09:00",
]

A1_SCHEDULED = "A1: P1 with DR1, 2026-11-20 09:00, scheduled"
A1_CANCELLED = "A1: P1 with DR1, 2026-11-20 09:00, cancelled"

def run_session(inputs, capsys):
    """Run the menu with the given typed answers and return its output."""
    with patch("builtins.input", side_effect=inputs):
        run_menu()
    return capsys.readouterr().out

def test_blank_and_text_menu_choices_are_rejected(capsys):
    inputs = ["", "abc", "1", "P1", "Alex", "2", "P1", "0"]

    output = run_session(inputs, capsys)

    assert output.count("Invalid menu option. Please choose 0-8.") == 2
    assert "Patient found: P1 - Alex" in output

def test_blank_patient_id_is_rejected_and_menu_continues(capsys):
    inputs = ["1", "", "Alex", "2", "P1", "1", "P1", "Alex", "2", "P1", "0"]

    output = run_session(inputs, capsys)

    assert "Error: Patient ID cannot be blank" in output
    assert "Error: Patient not found" in output
    assert "Patient found: P1 - Alex" in output

def test_duplicate_patient_is_rejected_and_original_is_kept(capsys):
    inputs = ["1", "P1", "Alex", "1", "P1", "Sam", "2", "P1", "0"]

    output = run_session(inputs, capsys)

    assert "Error: Patient ID already exists" in output
    assert "Patient found: P1 - Alex" in output
    assert "P1 - Sam" not in output

def test_duplicate_practitioner_is_rejected_and_original_is_kept(capsys):
    inputs = [
        "3", "DR1", "Taylor", "General Practice",
        "3", "DR1", "Lee", "General Practice",
        "4", "DR1",
        "0",
    ]

    output = run_session(inputs, capsys)

    assert "Error: Practitioner ID already exists" in output
    assert "Practitioner found: DR1 - Taylor (General Practice)" in output
    assert "DR1 - Lee" not in output

def test_unknown_patient_and_practitioner_lookups_show_errors(capsys):
    inputs = ["2", "P9", "4", "DR9", "1", "P1", "Alex", "2", "P1", "0"]

    output = run_session(inputs, capsys)

    assert "Error: Patient not found" in output
    assert "Error: Practitioner not found" in output
    assert "Patient found: P1 - Alex" in output


def test_malformed_date_is_rejected_and_no_appointment_is_stored(capsys):
    inputs = REGISTER_P1_AND_DR1 + [
        "5", "A1", "P1", "DR1", "not-a-date",
        "7", "A1",
        "5", "A1", "P1", "DR1", "2026-11-20 09:00",
        "7", "A1",
        "0",
    ]

    output = run_session(inputs, capsys)

    assert "Error: Use date/time format YYYY-MM-DD HH:MM" in output
    assert "Error: Appointment not found" in output  # nothing was stored
    assert f"Appointment found: {A1_SCHEDULED}" in output  # later success

def test_impossible_dates_are_rejected_and_no_appointment_is_stored(capsys):
    inputs = REGISTER_P1_AND_DR1 + [
        "5", "A1", "P1", "DR1", "2026-02-30 09:00",
        "5", "A1", "P1", "DR1", "2026-11-20 25:00",
        "7","A1",
        "0",
    ]
    output = run_session(inputs, capsys)
    message = "Error: Invalid calendar date/time; use YYYY-MM-DD HH:MM"
    assert output.count(message) == 2
    assert "Error: Appointment not found" in output

def test_booking_with_unknown_participants_is_rejected(capsys):
    inputs = REGISTER_P1_AND_DR1 + [
        "5", "A1", "P9", "DR1", "2026-11-20 09:00",
        "5", "A1", "P1", "DR9", "2026-11-20 09:00",
        "5", "A1", "P1", "DR1", "2026-11-20 09:00",
        "0",
    ]

    output = run_session(inputs, capsys)

    assert "Error: Patient not found" in output
    assert "Error: Practitioner not found" in output
    assert f"Appointment booked: {A1_SCHEDULED}" in output

def test_blank_and_duplicate_appointment_ids_are_rejected(capsys):
    inputs = REGISTER_P1_AND_DR1 + [
        "5", "", "P1", "DR1", "2026-11-20 09:00",
        "5", "A1", "P1", "DR1", "2026-11-20 09:00",
        "5", "A1", "P1", "DR1", "2026-11-21 10:00",
        "7", "A1",
        "0",
    ]

    output = run_session(inputs, capsys)

    assert "Error: Appointment ID cannot be blank" in output
    assert "Error: Appointment ID already exists" in output
    assert f"Appointment found: {A1_SCHEDULED}" in output

def test_same_practitioner_double_booking_is_rejected(capsys):
    inputs = BOOK_A1 + [
        "1", "P2", "Sam",
        "5", "A2", "P2", "DR1", "2026-11-20 09:00",
        "7", "A2",
        "7", "A1",
        "0",
    ]

    output = run_session(inputs, capsys)

    assert (
        "Error: Practitioner already has a SCHEDULED appointment "
        "at this time" in output
    )
    assert "Error: Appointment not found" in output
    assert f"Appointment found: {A1_SCHEDULED}" in output

def test_different_practitioner_can_book_the_same_time(capsys):
    inputs = BOOK_A1 + [
        "1", "P2", "Sam",
        "3", "DR2", "Lee", "General Practice",
        "5", "A2", "P2", "DR2", "2026-11-20 09:00",
        "0",
    ]

    output = run_session(inputs, capsys)

    expected = "A2: P2 with DR2, 2026-11-20 09:00, scheduled"
    assert f"Appointment booked: {expected}" in output


def test_repeated_cancellation_is_rejected_and_history_is_kept(capsys):
    inputs = BOOK_A1 + ["6", "A1", "6", "A1", "7", "A1", "0"]

    output = run_session(inputs, capsys)

    assert f"Appointment cancelled: {A1_CANCELLED}" in output
    assert "Error: Only SCHEDULED appointments may be cancelled" in output
    assert f"Appointment found: {A1_CANCELLED}" in output


def test_unknown_appointment_lookup_and_cancel_show_errors(capsys):
    inputs = BOOK_A1 + ["7", "A9", "6", "A9", "7", "A1", "0"]

    output = run_session(inputs, capsys)

    assert output.count("Error: Appointment not found") == 2
    assert f"Appointment found: {A1_SCHEDULED}" in output

def test_freed_slot_can_be_booked_again_after_cancellation(capsys):
    inputs = BOOK_A1 + [
        "1", "P2", "Sam",
        "6", "A1",
        "5", "A2", "P2", "DR1", "2026-11-20 09:00",
        "8", "DR1", "",
        "0",
    ]

    output = run_session(inputs, capsys)

    booked = "A2: P2 with DR1, 2026-11-20 09:00, scheduled"
    assert f"Appointment booked: {booked}" in output
    assert A1_CANCELLED in output
    assert output.count(booked) == 2

def test_invalid_status_filter_is_rejected_and_listing_still_works(capsys):
    inputs = BOOK_A1 + ["8", "DR1", "archived", "8", "DR1", "", "0"]

    output = run_session(inputs, capsys)

    assert "Error: 'archived' is not a valid AppointmentStatus" in output
    assert A1_SCHEDULED in output

def test_unknown_and_blank_practitioner_listing_show_errors(capsys):
    inputs = BOOK_A1 + ["8", "DR9", "", "8", "", "", "8", "DR1", "", "0"]

    output = run_session(inputs, capsys)

    assert "Error: Practitioner not found" in output
    assert "Error: Practitioner ID cannot be blank" in output
    assert A1_SCHEDULED in output

