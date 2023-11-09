
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
 

 
from tp_6 import values

@pytest.mark.parametrize("input_1,value",
    [
    ([24565478970], [2456547897]),
    ([85495473450], [8549547345]),
   
    ]
)
def test_tp_6(input_1,value):
   result= values(input_1)
   assert result == value
   
   
from tp_7 import bubble_sort

# Importa la función bubble_sort desde el archivo donde está definida


import pytest

@pytest.mark.parametrize("input_list, sorted_list",
    [
    ([4, 2, 7, 1, 9], [1, 2, 4, 7, 9]),
    ([3, 1, 5, 2, 4], [1, 2, 3, 4, 5]),
    ([10, 9, 8, 7, 6], [6, 7, 8, 9, 10]),
    
    ]
)
def test_bubble_sort(input_list, sorted_list):
    #
    input_copy = input_list.copy()
    bubble_sort(input_copy) 
    assert input_copy == sorted_list

from tp_8 import positive_number

import pytest

@pytest.mark.parametrize("input_number, expected_result",
    [
    (0, 1),     
    (5, 1),       
    (12345, 5),   
    (987654321, 9) 
    ]
)
def test_positive_number(input_number, expected_result):
    result = positive_number(input_number)
    assert result == expected_result  
   