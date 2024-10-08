from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configuration for SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

class Todo(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   title = db.Column(db.String(100))
   complete = db.Column(db.Boolean)

def __repr__(self):
    return f'<User {self.title}>'
   
with app.app_context():
    db.create_all()



@app.get("/")
def home():
    todo_list = db.session.query(Todo).all()
    return render_template("base.htm", todo_list=todo_list)

@app.post("/add")
def add():
    title = request.form.get("title")
    new_todo = Todo(title=title, complete=False)
    db.session.add(new_todo)
    db.session.commit()
    return redirect(url_for("home"))

@app.get("/update/<int:todo_id>")
def update(todo_id):
    todo = Todo.query.get(todo_id)
    todo.complete = not todo.complete
    db.session.commit()
    return redirect(url_for("home"))

@app.get("/delete/<int:todo_id>")
def delete(todo_id):
    todo = db.session.query(Todo).filter(Todo.id == Todo.id).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("home"))