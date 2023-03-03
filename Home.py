import streamlit as st

name = st.text_input("Please, enter your name.", value="John")

if name:
  string = f"Hello, {name}!"
  st.write(string)
else:
  st.write("Hello, stranger!")
