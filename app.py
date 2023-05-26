from flask import Flask, jsonify, request
from db_utils import db_get_student_info, db_add_student

app = Flask(__name__)


@app.route('/students/<student_id>')
def get_student_info(student_id):
    res = db_get_student_info(student_id)
    return jsonify(res)


@app.route('/students', methods=['POST'])
def add_student():
    student_info = request.get_json()
    try:
        db_add_student(firstName=student_info['firstName'],
                   lastName=student_info['lastName'], courseId=student_info['courseId'])
    except:
        return "Failed to add student"
    else:
        return "Successfully added a student"
if __name__ == '__main__':
    app.run(debug=True, port=5001)