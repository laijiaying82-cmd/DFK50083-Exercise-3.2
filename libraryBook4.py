import streamlit as st

st.title("Library Book Type")

number_of_books = st.number_input(
    "Enter the number of books",
    min_value=1,
    step=1
)

if "show_books" not in st.session_state:
    st.session_state.show_books = False

if st.button("Display"):
    st.session_state.show_books = True

if st.session_state.show_books:

    for i in range(int(number_of_books)):

        book_type = st.selectbox(
            f"Select type for Book {i + 1}",
            ["Fiction", "Non-Fiction", "Reference"],
            index=None,
            placeholder="Please select a book type",
            key=f"book_{i}"
        )

        if book_type is not None:
            st.write(f"Book {i + 1} Type: {book_type}")
        else:
            st.warning(f"Please select a book type for Book {i + 1}")