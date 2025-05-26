import streamlit as st

def calculate_bmi(weight, height_cm):
    height_m = height_cm / 100
    return round(weight / (height_m ** 2), 2)

    st.title("BMI Calculator")

    weight = st.number_input("Weight (kg)", min_value=1.0)
    height = st.number_input("Height (cm)", min_value=50.0)

    if st.button("Calculate BMI"):
        bmi = calculate_bmi(weight, height)
        st.write(f"Your BMI is {bmi}")
    if bmi < 18.5:
        st.warning("Underweight")
    elif bmi < 25:
        st.success("Normal weight")
    elif bmi < 30:
        st.warning("Overweight")
    else:
        st.error("Obese")