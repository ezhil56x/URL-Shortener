import random
import sqlite3

from flask import Flask, redirect, render_template, request

app = Flask(__name__, template_folder='templates')


def randomString(length=6):
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    while True:
        result_str = ''.join(random.choice(letters) for i in range(length))
        db = sqlite3.connect('data.db')
        cursor = db.cursor()
        cursor.execute(
            'SELECT shorturl FROM urls WHERE shorturl = ?', (result_str,))
        existing_url = cursor.fetchone()
        if not existing_url:
            return result_str


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        longurl = request.form.get('longurl')

        if longurl == '':
            return render_template('index.html', error='Please enter a URL')
        else:
            db = sqlite3.connect('data.db')
            cursor = db.cursor()
            cursor.execute(
                'CREATE TABLE IF NOT EXISTS urls (id INTEGER PRIMARY KEY, longurl TEXT, shorturl TEXT UNIQUE)')
            cursor.execute(
                'SELECT shorturl FROM urls WHERE longurl = ?', (longurl,))
            result = cursor.fetchone()

            if result:
                return render_template('index.html', host=request.host_url, shorturl=result[0])

            else:
                shorturl = randomString(6)
                db = sqlite3.connect('data.db')
                cursor = db.cursor()
                cursor.execute(
                    'CREATE TABLE IF NOT EXISTS urls (id INTEGER PRIMARY KEY, longurl TEXT, shorturl TEXT UNIQUE)')
                cursor.execute(
                    'INSERT INTO urls (longurl, shorturl) VALUES (?, ?)', (longurl, shorturl))
                db.commit()
                return render_template('index.html', host=request.host_url, shorturl=shorturl)

    if request.method == 'GET':
        return render_template('index.html')


@app.route('/<shorturl>')
def redirect_shorturl(shorturl):

    db = sqlite3.connect('data.db')
    cursor = db.cursor()
    cursor.execute('SELECT longurl FROM urls WHERE shorturl = ?', (shorturl,))
    result = cursor.fetchone()

    if result:
        return redirect(result[0])
    else:
        return "URL does not exist"


app.run(debug=True)
