import streamlit as st

st.title("Ticket Price")

price = st.text_input("Enter ticket price")

if st.button("Check"):
    try:
        price = float(price)

    except ValueError:
        st.error("Invalid Price")

    else:
        st.success("Ticket Price: RM " + format(price, ".2f"))