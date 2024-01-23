from flask import Flask, render_template, url_for, flash, redirect, request, make_response
from secrets import token_hex

app = Flask(__name__)

app.secret_key = token_hex()

"""
Создать страницу, на которой будет форма для ввода имени
и кнопка "Отправить"
При нажатии на кнопку будет произведено
перенаправление на страницу с flash сообщением, где будет
выведено "Привет, {имя}!".
"""


@app.get('/form')
def form():
    return render_template('login.html')


@app.post('/form')
def hello():
    if not request.form['name']:
        flash('Введите имя!', 'danger')
        return redirect(url_for('hello'))
    response = make_response('Cookie')
    response.set_cookie('name', request.form['name'])
    return redirect(url_for('say_hi', username=request.form['name']))


@app.get('/form/<username>')
def say_hi(username):
    flash(f'Привет {username}', 'success')
    context = {'name': username}
    return render_template('hi.html', **context)


if __name__ == '__main__':
    app.run(debug=True)
