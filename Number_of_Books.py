import streamlit as st

st.title("Number of Books")

quantity = st.text_input("Enter number of books")

if st.button("Check"):
    try:
        quantity = int(quantity)
        st.success("Number of Books: " + str(quantity))

    except ValueError:
        st.error("Invalid Quantity")

    finally:
        st.write("Program Completed")