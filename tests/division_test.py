"""Testing Subtraction"""
from calc.calculations.division import Division

def test_calculation_subtraction():
    """testing that our calculator has a static method for addition"""
    #Arrange
    mynumbers = (1.0,2.0)
    divsiion = Division (mynumbers)
    #Act
    #Assert
    assert division.get_result() == -3