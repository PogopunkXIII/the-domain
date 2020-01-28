from flask import Flask, jsonify, abort, make_response, request
import network
domain = Flask(__name__)

@domain.route('/network/wol', methods=['POST'])
def wakeComp():
    if not request.json or not 'computer_name' in request.json:
        abort(400)
    network.wake_on_lan(request.json['computer_name'])
    return "", 200

@domain.route('/todo/api/v1.0/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})

@domain.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    return jsonify({'task': task[0]})

@domain.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not Found'}), 404)

if __name__ == '__main__':
	domain.run(debug=True)
