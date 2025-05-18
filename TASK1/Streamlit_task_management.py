import streamlit as st

for key in ["urgent_tasks", "high_tasks", "general_tasks", "completed_tasks", "recent_tasks_stack"]:
    if key not in st.session_state:
        st.session_state[key] = []

class Task:
    def __init__(self, name, priority="Medium"):
        self.name = name
        self.priority = priority
        self.status = "Pending"

    def __repr__(self):
        return f"{self.name} ({self.priority}, {self.status})"

st.title("Task Management System")
st.header("Add New Task")
with st.form("add_task_form"):
    task_name = st.text_input("Task Name")
    priority = st.selectbox("Select Priority", ["Urgent", "High", "Medium", "Low"])
    submitted = st.form_submit_button("Add Task")
    if submitted and task_name:
        task = Task(task_name, priority)
        if priority == "Urgent":
            st.session_state.urgent_tasks.append(task)
        elif priority == "High":
            st.session_state.high_tasks.append(task)
        else:
            st.session_state.general_tasks.append(task)
        st.session_state.recent_tasks_stack.append(task)
        st.success(f"Task '{task_name}' added with priority '{priority}'")

def render_task_section(title, key_name):
    st.subheader(title)
    tasks = st.session_state[key_name]
    updated_tasks = []
    if tasks:
        for i, task in enumerate(tasks):
            col1, col2, col3 = st.columns([5, 2, 2])
            with col1:
                st.write(f"_{task.name} ({task.priority}, {task.status})_")
            with col2:
                if st.button("Completed", key=f"{key_name}_complete_{i}"):
                    task.status = "Completed"
                    st.session_state.completed_tasks.append(task)
                    break
            with col3:
                if st.button("Remove", key=f"{key_name}_remove_{i}"):
                    break
            updated_tasks.append(task)
        st.session_state[key_name] = updated_tasks
    else:
        st.info(f"No {title.lower()}")

render_task_section("Urgent Tasks (Array)", "urgent_tasks")
render_task_section("High Priority Tasks (Array)", "high_tasks")
render_task_section("General Tasks (Linked List)", "general_tasks")

st.subheader("Recently Viewed Tasks (Stack)")
recent_stack = st.session_state.recent_tasks_stack

if len(recent_stack) >= 2:
    preview_task = recent_stack[-2]
    with st.expander("Recently Viewed Task"):
        st.markdown(f"**Task:** {preview_task.name}")
        st.markdown(f"**Priority:** {preview_task.priority}")
        st.markdown(f"**Status:** {preview_task.status}")

if recent_stack:
    if st.button("View Details", key="view_recent"):
        st.markdown("#### Last 5 Recently Viewed Tasks")
        for task in reversed(recent_stack[-5:]):
            st.write(f"{task.name} ({task.priority}, {task.status})")
else:
    st.info("No recent tasks viewed.")

# -----------------------------------------
# st.header("Task Review Section (Completed Tasks)")
# if st.session_state.completed_tasks:
#     priority_order = {"Urgent": 0, "High": 1, "Medium": 2, "Low": 3}
#     sorted_completed = sorted(
#         st.session_state.completed_tasks,
#         key=lambda t: priority_order.get(t.priority, 4)
#     )
#     for task in sorted_completed:
#         st.write(f"{task.name} ({task.priority}, {task.status})")
# else:
#     st.info("No tasks completed yet.")
# -----------------------------------------

st.header("Task Manager Application")
st.subheader("Task Overview")

default_task_name = recent_stack[-1].name if recent_stack else "Select View"

view_option = st.selectbox(
    "Select Task View",
    options=[
        "All Tasks", "Recent Tasks", "Pending Tasks", "Completed Tasks"
    ],
    index=0
)
filtered_tasks = []
if view_option == "All Tasks":
    for key in ["urgent_tasks", "high_tasks", "general_tasks", "completed_tasks",]:
        filtered_tasks.extend(st.session_state[key])

elif view_option == "Recent Tasks":
    filtered_tasks = recent_stack[-5:]

elif view_option == "Pending Tasks":
    for key in ["urgent_tasks", "high_tasks", "general_tasks"]:
        filtered_tasks.extend([t for t in st.session_state[key] if t.status == "Pending"])

elif view_option == "Completed Tasks":
    filtered_tasks = st.session_state.completed_tasks

if filtered_tasks:
    for task in filtered_tasks:
        st.markdown(f"**{task.name}** — *{task.priority}, {task.status}*")
else:
    st.info("No tasks to display for the selected view.")


st.text_input("Enter description of task to delete", key="delete_desc_input")
if st.button("Delete Task"):
    desc = st.session_state.delete_desc_input.strip()
    found = False
    for key in ["urgent_tasks", "high_tasks", "general_tasks", "completed_tasks", "recent_tasks_stack"]:
        new_list = [t for t in st.session_state[key] if t.name != desc]
        if len(new_list) != len(st.session_state[key]):
            st.session_state[key] = new_list
            found = True
    if found:
        st.success(f"Task '{desc}' deleted from all sections.")
    else:
        st.warning(f"No task found with description '{desc}'.")
