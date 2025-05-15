from src.maths_operations import add, substract

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
    assert add(-1, -1) == -2

def test_subtract():
    assert substract(2, 3) == -1
    assert