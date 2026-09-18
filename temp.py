import streamlit as st

st.title("Temperature Input")

temperature = st.text_input("Enter a temperature")

if st.button("Display"):
    try:
        temperature = float(temperature)
        st.write("Temperature:", temperature)

    except ValueError:
        st.error("Invalid Temperature")