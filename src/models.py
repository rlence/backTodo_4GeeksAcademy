from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tabelname__='todos'
    id = db.Column(db.Integer, primary_key=True)
    todo = db.Column(db.String(200), unique=False, nullable=False)
    check = db.Column(db.Boolean, unique=False, nullable=False)

    def __init__(self, id, todo, check):
        self.id = id
        self.todo = todo
        self.check = check

    def __repr__(self):
        todo = { 'id':self.id, 'todo':self.todo, 'check':self.check }
        return str(todo)

