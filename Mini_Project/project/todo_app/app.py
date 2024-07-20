# app.py

from flask import Flask, render_template, request
from urllib.parse import quote
app = Flask(__name__)

# Sample Student class
class Student:
    def __init__(self, student_id):
        self.student_id = student_id
        self.courses = []

    def enroll(self, course):
        if course not in self.courses:
            self.courses.append(course)
            return f"Enrolled in course: {course}"
        else:
            return f"Already enrolled in course: {course}"

    def drop(self, course):
        if course in self.courses:
            self.courses.remove(course)
            return f"Dropped course: {course}"
        else:
            return f"Not enrolled in course: {course}"

@app.route('/', methods=['GET', 'POST'])
def index():
    student = None
    message = None

    if request.method == 'POST':
        student_id = request.form['student_id']
        course_name = request.form['course']
        action = request.form['action']

        # Assuming student ID validation logic
        # For simplicity, just create a new student instance based on the input ID
        student = Student(student_id)

        if action == 'enroll':
            message = student.enroll(course_name)
        elif action == 'drop':
            message = student.drop(course_name)
        else:
            message = "Invalid action"

    return render_template('index.html', student=student, message=message)

if __name__ == '__main__':
    app.run(debug=True)
