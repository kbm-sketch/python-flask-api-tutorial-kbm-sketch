from flask import Flask,jsonify,request

todos = [
    {"label":'study',"done":False},
    {"label":'work on projects',"done":False},
    {"label":'get some chores done',"done":False}
]

app = Flask(__name__)


@app.route('/todos',methods=['GET'])
def get_todos():
    data = jsonify(todos)
    return data

@app.route('/todos',methods=['POST'])
def add_new_todo():
    request_body = request.json
    print("Incoming request with the following body", request_body)
    todos.append(request_body)
    return jsonify(todos)



@app.route('/todos/<int:position>',methods=['DELETE'])
def delete_todo(position):
    print("This is the position to delete:",position)
    del todos[position]
    return jsonify(todos)


if(__name__) == '__main__':
    app.run(host='0.0.0.0',port=3245,debug=True)