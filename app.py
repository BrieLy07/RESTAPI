from flask import Flask, request, jsonify

app = Flask(__name__)

# Lista de tareas (simulación de base de datos)
tasks = [
    {"id": 1, "title": "Comprar comida", "done": False},
    {"id": 2, "title": "Lavar el auto", "done": True},
]

# Obtener todas las tareas
@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

# Crear una nueva tarea
@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    new_task = {"id": len(tasks) + 1, "title": data['title'], "done": False}
    tasks.append(new_task)
    return jsonify(new_task), 201

# Actualizar una tarea
@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    data = request.get_json()
    for task in tasks:
        if task['id'] == task_id:
            task['title'] = data.get('title', task['title'])
            task['done'] = data.get('done', task['done'])
            return jsonify(task)
    return jsonify({"error": "Task not found"}), 404

# Eliminar una tarea
@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task['id'] != task_id]
    return jsonify({"message": "Task deleted"}), 200

# Ejecutar el servidor
if __name__ == '__main__':
    app.run(debug=True)
