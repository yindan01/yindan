import pytest
@pytest.mark.last
def test_foo():
    assert True

@pytest.mark.third
def test_bar():
    assert True
@pytest.mark.fourth
def test_aar():
    assert True