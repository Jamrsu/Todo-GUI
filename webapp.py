import streamlit as st
import functions

todos = functions.get_todos()

st.title("My Todo App")
st.subheader("this is my todo app")
st.write("This ap is to increase productivity")


for todo in todos:
    st.checkbox(todo)


st.text_input(label="", placeholder="Add new todo...")
