import streamlit as st

def calculate_bmi(weight, height_cm):
    height_m = height_cm / 100  # convert height to meters
    bmi = weight / (height_m ** 2)
    return round(bmi, 2)

# Streamlit UI components
st.title("BMI Calculator")

# User inputs
weight = st.number_input("Enter your weight (kg)", min_value=1.0, step=0.5)
height = st.number_input("Enter your height (cm)", min_value=50.0, step=1.0)

if st.button("Calculate BMI"):
    bmi = calculate_bmi(weight, height)

    st.write(f"Your BMI is: **{bmi}**")

    # Simple interpretation
    if bmi < 18.5:
        st.warning("You are underweight.")
    elif 18.5 <= bmi < 24.9:
        st.success("You have a normal weight.")
    elif 25 <= bmi < 29.9:
        st.warning("You are overweight.")
    else:
        st.error("You are obese.")
