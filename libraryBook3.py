import streamlit as st

st.title("Library Book Type")

number_of_books = st.number_input(
    "Enter the number of books",
    min_value=1,
    step=1
)

if st.button("Display"):

    for i in range(int(number_of_books)):

        book_type = st.selectbox(
            f"Select type for Book {i + 1}",
            ["Fiction", "Non-Fiction", "Reference"],
            index=None,
            placeholder="Please select a book type"
        )

        if book_type is not None:
            st.write(f"Book {i + 1} Type: {book_type}")
        else:
            st.warning(f"Please select a book type for Book {i + 1}")