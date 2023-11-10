from lib.solutions.CHK.checkout_solution import checkout


def test_valid_checkout():
    assert checkout("CABABAD") == 210


def test_failed_secondary_valid_checkout_0():
    assert checkout("AAAAABBCDE") == 320


def test_failed_secondary_valid_checkout_1():
    assert checkout("EEB") == 80


def test_failed_secondary_valid_checkout_2():
    assert checkout("EEEB") == 120


def test_failed_secondary_valid_checkout_3():
    assert checkout("EEEEBB") == 160


def test_third_valid_checkout_0():
    assert checkout("AAAAABBCDEFF") == 340


def test_third_valid_checkout_1():
    assert checkout("AAAAABBCDEFFF") == 340


def test_third_valid_checkout_2():
    assert checkout("AAAAABBCDEFFFFF") == 350


def test_invalid_checkout():
    assert checkout("TESTINGCHECKOUT") == -1

