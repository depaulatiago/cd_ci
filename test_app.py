from app import soma


def test_soma():
    assert soma(2, 2) == 2
    assert soma(-1, 1) == 0
