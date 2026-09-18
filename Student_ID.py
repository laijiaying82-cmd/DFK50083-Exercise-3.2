import streamlit as st

st.title("Student ID")

student_id = st.text_input("Enter Student ID")

if st.button("Check"):
    try:
        student_id = int(student_id)

    except ValueError:
        st.error("Invalid Student ID")

    else:
        st.success("Student ID: " + str(student_id))