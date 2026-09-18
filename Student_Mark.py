import streamlit as st

st.title("Student Mark")

mark = st.text_input("Enter student mark")

if st.button("Check"):
    try:
        mark = int(mark)
        st.success("Student Mark: " + str(mark))

    except ValueError:
        st.error("Invalid Mark")