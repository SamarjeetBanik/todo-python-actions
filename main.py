from flask import Flask, request, jsonify, render_template
from flask_frozen import Freezer

app = Flask(__name__)
freezer = Freezer(app)

# In-memory storage for to-do items
todos = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)

@app.route('/todos', methods=['POST'])
def add_todo():
    todo = request.json.get('todo')
    if todo:
        todos.append(todo)
        return jsonify({'message': 'Todo added successfully!'}), 201
    return jsonify({'message': 'Invalid input'}), 400

@app.route('/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    if 0 <= todo_id < len(todos):
        todos.pop(todo_id)
        return jsonify({'message': 'Todo deleted successfully!'})
    return jsonify({'message': 'Todo not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)

# Add this to freeze the app
@freezer.register_generator
def url_generator():
    yield 'index'
    yield 'get_todos'