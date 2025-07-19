import pytest

# function to test square
def square(n):
    return n ** 2

# function to test cube
def cube(n):
    return n ** 3

# function to test fifth power
def fifth_power(n):
    return n ** 5

# pytest test cases for square
def test_square():
    assert square(2) == 4
    assert square(3) == 9
    assert square(4) == 16
    assert square(-2) == 4
    assert square(0) == 0

# pytest test cases for cube
def test_cube():
    assert cube(2) == 8
    assert cube(3) == 27
    assert cube(4) == 64
    assert cube(-2) == -8
    assert cube(0) == 0

# pytest test cases for fifth power
def test_fifth_power():
    assert fifth_power(2) == 32
    assert fifth_power(3) == 243
    assert fifth_power(4) == 1024
    assert fifth_power(-2) == -32
    assert fifth_power(0) == 0

# pytest test cases for invalid input
def test_square_invalid_input():
    with pytest.raises(TypeError):
        square("string")
    with pytest.raises(TypeError):
        square(None)

def test_cube_invalid_input():
    with pytest.raises(TypeError):
        cube("string")
    with pytest.raises(TypeError):
        cube(None)

def test_fifth_power_invalid_input():
    with pytest.raises(TypeError):
        fifth_power("string")
    with pytest.raises(TypeError):
        fifth_power(None)
