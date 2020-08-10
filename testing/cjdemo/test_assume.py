import sys

import pytest

sys.path.append('..')
print(sys.path)
def test_a():
    #assert 1==2
    #assert False==True
    #assert 100==200
    pytest.assume(1==1)
    pytest.assume(False == True)
    pytest.assume(300 == 200)

