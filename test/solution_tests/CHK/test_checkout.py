from lib.solutions.CHK.checkout_solution import checkout


def test_valid_checkout():
    assert checkout("CABABAD") == 210


def test_secondary_valid_checkout():
    assert checkout("AAAAAAAAABBBCDEEE") == 570


def test_failed_secondary_valid_checkout_1():
    assert checkout("EE") == 80


def test_failed_secondary_valid_checkout_2():
    assert checkout("EEB") == 110


def test_failed_secondary_valid_checkout_3():
    assert checkout("EEEB") == 110


def test_invalid_checkout():
    assert checkout("TESTINGCHECKOUT") == -1


