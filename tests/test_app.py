from my_bmi_app.app import calculate_bmi

def test_bmi_calculation():
    assert calculate_bmi(70, 170) == 24.2
