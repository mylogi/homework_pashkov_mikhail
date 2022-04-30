"""Task 1

Create a table

Create a table of your choice inside the sample SQLite database, rename it, and add a new column. Insert a couple rows
inside your table. Also, perform UPDATE and DELETE statements on inserted rows.

As a solution to this task, create a file named: task1.sql, with all the SQL statements you have used to accomplish this
task

"""

# Solution:
import sqlite3

con = sqlite3.connect('task1_database.db')

cursorObj = con.cursor()

# def sql_table(con_example):
#     cursorObj.execute(
#         "CREATE TABLE employees(id integer PRIMARY KEY, name text, salary real, department text, position text, hireDate text)"
#     )
#
#     con_example.commit()


# def add_column(con_example):
#     cursorObj.execute("ALTER TABLE employees ADD new_column_name text")
#
#     con_example.commit()


# def rename_db(con_example):
#     cursorObj.execute("ALTER TABLE table1_try RENAME TO employees")
#
#     con_example.commit()

# def delete_column(con_example):
# cursorObj.execute("ALTER TABLE employees RENAME TO _employees_old")
# cursorObj.execute(
#     "CREATE TABLE employees(id integer PRIMARY KEY, name text, salary real, department text, position text, hireDate text)")

# list_of_insert =
# cursorObj.execute(
#     "INSERT INTO employees(id, name, salary, department, position, hireDate) VALUES(?, ?, ?, ?, ?, ?)", cursorObj.execute("SELECT * FROM _employees_old"))
# con_example.commit()

# def sql_insert(con_example, entities_tuple):
#     cursorObj.execute(
#         'INSERT INTO employees(id, name, salary, department, position, hireDate) VALUES(?, ?, ?, ?, ?, ?)',
#         entities_tuple)
#
#     con_example.commit()
#
#
# entities = (2, 'Andrew', 800, 'IT', 'Tech', '2018-02-06')
#
#
# def sql_update(con_example):
#     cursorObj.execute('UPDATE employees SET name = "Rogers" where id = 2')
#
#     con_example.commit()

# sql_table(con)
# sql_insert(con, entities)
# sql_update(con)
# add_column(con)
# rename_db(con)
# delete_column(con)
