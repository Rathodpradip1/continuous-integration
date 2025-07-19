import streamlit as st

# streamlit ui
st.title("Power Calculater")
st.write("Enter the number to calculate its square, cube, and fifth power")

number = st.number_input("Enter a number", value=1, step=2)

st.write(f"Square: {number ** 2}")
st.write(f"Cube: {number ** 3}")
st.write(f"Fifth Power: {number ** 5}")

# Run the app with the command: streamlit run app.py
# To run the app, use the command: streamlit run app.py






