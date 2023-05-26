import requests
import json


def get_student_info(student_id):
    result = requests.get(
        f"http://localhost:5001/students/{student_id}",
        headers={'content-type': 'application/json'}
    )
    return result.json()


def add_student_info(student_first_name, student_last_name, course_id):
    student = {
        "firstName": student_first_name,
        "lastName": student_last_name,
        "courseId": course_id
    }
    result = requests.post(
        'http://localhost:5001/students',
        headers={'content-type': 'application/json'},
        data=json.dumps(student)
    )
    return result


def run():
    print('############################')
    print('Hello, welcome to our school')
    print("Press 1 to view a student, Press 2 to add a student")
    print('############################')
    choice = int(input("Which do you want to do? : "))
    if choice == 1:
        student_id = input("Which student would you like to see ? :")
        print(get_student_info(student_id))
    else:
        student_first_name = input("First Name ? :")
        student_last_name = input("Last Name ? :")
        course_id = input("Course ID ? :")
        add_student_info(student_first_name, student_last_name, course_id)



if __name__ == '__main__':
    run()



