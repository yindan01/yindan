import pytest


def test_rerun():
    assert 1==2


def test_rerun1():
    assert 2==2
@pytest.mark.flaky(reruns=5,reruns_delay=2)
def test_rerun2():
    assert 3 == 2