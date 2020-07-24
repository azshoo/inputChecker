import pytest
import sys, os
sys.path.append(os.path.relpath('../inputCheck'))
from checkInputIsDate import check_input_is_date

@pytest.mark.parametrize('test_data', ["13 04 2013", "01 05 2000", "31 12 2012"])
def testValidInputProcessing(test_data):
    test_result = check_input_is_date(test_data)
    assert test_result, f"Failed with data: {test_data}, expected True, got {test_result}"


@pytest.mark.parametrize('test_data', ["00 12 2014", "00 00 0000", "10 13 2008", "13 05 0",  "05 00 03"])
def testInputIsInvalidDate(test_data):
    test_result = check_input_is_date(test_data)
    assert test_result is False, f"Failed with data: {test_data}, expected False, got {test_result}"

@pytest.mark.parametrize('test_data', ["0.5 13 999", "foobar", "05 test 12", "O 12 13"])
def testInputIsNotValidInteger(test_data):
    test_result = check_input_is_date(test_data)
    assert test_result is False, f"Failed with data: {test_data}, expected False, got {test_result}"

@pytest.mark.parametrize('test_data', ["29 02 2004", "29 02 4", "29 02 2000", "29 02 1600"])
def testLeapYearPositive(test_data):
    test_result = check_input_is_date(test_data)
    assert test_result, f"Failed with data: {test_data}, expected True, got {test_result}"

@pytest.mark.parametrize('test_data', ["29 02 2005", "29 02 1900", "29 02 2021", "29 02 2"])
def testLeapYearNegative(test_data):
    test_result = check_input_is_date(test_data)
    assert test_result is False, f"Failed with data: {test_data}, expected False, got {test_result}"

@pytest.mark.parametrize('test_data', ["31 05 2003", "28 02 2005", "30 04 1991", "31 08 1734", "31 07 166"])
def testDaysAtMonthCountPositive(test_data):
    test_result = check_input_is_date(test_data)
    assert test_result, f"Failed with data: {test_data}, expected True, got {test_result}"

@pytest.mark.parametrize('test_data', ["31 02 2001", "30 2 11", "31 04 2018", "31 06 1136", "31 9 2018", "31 11 1854"])
def testDaysAtMonthCountNegative(test_data):
    test_result = check_input_is_date(test_data)
    assert test_result is False, f"Failed with data: {test_data}, expected False, got {test_result}"
