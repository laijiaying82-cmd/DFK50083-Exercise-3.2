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
            ["Fiction", "Non-Fiction", "Reference"]
        )

        if book_type:
            st.write(
                "Book", i + 1,
                "Type:", book_type
            )
        else:
            st.write(
                "Book", i + 1,
                "No type selected"
            )