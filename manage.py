from app import app
from app.models import Todo
from flask_script import Manager


manager = Manager(app)


@manager.command
def save():
    todo = Todo(content="todo base on flask")
    todo.save()


if __name__ == '__main__':
    manager.run()