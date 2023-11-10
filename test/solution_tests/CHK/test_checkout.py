from lib.solutions.CHK.checkout_solution import checkout


def test_valid_checkout():
    assert checkout("CABABAD") == 210