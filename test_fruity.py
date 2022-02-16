from lib.randoFruit import fruity


def test_fruity():
    assert fruity(interval=0).pop() in ["apple", "cherry", "strawberry"]
