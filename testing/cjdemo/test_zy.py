import pytest
@pytest.mark.first
def test_add():
    assert True

@pytest.mark.third
def test_sub():
    assert True
@pytest.mark.last
def test_multiply():
    assert True

@pytest.mark.second
def test_divide():
    assert True