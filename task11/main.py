#===========================================================================================================
# - How to  GET, POST, PUT, DELETE data through json
#===========================================================================================================

from flask import abort
from flask import Flask
from flask import jsonify
from flask import request
from flask import make_response
from flask_httpauth import HTTPBasicAuth
app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol', 
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web', 
        'done': False
    }
]

#===========================================================================================================
# - How to  GET all record  through json
#===========================================================================================================


@app.route('/home/api/v1.0/tasks', methods=['GET'])
@auth.login_required
def get_tasks():
    return jsonify({'tasks': tasks})



#===========================================================================================================
# - How to  GET  specific record through json
#===========================================================================================================

@app.route('/home/api/v1.0/tasks/<int:task_id>', methods=['GET'])
@auth.login_required
def get_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    return jsonify({'task': task[0]})

#===========================================================================================================
# - How to  POST data through json
#===========================================================================================================

@app.route('/home/api/v1.0/tasks', methods=['POST'])
def create_task():
    if not request.json or not 'title' in request.json:
        abort(400)
    task = {
        'id': tasks[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'done': False
    }
    tasks.append(task)
    return jsonify({'task': tasks}), 201

#===========================================================================================================
# - How to  PUT data in json
#===========================================================================================================

@app.route('/home/api/v1.0/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    task[0]['title'] = request.json.get('title', task[0]['title'])
    task[0]['description'] = request.json.get('description', task[0]['description'])
    task[0]['done'] = request.json.get('done', task[0]['done'])
    return jsonify({'task': task[0]})


#===========================================================================================================
# - How to  DELETE in json
#===========================================================================================================

@app.route('/home/api/v1.0/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    tasks.remove(task[0])
    return jsonify(tasks)

#===========================================================================================================
# - How to show message in case of error 
#===========================================================================================================

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
    app.run(debug=True)