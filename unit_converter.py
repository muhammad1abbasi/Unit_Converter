import streamlit as st

def length_converter(value, from_unit, to_unit):
    conversion_factors = {
        "Meters": 1,
        "Kilometers": 0.001,
        "Miles": 0.000621371,
        "Feet": 3.28084
    }
    return value * (conversion_factors[to_unit] / conversion_factors[from_unit])

def weight_converter(value, from_unit, to_unit):
    conversion_factors = {
        "Grams": 1,
        "Kilograms": 0.001,
        "Pounds": 0.00220462
    }
    return value * (conversion_factors[to_unit] / conversion_factors[from_unit])

def temperature_converter(value, from_unit, to_unit):
    if from_unit == "Celsius" and to_unit == "Fahrenheit":
        return (value * 9/5) + 32
    elif from_unit == "Fahrenheit" and to_unit == "Celsius":
        return (value - 32) * 5/9
    return value

# Streamlit UI
st.set_page_config(page_title="Unit Converter", page_icon="🔄", layout="centered")
st.title("🔄 Unit Converter")
st.markdown("Convert between different units of Length, Weight, and Temperature.")

# Sidebar for category selection
category = st.sidebar.selectbox("Select Conversion Category", ["Length", "Weight", "Temperature"])
value = st.number_input("Enter value", min_value=0.0, format="%.2f")

if category == "Length":
    from_unit = st.selectbox("From", ["Meters", "Kilometers", "Miles", "Feet"])
    to_unit = st.selectbox("To", ["Meters", "Kilometers", "Miles", "Feet"])
    result = length_converter(value, from_unit, to_unit)
elif category == "Weight":
    from_unit = st.selectbox("From", ["Grams", "Kilograms", "Pounds"])
    to_unit = st.selectbox("To", ["Grams", "Kilograms", "Pounds"])
    result = weight_converter(value, from_unit, to_unit)
else:
    from_unit = st.selectbox("From", ["Celsius", "Fahrenheit"])
    to_unit = st.selectbox("To", ["Celsius", "Fahrenheit"])
    result = temperature_converter(value, from_unit, to_unit)

if st.button("Convert", use_container_width=True):
    st.success(f"Converted Value: {result:.2f} {to_unit}")
