import pytest
from bank import Bank

@pytest.fixture
def bank():
    return Bank(1000)

def test_deposit(bank):
    assert bank.deposit(500)==1500

def test_withdrawl(bank):
    assert bank.deposit(200)==800


def test_withdraw_error(bank):
    with pytest.raises(ValueError):
        bank.withdraw(2000)
    