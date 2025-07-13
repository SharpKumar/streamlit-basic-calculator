import streamlit as st

st.title("🧮 Sharp Basic Calculator")

num1 = st.number_input("Enter first number:")
num2 = st.number_input("Enter second number:")
operation = st.selectbox("Choose an operation", ["Addition", "Subtraction", "Multiplication", "Division"])

if st.button("Calculate"):
    if operation == "Addition":
        result = num1 + num2
        st.success(f"Result: {result}")
    elif operation == "Subtraction":
        result = num1 - num2
        st.success(f"Result: {result}")
    elif operation == "Multiplication":
        result = num1 * num2
        st.success(f"Result: {result}")
    elif operation == "Division":
        if num2 != 0:
            result = num1 / num2
            st.success(f"Result: {result}")
        else:
            st.error("Division by zero is not allowed.")
