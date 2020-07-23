"""
Program: gui_database.py
Author: Daniel Meeker
Date: 7/23/2020
This program demonstrates using GUI's in Python to
interact with databases.
"""
import tkinter
from tkinter import messagebox
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


conn = create_connection('gui_database.db')


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
                                    firstname text NOT NULL,
                                    lastname text NOT NULL,
                                    major text NOT NULL,
                                    start_date text NOT NULL,
                                    end_date text,
                                    FOREIGN KEY (id) REFERENCES person (id)
                                );"""
    # create a database connection
    global conn
    if conn is not None:
        # create projects table
        create_table(conn, sql_create_person_table)
        # create tasks table
        create_table(conn, sql_create_student_table)
    else:
        print("Unable to connect to " + str(database))


def create_database_and_tables():
    """
    creates the database and displays the Add Person
    and Add Student buttons
    :return: none
    """
    create_tables("gui_database.db")
    tkinter.Button(m, text="Add Person", width=25, state=tkinter.NORMAL, command=add_person).grid(row=1, column=0)
    tkinter.Button(m, text="Add Student", width=25, state=tkinter.NORMAL, command=add_student).grid(row=2, column=0)


def add_person():
    """
    Adds labels and entries and a submit button
    to allow user input for the person table
    :return: none
    """
    first_name = tkinter.StringVar()
    last_name = tkinter.StringVar()
    L1 = tkinter.Label(m, text="First Name:").grid(row=1, column=2)
    E1 = tkinter.Entry(m, textvariable=first_name).grid(row=1, column=3)
    L2 = tkinter.Label(m, text="Last Name:").grid(row=2, column=2)
    E2 = tkinter.Entry(m, textvariable=last_name).grid(row=2, column=3)
    global conn
    with conn:
        tkinter.Button(m, text="Submit", width=25,
                       command=lambda: create_person(conn, (first_name.get(), last_name.get()), first_name,
                                                     last_name)).grid(row=5,
                                                                      column=3)  # calls create person function


def add_student():
    """
    Adds labels and entries and a submit button
    so that the user can add input in the student
    table
    :return: none
    """
    first_name = tkinter.StringVar()
    last_name = tkinter.StringVar()
    major = tkinter.StringVar()
    start_date = tkinter.StringVar()
    L1 = tkinter.Label(m, text="First Name:").grid(row=1, column=2)
    E1 = tkinter.Entry(m, textvariable=first_name).grid(row=1, column=3)
    L2 = tkinter.Label(m, text="Last Name:").grid(row=2, column=2)
    E2 = tkinter.Entry(m, textvariable=last_name).grid(row=2, column=3)
    L3 = tkinter.Label(m, text="Major:").grid(row=3, column=2)
    E3 = tkinter.Entry(m, textvariable=major).grid(row=3, column=3)
    L4 = tkinter.Label(m, text="Start Date:").grid(row=4, column=2)
    E4 = tkinter.Entry(m, textvariable=start_date).grid(row=4, column=3)
    global conn
    with conn:
        tkinter.Button(m, text="Submit", width=25,
                       command=lambda: create_student(conn, (first_name.get(), last_name.get(), major.get(), start_date.get()),
                                                      first_name, last_name, major,
                                                      start_date)).grid(row=5,
                                                                        column=3)  # calls create student function


def create_person(conn, person, first_name, last_name):
    """Create a new person for table
    :param conn: required
    :param person: required (a tuple with first/last name)
    :param first_name: required - allows the field to be set to an empty string
    :param last_name: required - allows the field to be set to an empty string
    :return: none
    """
    sql = ''' INSERT INTO person(firstname,lastname)
              VALUES(?,?) '''
    cur = conn.cursor()  # cursor object
    cur.execute(sql, person)
    # print(str(cur.lastrowid))
    # return cur.lastrowid  # returns the row id of the cursor object, the person id
    first_name.set('')
    last_name.set('')
    messagebox.showinfo('Success', 'Person Successfully Added to Database!')


def create_student(conn, student, first_name, last_name, major, start_date):
    """Create a new person for table
    :param start_date: - allows entry to be reset to empty string
    :param major: - allows entry to be reset to empty string
    :param last_name: - allows entry to be reset to empty string
    :param first_name: - allows entry to be reset to empty string
    :param conn: required
    :param student: - a tuple representing all the fields in the student db
    :return: student id
    """
    sql = ''' INSERT INTO student(firstname, lastname, major, start_date)
              VALUES(?,?,?,?) '''
    cur = conn.cursor()  # cursor object
    cur.execute(sql, student)
    # return cur.lastrowid  # returns the row id of the cursor object, the student id
    first_name.set('')
    last_name.set('')
    major.set('')
    start_date.set('')
    messagebox.showinfo('Success', 'Student Successfully Added to the Database!')


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
    """
    Displays a messagebox with all the rows of the table
    :return: none
    """
    message = ''
    global conn
    with conn:
        rows = select_all_persons(conn)
        for row in rows:
            message += str(row) + "\n"
        messagebox.showinfo('Person Table', message)


def select_all_students(conn):
    """Query all rows of person table
    :param conn: the connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM student")

    rows = cur.fetchall()

    return rows  # return the rows


def view_all_students():
    """
    Displays a messagebox with all the rows of the student table
    :return: none
    """
    message = ''
    global conn
    with conn:
        rows = select_all_students(conn)
        for row in rows:
            message += str(row) + "\n"
        messagebox.showinfo('Student Table', message)


m = tkinter.Tk()
'''
widgets
'''
m.title('GUI Database')
tkinter.Button(m, text="Create Database & Table", width=25, state=tkinter.NORMAL,
               command=create_database_and_tables).grid(row=1, column=0)
view_person = tkinter.Button(m, text='View Person Table', width=25, command=view_all_persons)
view_person.grid(row=6, columnspan=2)
view_student = tkinter.Button(m, text='View Student Table', width=25, command=view_all_students)
view_student.grid(row=7, columnspan=2)
exit_button = tkinter.Button(m, text='Exit', width=25, command=m.destroy)
exit_button.grid(row=8, columnspan=2)
'''
end of widgets
'''

m.mainloop()
