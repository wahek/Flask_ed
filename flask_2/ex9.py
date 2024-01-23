from flask import Flask, render_template, url_for, flash, redirect, request, make_response
from secrets import token_hex

app = Flask(__name__)

app.secret_key = token_hex()

"""
Создать страницу, на которой будет форма для ввода имени
и электронной почты
При отправке которой будет создан cookie файл с данными
пользователя
Также будет произведено перенаправление на страницу
приветствия, где будет отображаться имя пользователя.
На странице приветствия должна быть кнопка "Выйти"
При нажатии на кнопку будет удален cookie файл с данными
пользователя и произведено перенаправление на страницу
ввода имени и электронной почты.
"""


@app.get('/email')
def email():
    return render_template('email.html')


@app.post('/email')
def cookie():
    response = make_response("Cookie установлен")
    response.set_cookie('username', 'ewf')
    response.set_cookie('email', 'wefq')
    return redirect(url_for('coo'))


@app.get('/email/coo')
def coo():
    print(request.cookies.get('username'))
    return render_template('hi.html')


if __name__ == '__main__':
    app.run(debug=True)
