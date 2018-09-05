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
    return make_response(" You are not authorized to access api")



#========================================================================================
# Funtion to get the all the record from the url
#========================================================================================

@app.route('/ebryx/api/<url>', methods=['GET'])
@auth.login_required
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


    # else:
    
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
    app.run(host="localhost", debug=True)