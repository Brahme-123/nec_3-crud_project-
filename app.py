from flask import Flask, render_template, request, redirect, send_from_directory
import sqlite3

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()

    cur.execute('''
  CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
 )
''')
    

    conn.commit()
    conn.close()

init_db()

@app.route('/')
def home():
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()

    cur.execute("SELECT * FROM users")
    users = cur.fetchall()

    conn.close()

    return render_template('index.html', users=users)

@app.route('/add', methods=['POST'])
def add():
    name = request.form['name']

    conn = sqlite3.connect('database.db')
    cur = conn.cursor()

    cur.execute("INSERT INTO users(name) VALUES(?)", (name,))
    conn.commit()
    conn.close()

    return redirect('/')

@app.route('/edit/<int:id>')
def edit(id):
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()

    cur.execute("SELECT * FROM users WHERE id=?", (id,))
    user = cur.fetchone()

    conn.close()

    return render_template('edit.html', user=user)

@app.route('/update/<int:id>', methods=['POST'])
def update(id):
    name = request.form['name']

    conn = sqlite3.connect('database.db')
    cur = conn.cursor()

    cur.execute(
        "UPDATE users SET name=? WHERE id=?",
        (name, id)
    )

    conn.commit()
    conn.close()

    return redirect('/')

@app.route('/delete/<int:id>')
def delete(id):
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()

    cur.execute("DELETE FROM users WHERE id=?", (id,))
    conn.commit()
    conn.close()

    return redirect('/')


@app.route('/output/<path:filename>')
def output_file(filename):
    return send_from_directory('output', filename)

if __name__ == '__main__':
    app.run(debug=True)