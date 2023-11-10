from lib.solutions.CHK.checkout_solution import checkout


def test_valid_checkout():
    assert checkout("CABABAD") == 210


def test_secondary_valid_checkout():
    assert checkout("AAAAAAAAABBBCDEEE") == 570


def test_invalid_checkout():
    assert checkout("TESTINGCHECKOUT") == -1

