from flask import Flask, render_template, request, redirect, session, flash
import sqlite3,stripe
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.secret_key = 'y1'
stripe.api_key = 'y2'
stripe_publishable_key = 'y3'


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
db = SQLAlchemy(app)

class Wines(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), nullable=False)
    type = db.Column(db.String(80), nullable=False)
    def __str__(self):
        return f'name -  {self.name}, type - {self.type}'
with app.app_context():
    db.create_all()
    password = 'test'




def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


def create_table():
    conn = get_db_connection()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
        user = cursor.fetchone()

        if user:
            flash('Username already exists', 'error')
            return redirect('/register')

        cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
        conn.commit()

        session['username'] = username

        flash('Registration successful', 'success')
        return redirect('/')

    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password))
        user = cursor.fetchone()

        if user:
            session['username'] = username
            flash('Login successful', 'success')
            return redirect('/')

        flash('Invalid username or password', 'error')
        return redirect('/login')

    return render_template('login.html')



@app.route('/logout')
def logout():
    session.pop('username', None)
    flash('Logged out successfully', 'info')
    return redirect('/')
@app.route('/favorites')
def favorites():
    return render_template('favorites.html')
@app.route('/wines', methods=['GET', 'POST'])
def wines():
    if request.method == 'POST':
        name = request.form['name']
        type = request.form['type']

        if name == '' or type == '':
            flash('Please enter values for all fields', 'error')
        else:
            new_wine = Wines(name=name, type=type)
            db.session.add(new_wine)
            db.session.commit()
            flash('Wine added successfully', 'info')

        return redirect('/wines')

    wines = Wines.query.all()
    return render_template('wines.html', winess=wines)
@app.route('/checkout', methods=['GET'])
def checkout():
    return render_template('checkout.html', key=stripe_publishable_key)
@app.route('/charge', methods=['POST'])
def charge():
    token = request.form['stripeToken']

    try:

        charge = stripe.Charge.create(
            amount=1000,
            currency='usd',
            description='Example Charge',
            source=token
        )

        return render_template('succsess.html')
    except stripe.error.CardError as e:
        return render_template('error.html', error=e)


if __name__ == '__main__':
    create_table()
    app.run(debug=True)