from flask import (Flask, render_template)

import sqlite3

# PATH = "db/jobs.sqlite"

app = Flask(__name__)

# def open_connection():
#     db = getattr(g, '_database', None)
#     if db is None:
#         db.row_factory = sqlite3.Row
#         db = g._database = sqlite3.connect(PATH)
#     return db

# def execute_sql(sql, values, commit, single):
#     values = ()
#     commit = False
#     single = False
#     connection = open_connection()
#     connection.execute(sql, values)
#     if commit == True:
#         results = connection.commit()
#     else:
#         results = cursor.fetchone() 
#         if single else cursor.fetchall()

@app.route('/')
@app.route('/jobs')
def jobs():
     return render_template(
         "index.html"
    )