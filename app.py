import streamlit as st

# Title
st.title("🎉 Personal Greeting App")

# Input fields
name = st.text_input("What is your name?")
age = st.number_input("How old are you?", min_value=1, max_value=120, step=1)
color = st.color_picker("Pick your favorite color")

# Display message
if name and age:
    st.markdown(f"""
    ### 👋 Hello, {name}!
    You are **{int(age)} years old** and your favorite color is  
    <span style='color:{color}; font-weight:bold;'>{color}</span> 🎨
    """, unsafe_allow_html=True)
