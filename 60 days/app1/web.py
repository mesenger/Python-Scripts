import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    print(todos)
    todos.append(todo)
    functions.write_todos(todos)



st.title('My Todo app')
st.subheader('This is my todo app')
st.write('This is a todo app that I made in 60 days of code')


for todo in todos:
    todo = todo.strip()
    st.checkbox(todo)

st.text_input(label="Add a todo", placeholder='Add a todo here...', on_change=add_todo, key='new_todo')

st.session_state
