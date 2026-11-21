import streamlit as st

st.set_page_config(page_title="Student Attendance")

st.title("🎓 Student Attendance System")

if "students" not in st.session_state:
    st.session_state.students = {}

students = st.session_state.students

menu = st.sidebar.selectbox(
    "Select Menu",
    ["Add Student", "Mark Attendance", "View Reports"]
)

if menu == "Add Student":
    roll = st.text_input("Roll Number")
    name = st.text_input("Student Name")

    if st.button("Add Student"):
        if roll and name and roll not in students:
            students[roll] = {
                "name": name,
                "present": 0,
                "total": 0
            }
            st.success("Student added successfully!")
        else:
            st.error("Enter valid details or use a new roll number.")

elif menu == "Mark Attendance":
    if students:
        roll = st.selectbox("Select Student", list(students.keys()))
        status = st.radio("Attendance", ["Present", "Absent"])

        if st.button("Save Attendance"):
            students[roll]["total"] += 1
            if status == "Present":
                students[roll]["present"] += 1
            st.success("Attendance saved!")
    else:
        st.info("First add a student.")

elif menu == "View Reports":
    for roll, data in students.items():
        total = data["total"]
        present = data["present"]
        percent = present / total * 100 if total else 0

        st.write(
            f"Roll: {roll} | Name: {data['name']} | "
            f"Present: {present} | Total: {total} | "
            f"Attendance: {percent:.2f}%"
        )
