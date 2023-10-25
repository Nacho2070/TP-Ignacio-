import pytest
from main import suma

@pytest.mark.parametrize("input_1,input_2,value",
    [
    (2,2,4),
    (5,2,7),
    (5,5,15)
    ]
)
def test_suma(input_1,input_2,value):
   result= suma(input_1,input_2)
   assert result == value