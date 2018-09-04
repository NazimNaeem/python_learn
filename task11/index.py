import sqlite3
from sqlite3 import Error
from flask import abort
from flask import Flask
from flask import jsonify
from flask import request
from flask import make_response
from flask_httpauth import HTTPBasicAuth
app = Flask(__name__)

#========================================================================================
# Funtion to authenticate the user
#========================================================================================

auth = HTTPBasicAuth()
@auth.get_password
def get_password(username):
    conn = create_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM login_tb WHERE username = ?',(username,) )
    rows = cur.fetchall()
    for row in rows:
        if username == row[1]:
            return row[2]
        return None

#========================================================================================
# Funtion to show message to Unauthorized user
#========================================================================================

@auth.error_handler
def unauthorized():
    return make_response(jsonify({'error': 'Unauthorized access'}), 401)



#========================================================================================
# Funtion to get the all the record from the database
#========================================================================================

@app.route('/ebryx/api/v1.0/emp', methods=['GET'])
def get_emp():
    conn = create_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM ebryx")
    result = list()
    rows = cur.fetchall()
    
    for row in rows:
        d = {'Id':row[0],
             'Name':row[1],
             'Designation':row[2],
             'Manager':row[3]
            }
        result.append(d)
    return jsonify(result)


#========================================================================================
# Funtion to get the specific record from the database
#========================================================================================


@app.route('/ebryx/api/v1.0/emp/<int:emp_id>', methods=['GET'])
def get_task(emp_id):
    conn = create_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM ebryx WHERE id = ?', (emp_id,))
    rows = cur.fetchall()
    if len(rows) == 0:
        abort(404)
    for row in rows:
        d = {'Id':row[0],
             'Name':row[1],
             'Designation':row[2],
             'Manger':row[3]
            }
        
    return jsonify(d)

#========================================================================================
# Funtion to post the data in the database
#========================================================================================
    
@app.route('/ebryx/api/v1.0/emp', methods=['POST'])
@auth.login_required
def create_task():

    conn = create_connection()
    cur = conn.cursor()
    cur.execute('INSERT INTO ebryx (name,designation,manager) VALUES (?,?,?)',
               (request.form['name'],
                request.form['designation'],
                request.form['manager'])
               )
    conn.commit()
    return str(cur.lastrowid)

#========================================================================================
# Funtion to Update the specific record from the database
#========================================================================================

@app.route('/ebryx/api/v1.0/emp/<int:emp_id>', methods=['PUT'])
def update_task(emp_id):
    conn = create_connection()
    cur = conn.cursor()
    cur.execute('UPDATE ebryx  SET name = ?, designation = ?, manager = ? WHERE id = ?',
               (request.form['name'],
                request.form['designation'],
                request.form['manager'],emp_id)
               )
    conn.commit()
    return str(cur.lastrowid)

#========================================================================================
# Funtion to delete the specific record from the database
#========================================================================================

@app.route('/ebryx/api/v1.0/emp/<int:emp_id>', methods=['DELETE'])
def delete_task(emp_id):
    conn = create_connection()
    cur = conn.cursor()
    cur.execute('DELETE FROM ebryx WHERE id = ?',
               (emp_id,)
               )
    conn.commit()
    
#========================================================================================
# Funtion to post the username and password in the database
#========================================================================================
    
@app.route('/ebryx/api/v1.0/login', methods=['POST'])
def user_signup():

    conn = create_connection()
    cur = conn.cursor()
    cur.execute('INSERT INTO login_tb (username,password) VALUES (?,?)',
               (request.form['username'],
                request.form['password'])
               )
    conn.commit()

    return "User signup Successfully"

#========================================================================================
# Funtion to show error 
#========================================================================================

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


 
#========================================================================================
# Funtion to create  a connection with database
#========================================================================================

def create_connection():
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    try:
        conn = sqlite3.connect("company.db")
        return conn
    except Error as e:
        print(e)
 
    return None
 
 

 
if __name__ == '__main__':
    app.run(port=5005, debug=True)