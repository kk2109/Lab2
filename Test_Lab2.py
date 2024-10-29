import pytest
from lab2 import find_min_max, calc_average, calc_median_temperature
test_data = [30.5, 25.2, 40.3, 28.1, 35.6]

def test_find_min_max ():
    result = find_min_max(test_data)
    assert result == [25.2,40.3]
    

def test_calc_average():
    result=calc_average(test_data)
    assert result == pytest.approx(31.94)

def test_calc_median_temperature():
    result = calc_median_temperature(test_data) 
    assert result == pytest.approx(30.5)