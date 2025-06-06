import streamlit as st

st.title("From Code to Consciousness")

st.write("""
Welcome to the **From Code to Consciousness** project.

This app will explore the intersection of algorithms, biology, governance, and the Fourth Industrial Revolution.

Feel free to expand this app with more interactive content!
""")

# Example of a simple user input and display
user_input = st.text_input("Share your thoughts about AI and consciousness:")

if user_input:
    st.write("You said:", user_input)
