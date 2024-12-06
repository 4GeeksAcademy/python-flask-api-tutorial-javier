from flask import Flask, jsonify, request 
from flask import Flask
app = Flask(__name__)


todos = [{ "label": "aprender flask", "done": False }] # aca se agrega la nueva tarea del usuario  con post 

@app.route('/todos',methods=['GET'])
def hello_world():
  todos_json = jsonify(todos)
  return todos_json



@app.route('/todos',methods=['POST']) # ACA SE ENVIA LA TEASREA QUE ENVIA EL USERS
def add_new_todo():
  body = request.json # accedemos a la peticion y lo guardamos aca
  todos.append(body) # agrega un nuevo elem a la lista de tareas
  todos_actualizado = jsonify(todos)
  return todos_actualizado, 200


@app.route('/todos/int<positon>',methods=['DELETE']) 
def delete_todo(position):
 todos.remove(todos[position])
 todos_actualizado = jsonify(todos)
 return todos_actualizado, 200


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)

