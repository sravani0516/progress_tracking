# test_employee.py

import pytest
from employee import Employee


# -----------------------------
# FIXTURE
# -----------------------------
@pytest.fixture
def emp():
    return Employee(1, "Sravani", 40000)


# -----------------------------
# BUSINESS LOGIC TESTING
# -----------------------------
def test_increase_salary(emp):
    assert emp.increase_salary(5000) == 45000


def test_decrease_salary(emp):
    assert emp.decrease_salary(5000) == 35000


def test_get_annual_salary(emp):
    assert emp.get_annual_salary() == 40000 * 12


def test_is_high_earner_false(emp):
    assert emp.is_high_earner() is False


# -----------------------------
# PARAMETRIZE
# -----------------------------
@pytest.mark.parametrize("salary, expected", [
    (30000, False),
    (50000, True),
    (80000, True),
])
def test_is_high_earner_param(salary, expected):
    emp = Employee(2, "Test", salary)
    assert emp.is_high_earner() == expected


# -----------------------------
# EXCEPTION TESTING
# -----------------------------
def test_increase_salary_invalid(emp):
    with pytest.raises(ValueError):
        emp.increase_salary(-1000)


def test_decrease_salary_invalid(emp):
    with pytest.raises(ValueError):
        emp.decrease_salary(-1000)


def test_decrease_more_than_salary(emp):
    with pytest.raises(ValueError):
        emp.decrease_salary(50000)
