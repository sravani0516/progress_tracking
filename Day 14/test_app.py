import pytest
from app import division
#from app import calc
# def test_add():
#     result = add(2,3)
#     assert result == 5

# def test_sub():
#     result = sub(2,3)
#     assert result == -1

# def test_mul():
#     result = multipuly(2,3)
#     assert result == 6

# def test_dev():
#     result = division(10,5)
#     assert result == 2
# @pytest.fixture
# def calc():
#     return calccc()

# def test_calc_add(calc):
#     assert calc.add(1,2)==3

    
# @pytest.mark.parametrize("a,b,expected",[
#     (1,2,3),
#     (9,7,10),
#     (3,4,7)
# ])
# def test_calc_add_param(calc,a,b,expected):
#     assert calc.add(a,b)== expected

def test_devide_by_zero():
    with pytest.raises(ValueError):
        division(10,0)