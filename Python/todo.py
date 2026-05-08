from flask import Flask, render_template, request, redirect

app = Flask(__name__)
TODO_FILE = "tasks.txt"

# Read tasks from file
def load_tasks():
    try:
        with open(TODO_FILE, "r") as f:
            return [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        return []

# Save tasks to file
def save_tasks(tasks):
    with open(TODO_FILE, "w") as f:
        for task in tasks:
            f.write(task + "\n")

@app.route('/')
def index():
    tasks = load_tasks()
    return render_template('index2.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add():
    task = request.form.get('task')
    if task:
        tasks = load_tasks()
        tasks.append(task)
        save_tasks(tasks)
    return redirect('/')

@app.route('/delete/<int:task_id>')
def delete(task_id):
    tasks = load_tasks()
    if 0 <= task_id < len(tasks):
        tasks.pop(task_id)
        save_tasks(tasks)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
