import streamlit as st
import functions

todos = functions.get_todos()

st.title('My Todo app')
st.subheader('This is my todo app')
st.write('This is a todo app that I made in 60 days of code')


for todo in todos:
    todo = todo.strip()
    st.checkbox(todo)

st.text_input('Add a todo', placeholder='Add a todo here...')