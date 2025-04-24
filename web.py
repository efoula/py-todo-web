import streamlit as st
import functions as f

st.title("Welcome to the Streamlit App")
st.subheader("ToDo Application")
st.write("This is a simple ToDo application built with Streamlit.")
todo_list = f.get_todos()

for i, todo in enumerate(todo_list):
    todo_checkbox = st.checkbox(todo, key=f"{todo}_{i}")
    if todo_checkbox:
        f.complete_todo(todo)
        st.success(f"Completed: {todo}")
        st.rerun()  # Refresh the app to update the list

# Step 1: Ensure the session_state key exists
if "new_todo" not in st.session_state:
    st.session_state["new_todo"] = ""

# Step 2: Define a handler that uses the value at the right time
def handle_new_todo():
    f.add_todo(st.session_state["new_todo"])
    st.session_state["new_todo"] = ""  # Clear the input after adding

st.text_input(
    "",
    key="new_todo",
    placeholder="Add a new todo",
    on_change=handle_new_todo
)

# st.session_state