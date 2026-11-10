import psycopg2


def get_connection():
    return psycopg2.connect(
        host="localhost", port=5432,
        dbname="tp", user="postgres", password="postgres",
    )


def add_student(conn, name, grade):
    with conn.cursor() as cur:
        cur.execute(
            "INSERT INTO students (name, grade) VALUES (%s, %s) RETURNING id",
            (name, grade),
        )
        new_id = cur.fetchone()[0]
    conn.commit()
    return new_id


def get_student(conn, student_id):
    with conn.cursor() as cur:
        cur.execute(
            "SELECT id, name, grade FROM students WHERE id = %s",
            (student_id,),
        )
        return cur.fetchone()  # None si l'étudiant n'existe pas


def average_grade(conn):
    # À écrire à l'exercice 2
    raise NotImplementedError
