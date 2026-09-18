import streamlit as st

st.title("Average Score")

total_score = st.text_input("Enter total score")

number_of_subjects = st.text_input("Enter number of subjects")

if st.button("Calculate"):
    try:
        total_score = float(total_score)
        number_of_subjects = int(number_of_subjects)

        average = total_score / number_of_subjects

        st.success("Average Score: " + str(average))

    except ZeroDivisionError:
        st.error("Number of Subjects Cannot Be Zero")

    except ValueError:
        st.error("Invalid Input")