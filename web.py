import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    if todo not in todos:
        todos.append(todo)
        functions.write_todos(todos)
    else:
        print("todo is already in")

st.title("My Todo App")
st.subheader("This is my Todo App")
st.write("This app is to increase your productivity!")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo.strip(), key=todo) # cause each to-do need different key
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input("Enter a todo", placeholder="Add new todo",
              on_change=add_todo ,key= 'new_todo')