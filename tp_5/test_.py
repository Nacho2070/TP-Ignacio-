import pytest
from funciones_tp5 import *
@pytest.mark.parametrize("dni, expected_result", [
    ("1234567", True), 
    ("12345678", True), 
    ("12345", False),  
    ("123456789", False), 
   
])

def test_check_DNI(dni, expected_result):
    result = check_DNI(dni)
    assert result == expected_result


@pytest.mark.parametrize("max_temp,min_temp,expected_result", [
    (25,10,7.5), 
    (12,0,6),   
   
])

def test_temperature(max_temp,min_temp,expected_result):
    result = medium_Temperature(max_temp,min_temp)
    assert result == expected_result



