import mysql.connector
from config import USER, PASSWORD, HOST


class DbConnectionError(Exception):
    pass


def _connect_to_db(db_name):
    cnx = mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        auth_plugin='mysql_native_password',
        database=db_name
    )
    return cnx


# EXAMPLE 1
def db_get_student_info(student_id):
    result = None
    db_connection = None
    try:
        db_name = 'COURSE'
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor(dictionary=True)
        print("Connected to DB: %s" % db_name)
        query = """
            SELECT
                s.firstName, s.lastName, c.subject, t.firstName AS teacherFirstName, t.lastName AS teacherLastName
            FROM Student s
            JOIN Course c
            ON c.id = s.courseId
            JOIN Teacher t
            ON t.id = c.teacherId
            WHERE s.id = %s;
            """
        data = (student_id,)
        cur.execute(query, data)
        result = cur.fetchall()  # this is a list with db records where each record is a tuple
        cur.close()
    except Exception:
        raise DbConnectionError("Failed to read data from DB")
    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")
        return result
