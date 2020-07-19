"""
Program: basic_gui.py
Author: Daniel Meeker
Date: 6/30/2020
This program creates a basic GUI that allows the user
to select between 4 different meals.
"""
import tkinter
import sqlite3
from sqlite3 import Error


def create_connection(db):
    """ Connect to a SQLite database
    :param db: filename of database
    :return connection if no error, otherwise None"""
    try:
        conn = sqlite3.connect(db)
        return conn
    except Error as err:
        print(err)
    return None


def create_table(conn, sql_create_table):
    """ Creates table with give sql statement
    :param conn: Connection object
    :param sql_create_table: a SQL CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(sql_create_table)
    except Error as e:
        print(e)


def create_tables(database):
    sql_create_person_table = """ CREATE TABLE IF NOT EXISTS person (
                                        id integer PRIMARY KEY,
                                        firstname text NOT NULL,
                                        lastname text NOT NULL
                                    ); """

    sql_create_student_table = """CREATE TABLE IF NOT EXISTS student (
                                    id integer PRIMARY KEY,
                                    major text NOT NULL,
                                    begin_date text NOT NULL,
                                    end_date text,
                                    FOREIGN KEY (id) REFERENCES person (id)
                                );"""
    # create a database connection
    conn = create_connection(database)
    if conn is not None:
        # create projects table
        create_table(conn, sql_create_person_table)
        # create tasks table
        create_table(conn, sql_create_student_table)
    else:
        print("Unable to connect to " + str(database))


def create_database_and_tables():
    create_tables("gui_database.db")
    tkinter.Button(m, text="Add Person", width=25, state=tkinter.NORMAL, command=add_person).grid(row=1, column=0)
    tkinter.Button(m, text="Add Student", width=25, state=tkinter.NORMAL, command=add_student).grid(row=2, column=0)


def add_person():
    first_name = tkinter.StringVar()
    last_name = tkinter.StringVar()
    L1 = tkinter.Label(m, text="First Name:").grid(row=1)
    E1 = tkinter.Entry(m, textvariable=first_name).grid(row=1, column=2)
    L2 = tkinter.Label(m, text="Last Name:").grid(row=2)
    E2 = tkinter.Entry(m, textvariable=last_name).grid(row=2, column=2)
    person = (first_name.get(), last_name.get())  # creates a person tuple
    conn = create_connection("gui_database.db")
    tkinter.Button(m, text="Submit", width=25,
                   command=lambda: create_person(conn, person)).grid(row=5, column=2)  # calls create person function


def add_student():
    pass


def create_person(conn, person):
    """Create a new person for table
    :param conn:
    :param person:
    :return: person id
    """
    sql = ''' INSERT INTO person(firstname,lastname)
              VALUES(?,?) '''
    cur = conn.cursor()  # cursor object
    cur.execute(sql, person)
    # return cur.lastrowid  # returns the row id of the cursor object, the person id


def create_student(conn, student):
    """Create a new person for table
    :param conn:
    :param student:
    :return: student id
    """
    sql = ''' INSERT INTO student(id, major, begin_date)
              VALUES(?,?,?) '''
    cur = conn.cursor()  # cursor object
    cur.execute(sql, student)
    return cur.lastrowid  # returns the row id of the cursor object, the student id


def select_all_persons(conn):
    """Query all rows of person table
    :param conn: the connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM person")

    rows = cur.fetchall()

    return rows  # return the rows


def view_all_persons():
    conn = create_connection("gui_database.db")
    with conn:
        rows = select_all_persons(conn)
        for row in rows:
            print(row)


m = tkinter.Tk()
'''
widgets
'''
m.title('GUI Database')
tkinter.Button(m, text="Create Database & Table", width=25, state=tkinter.NORMAL,
               command=create_database_and_tables).grid(row=1, column=0)
view_person = tkinter.Button(m, text='View Person Table', width=25, command=view_all_persons)
view_person.grid(row=6, columnspan=2)
view_student = tkinter.Button(m, text='View Student Table', width=25, command=m.destroy)
view_student.grid(row=7, columnspan=2)
exit_button = tkinter.Button(m, text='Exit', width=25, command=m.destroy)
exit_button.grid(row=8, columnspan=2)
'''
end of widgets
'''

m.mainloop()
