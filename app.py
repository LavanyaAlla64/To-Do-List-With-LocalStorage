from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Create a list to store tasks
tasks = []

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/add_task', methods=['POST'])
def add_task():
    new_task = request.form.get('new_task')
    if new_task:
        tasks.append(new_task)
    return redirect(url_for('index'))

@app.route('/delete_task/<int:task_index>')
def delete_task(task_index):
    if 0 <= task_index < len(tasks):
        tasks.pop(task_index)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
