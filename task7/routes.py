from flask import Flask
from flask import render_template
from flask import request, jsonify
from flask import jsonify
app = Flask(__name__)      

data = {'message': 'hello world'}

@app.route('/home', methods=['GET'])
def get_Api():
    return jsonify(data)

@app.route('/home', methods=['POST'])
def post_Api():
	data = request.json['data']
	count = len(data)
	response = [
		{'received': data,
		 'count': count
		}
	]

	return jsonify(response)
 
# @app.route('/')
# def home():
#   return render_template('home.html')
# @app.route('/about')
# def about():
# 	return render_template('about.html')

if __name__ == '__main__':
  app.run(host='localhost', debug=True)
