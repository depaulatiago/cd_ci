from app import soma


def test_soma():
    assert soma(2, 2) == 4
    assert soma(-1, 1) == 0
