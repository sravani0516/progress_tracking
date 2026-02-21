import pytest
from app import add, square

# 8. Fixture
@pytest.fixture
def sample_data():
    return [1,2,3,4]

def test_fixture_length(sample_data):
    assert len(sample_data) == 4

# 9. Multiple inputs
def test_square():
    assert square(2) == 4
    assert square(3) == 9

# 10. Parametrize
@pytest.mark.parametrize("a,b,result", [
    (1,2,3),
    (2,3,5),
    (-1,1,0)
])
def test_add_param(a,b,result):
    assert add(a,b) == result

# 19. Fixture scope
@pytest.fixture(scope="module")
def module_data():
    return {"course": "Python"}

def test_module_fixture(module_data):
    assert module_data["course"] == "Python"