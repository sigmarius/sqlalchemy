from flask import Flask, render_template, request, flash
# pip install flask_sqlalchemy
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# генерация ключа => Python Console => import os => os.urandom(20).hex()
app.config['SECRET_KEY'] = '2f08ce45d761e9fdd097ac221e15f8c34c2635b7'


db = SQLAlchemy(app)


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), unique=True)
    psw = db.Column(db.String(500), nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<users {self.id}>"


class Profiles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=True)
    age = db.Column(db.Integer)
    city = db.Column(db.String(100))

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self):
        return f"<profiles {self.id}>"

# создание БД и таблиц в БД => Python Console => from app import db => db.create_all()


@app.route('/')
def index():
    return render_template('index.html', title='Главная')


@app.route('/register', methods=('POST', 'GET'))
def register():
    if request.method == 'POST':
        try:
            hash = generate_password_hash(request.form['psw'])
            # именнованные параметры email, psw соответствуют заданным в классе Users
            u = Users(email=request.form['email'], psw=hash)
            # запись о пользователе сохраняется только в сессии, не в БД
            db.session.add(u)
            # перемещает запись из сессии в таблицу БД, файл БД остается прежним
            db.session.flush()

            p = Profiles(name=request.form['name'], age=request.form['age'],
                         city=request.form['city'], user_id = u.id)
            db.session.add(p)
            # физически меняет БД и сохраняет запись в таблице
            db.session.commit()
            flash('Пользователь добавлен успешно', category='success')
        except:
            # откатываем изменения
            db.session.rollback()
            flash('Ошибка при регистрации - невозожно добавить в БД', category='error')
            print('Ошибка добавления в БД')

    return render_template('register.html', title='Регистрация')


if __name__ == '__main__':
    app.run(debug=True)
