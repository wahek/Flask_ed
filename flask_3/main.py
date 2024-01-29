from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from models import User

"""
Создать форму для регистрации пользователей на сайте. Форма должна содержать поля 
"Имя", "Фамилия", "Email", "Пароль" и кнопку "Зарегистрироваться". 
При отправке формы данные должны сохраняться в базе данных, а пароль должен быть зашифрован.
"""
db = SQLAlchemy()
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'

db.init_app(app)


@app.get('/')
def initial():
    return render_template('index.html')


@app.post('/')
def update():
    user = User(first_name=request.form['first_name'],
                last_name=request.form['last_name'],
                email=request.form['email'],
                password=hash(request.form['password']),

                )
    db.session.add(user)
    db.session.commit()


@app.cli.command("init-db")
def init_db():
    db.create_all()
    print('OK')


@app.cli.command("del-db")
def del_db():
    db.drop_all()
    print('OK')


if __name__ == '__main__':
    app.run()
