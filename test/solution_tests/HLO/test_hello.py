from lib.solutions.HLO.hello_solution import hello


def test_hello():
    friend_name: str = "John"
    assert hello(friend_name) == "Hello, John!"

