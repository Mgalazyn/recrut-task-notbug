from flask import Flask, jsonify, request
from flask_restful import Api, Resource

app = Flask(__name__)


tasks = {
    'task1': {'title': 'Buy groceries', 'completed': False},
    'task2': {'title': 'Finish project', 'completed': False},
    'task3': {'title': 'Call dentist', 'completed': True},
}


@app.route('/tasks', methods=['GET'])
def get_all_tasks():
    return jsonify(list(tasks.values()))


@app.route('/tasks/create', methods=['POST'])
def create_task():
    data = request.json
    task_id = f'task{len(tasks) + 1}'
    tasks[task_id] = {'title': data['title'], 'completed': False}
    return jsonify({'success': True, 'task_id': task_id}), 201


@app.route('/tasks/<task_id>', methods=['GET'])
def get_task(task_id):
    task = tasks.get(task_id)
    if task is None:
        return jsonify({'error': 'Task not found'}), 404
    return jsonify(task)


@app.route('/tasks/<task_id>/update', methods=['PUT'])
def update_task(task_id):
    task = tasks.get(task_id)
    if task is None:
        return jsonify({'error': 'Task not found'}), 404
    data = request.json
    task['title'] = data.get('title', task['title'])
    task['completed'] = data.get('completed', task['completed'])
    return jsonify({'success': True})


@app.route('/tasks/<task_id>/delete', methods=['DELETE'])
def delete_task(task_id):
    task = tasks.pop(task_id, None)
    if task is None:
        return jsonify({'error': 'Task not found'}), 404
    return jsonify({'success': True})


if __name__ == '__main__':
    app.run(debug=True)
