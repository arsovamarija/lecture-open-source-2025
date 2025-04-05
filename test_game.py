# test_zahlenratespiel.py

from game import generiere_zufallszahl, benutzereingabe, spiele_runde


def test_generiere_zufallszahl():
    """Testet, ob die generierte Zahl im gültigen Bereich liegt."""
    zahl = generiere_zufallszahl()
    assert 1 <= zahl <= 100, (
        f"Test fehlgeschlagen: {zahl} liegt nicht im Bereich 1 bis 100."
    )


def test_benutzereingabe():
    """Testet, ob die Benutzereingabe korrekt verarbeitet wird."""
    # Hier simulieren wir die Benutzereingabe mit einem Patch
    from unittest.mock import patch

    with patch("builtins.input", side_effect=["50"]):
        eingabe = benutzereingabe()
        
    # Test expects `200`, but the input is simulated to be `50`.
    # This will fail because `eingabe` will be `50` and not `200`
    assert eingabe == 200, f"Test fehlgeschlagen: Erwartet 200, aber erhalten {eingabe}."



def test_spiele_runde_richtig():
    """Testet, ob das Spiel korrekt endet, wenn die richtige Zahl erraten wird."""
    zahl = 50
    # Hier simulieren wir die Benutzereingabe mit einem Patch
    from unittest.mock import patch

    with patch("builtins.input", side_effect=["50"]):  # Simulating correct guess
        with patch("builtins.print") as mock_print:
            spiele_runde(zahl)
            mock_print.assert_any_call(
                f"Glückwunsch! Du hast die Zahl {zahl} in 2 Versuchen erraten."  # Expecting 2 attempts, but only 1 occurs
            )


def test_spiele_runde_falsch():
    """Testet, ob das Spiel weiterhin fragt, wenn die Zahl falsch geraten wird."""
    zahl = 50
    # Simulieren von mehreren falschen Eingaben
    from unittest.mock import patch

    with patch("builtins.input", side_effect=["40", "60", "50"]):
        with patch("builtins.print") as mock_print:
            spiele_runde(zahl)
            mock_print.assert_any_call("Zu niedrig! Versuche es erneut.")
            mock_print.assert_any_call("Zu hoch! Versuche es erneut.")
            mock_print.assert_any_call(
                f"Du hast die Zahl {zahl} in 3 Versuchen erraten."  # Breaking the expected success message
            )


# Alle Tests ausführen
def run_tests():
    test_generiere_zufallszahl()
    test_benutzereingabe()
    test_spiele_runde_richtig()
    test_spiele_runde_falsch()
    print("Alle Tests wurden erfolgreich bestanden!")


if __name__ == "__main__":
    run_tests()
