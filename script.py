import streamlit as st

st.title("🌏Unit Convertor App")
st.markdown("### Streamline your work with our easy-to-use unit converter.")
st.write("Welcome! This app will help you convert between different units of measurement.")

category  = st.selectbox("Choose a category",["Time", "Weight", "Lenght"])

def convert_units(category, value, units):
    if category == "Lenght":
        if unit == "Kilometers to Miles":
            return value * 0.621371
        elif unit == "Miles to Kilometers":
            return value / 0.621371
    elif category == "Weight":
        if unit == "Kilograms to Pounds":
            return value * 2.20462
        elif unit == "Pounds to Kilograms":
            return value / 2.20462
    elif category == "Time":
        if unit == "Seconds to Minutes":
            return value / 60
        elif unit == "Minutes to Seconds":
            return value * 60 
        elif unit == "Minutes to Hours":
            return value / 60
        elif unit == "Hours to Minutes":
            return value * 60
        elif unit == "Hours to Days":
            return value / 24 
        elif unit == "Days to Hours":
            return value * 24
    return 0
if category == "Lenght":
    unit = st.selectbox("📏 Select conversion", ["Kilometers to Miles","Miles to Kilometers"])
elif category == "Weight":
    unit = st.selectbox("⚖️ Select conversion", ["Kilograms to Pounds","Pounds to Kilograms"])
elif category == "Time":
    unit = st.selectbox("🕐 Select conversion", ["Minutes to Hours","Hours to Minutes","Days to Hours","Hours to Days","Seconds to Minutes","Minutes to Seconds"])
          
value = st.number_input("Enter a value to convert")


if st.button("Convert"):
    result = convert_units(category, value , unit)
    st.success(f"The result is {result:.2f}")
st.write("Feel free to make another conversion.")


