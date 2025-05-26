from app import calculate_bmi
def test_bmi_calculation():
    assert calculate_bmi(70, 170) == 24.2
    print("Test passed: BMI calculation is correct.")

