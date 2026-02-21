import pytest
import os
from app import *

# 1. Test add
def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

# 2. Test subtract
def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(3, 5) == -2

# 3. String uppercase
def test_upper():
    assert to_upper("hello") == "HELLO"
    assert to_upper("Test") == "TEST"

# 4. List length
def test_list_length():
    assert list_length([1,2,3]) == 3
    assert list_length([]) == 0

# 5. Even check
def test_is_even():
    assert is_even(4) == True
    assert is_even(5) == False

# 6. Division
def test_divide():
    assert divide(10, 2) == 5

# 11. Exception test
def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)

# 7. Multiple functions
def test_multiply():
    assert multiply(2, 3) == 6

# 15. API test
def test_status():
    assert get_status() == 200

# 16. File exists
def test_file_exists():
    assert os.path.exists("app.py")

# 17. List contains
def test_list_contains():
    data = [1,2,3]
    assert 2 in data

# 18. Dictionary test
def test_dictionary():
    user = get_user()
    assert user["name"] == "Ravi"
    assert user["age"] == 25