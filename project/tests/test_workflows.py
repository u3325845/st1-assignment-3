
"""Stage 9 interactive console workflow tests."""

from unittest.mock import patch

from smartcare.console import run_menu


def test_patient_registration_and_lookup(capsys):
    """A registered patient remains available during the same session."""
    inputs = [
        "1", "P1", "Alex",
        "2", "P1",
        "0",
    ]

    with patch("builtins.input", side_effect=inputs):
        run_menu()

    output = capsys.readouterr().out

    assert "Patient registered: P1 - Alex" in output
    assert "Patient found: P1 - Alex" in output
    assert "Goodbye!" in output


def test_practitioner_registration_and_lookup(capsys):
    """A registered practitioner remains available in the same session."""
    inputs = [
        "3", "DR1", "Taylor", "General Practice",
        "4", "DR1",
        "0",
    ]

    with patch("builtins.input", side_effect=inputs):
        run_menu()

    output = capsys.readouterr().out

    assert "Practitioner registered: DR1 - Taylor (General Practice)" in output
    assert "Practitioner found: DR1 - Taylor (General Practice)" in output
    assert "Goodbye!" in output



def test_appointment_booking_and_lookup(capsys):
    """Booking an appointment makes it available for lookup."""
    inputs = [
        "1", "P1", "Alex",
        "3", "DR1", "Taylor", "General Practice",
        "5", "A1", "P1", "DR1", "2026-11-20 09:00",
        "7", "A1",
        "0",
    ]

    with patch("builtins.input", side_effect=inputs):
        run_menu()

    output = capsys.readouterr().out

    expected = "A1: P1 with DR1, 2026-11-20 09:00, scheduled"

    assert f"Appointment booked: {expected}" in output
    assert f"Appointment found: {expected}" in output
    assert "Goodbye!" in output



def test_appointment_cancellation_and_history(capsys):
    """Cancelled appointments remain available for lookup."""
    inputs = [
        "1", "P1", "Alex",
        "3", "DR1", "Taylor", "General Practice",
        "5", "A1", "P1", "DR1", "2026-11-20 09:00",
        "6", "A1",
        "7", "A1",
        "0",
    ]

    with patch("builtins.input", side_effect=inputs):
        run_menu()

    output = capsys.readouterr().out

    expected = "A1: P1 with DR1, 2026-11-20 09:00, cancelled"

    assert f"Appointment cancelled: {expected}" in output
    assert f"Appointment found: {expected}" in output
    assert "Goodbye!" in output



def test_invalid_menu_choice_recovers(capsys):
    """An invalid menu choice does not terminate the session."""
    inputs = [
        "99",
        "1", "P1", "Alex",
        "2", "P1",
        "0",
    ]

    with patch("builtins.input", side_effect=inputs):
        run_menu()

    output = capsys.readouterr().out

    assert "Invalid menu option. Please choose 0-8." in output
    assert "Patient registered: P1 - Alex" in output
    assert "Patient found: P1 - Alex" in output
    assert "Goodbye!" in output
