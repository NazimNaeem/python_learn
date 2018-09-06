import sqlite3
import requests
from sqlite3 import Error
from flask import abort
from flask import Flask
from flask import jsonify
from flask import request
from bs4 import BeautifulSoup
from flask import make_response
from flask_httpauth import HTTPBasicAuth

from flask_jwt_extended import JWTManager
from flask_jwt_extended import create_access_token
from flask_jwt_extended import create_refresh_token
from flask_jwt_extended import jwt_required 
from flask_jwt_extended import jwt_refresh_token_required
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import get_raw_jwt
from passlib.hash import pbkdf2_sha256 as sha256


app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'jwt-secret-string'
jwt = JWTManager(app)

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


#========================================================================================
# Funtion to register the user
#========================================================================================

@app.route('/ebryx/api/registration', methods=['POST'])
def user_signup():

    conn = create_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM login_tb WHERE username = ?',(request.form['username'],) )
    row = cur.fetchall()
    if row:
        return"user already exist"
    password = generate_hash(request.form['password'])
    cur.execute('INSERT INTO login_tb (username,password) VALUES (?,?)',
               (request.form['username'],
                password)
               )
    conn.commit()
    access_token = create_access_token(identity = request.form['username'])
    refresh_token = create_refresh_token(identity = request.form['username'])
    return jsonify({
            'message': 'User {} was created'.format(request.form['username']),
            'access_token': access_token,
            'refresh_token': refresh_token
            })

    
    #return "User signup Successfully"

#========================================================================================
# Funtion to login user 
#========================================================================================

@app.route('/ebryx/api/login', methods=['POST'])
def user_login():
    conn = create_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM login_tb WHERE username = ?',(request.form['username'],) )
    
    current_user = cur.fetchone()
    if not current_user:
        return "User does not exist"
    
    if verify_hash(request.form['password'],current_user[2]):                
        access_token = create_access_token(identity = request.form['username'])
        refresh_token = create_refresh_token(identity = request.form['username'])
        return jsonify({
                'message': 'User {} logeed in'.format(request.form['username']),
                'access_token': access_token,
                'refresh_token': refresh_token
                })
    else:
        return "wrong credentials"

#========================================================================================
# Funtion to get the all the record from the url
#========================================================================================

@app.route('/ebryx/api/<url>', methods=['GET'])
#  jwt_required token to access this url
@jwt_required
def get_url(url):
    
    source = request.args.get('source')
    if source == "true" or source == "True":
        url_list = list()
        response  = requests.get("https://"+ url)
        data = response.text
        return jsonify(data)
    else:
        url_list = list()
        response  = requests.get("https://"+ url)
        data = response.text
        soup = BeautifulSoup(data,"html.parser")
        for anchor_tag in soup.find_all('a'):
            url_list.append(anchor_tag.get("href"))
        return jsonify(url_list)

 
def generate_hash(password):
    return sha256.hash(password)

def verify_hash(password, hash):
    return sha256.verify(password, hash)
 
if __name__ == '__main__':
    app.run(host="localhost", debug=True)