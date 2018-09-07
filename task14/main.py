import jwt
import sqlite3
import requests
import datetime
from flask import Flask
from flask import jsonify
from flask import request
from bs4 import BeautifulSoup
from flask import make_response
from passlib.hash import pbkdf2_sha256 as sha256
from functools import wraps

app = Flask(__name__)
app.config['SECRET_KEY'] = "Thisisthesecretkey"
def token_required(f):
    @wraps(f)
    def decorated(**kwargs):
        token = request.headers.get('token')
        if not token:
            return jsonify({'message':'token is missing'}),403
        try:
            data =jwt.decode(token,app.config['SECRET_KEY'])
        except:
            return jsonify({'message':'token is  invalid'}),403
        return f(**kwargs)
    return decorated
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

@app.route('/ebryx/api/task14/registration', methods=['POST'])
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
    return jsonify({
            'message': 'User {} was created'.format(request.form['username']),
            })

    
    #return "User signup Successfully"

#========================================================================================
# Funtion to login user 
#========================================================================================

@app.route('/ebryx/api/task14/login', methods=['POST'])
def user_login():
    conn = create_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM login_tb WHERE username = ?',(request.form['username'],) )
    
    current_user = cur.fetchone()
    if not current_user:
        return "User does not exist"
    
    if verify_hash(request.form['password'],current_user[2]):                
        token = jwt.encode({'username': current_user[1],'exp':datetime.datetime.utcnow() + datetime.timedelta(hours=6)},app.config['SECRET_KEY'])
        return jsonify({'token' :token.decode('UTF-8')})
    return make_response('Could not verify', 401,{'WWW-Authenticate':'Basic realm="Login Required"'})
    

#========================================================================================
# Funtion to check token is valid or not
#========================================================================================
@app.route('/ebryx/api/task14')
@token_required
def protected():
    return jsonify({'message':'token is valid'})

#========================================================================================
# Funtion to get the all the record from the url
#========================================================================================

@app.route('/ebryx/api/task14/<url>', methods=['GET'])
@token_required
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

#========================================================================================
# Funtion to encode the password of user
#========================================================================================

def generate_hash(password):
    return sha256.hash(password)

#========================================================================================
# Funtion to decode the password of user
#========================================================================================

def verify_hash(password, hash):
    return sha256.verify(password, hash)
 
if __name__ == '__main__':
    app.run(host="localhost", debug=True)