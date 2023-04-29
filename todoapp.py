from flask import Flask
from flask import render_template
from flask import request
from flask import redirect


app = Flask(__name__)

tasks = []

@app.route('/')
def todolist():
    
    return render_template('todoform.html', tasks=tasks)

@app.route('/submit', methods = ['POST'])
def add_task():
    
    task = request.form['task']
    email = request.form['email']
    priority = request.form['priority']
    tasks.append({'task': task, 'email': email, 'priority': priority})
    return redirect(('/'))
    
@app.route('/clear', methods = ['POST'])
def clear_list():
    global tasks
    tasks = []
    return redirect('/')

if __name__ == '__main__':
    app.run()