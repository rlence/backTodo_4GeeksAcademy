"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/todo', methods=['GET'])
def get_all_todos():
    todos = db.session.query(User).all()
    new_list = []
    for todo in todos:
        print(todo.todo)
        obj = {
            "id":todo.id,
            "todo":todo.todo,
            "check":todo.check
        }
        new_list.append(obj)
    response_body = {
        'todos': new_list
    }
    return jsonify(response_body), 200

@app.route('/create/todo', methods=['POST'])
def create_todo():
    id= request.json['id']
    todo = request.json['todo']
    check = request.json['check']
    new_todo = User(id, todo, check)
    db.session.add(new_todo)
    db.session.commit()
    response_body = {
        "msg": "create, todo"
    }

    return jsonify(response_body), 200

@app.route('/delete/todo/<todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    todo = User.query.filter(User.id == todo_id).first()
    db.session.delete(todo)
    db.session.commit()
    response_body = {
        'msg': "todo delete"
    }
    return jsonify(response_body), 200

# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
