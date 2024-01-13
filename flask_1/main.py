from flask import Flask, render_template
import os

app = Flask(__name__)

pict_folder = os.path.join('../', 'static', 'picture')

app.config['UPLOAD_FOLDER'] = pict_folder

html = """
<h1>Моя первая страница HTML</h1>
<p>Привет Мир</p>
"""

students = [{'firstname': 'Alex', 'lastname': 'Kor', 'age': 18, 'score': 2.5},
            {'firstname': 'Alex2', 'lastname': 'Kor2', 'age': 15, 'score': 4.8},
            {'firstname': 'Alex3', 'lastname': 'Kor3', 'age': 14, 'score': 3.4}]


@app.route('/')
def hello():
    return render_template('stud.html', students=students)


@app.route('/about')
def about():
    return "Hi i'm wahek"


@app.route('/contact')
def contact():
    return "https://vk.com/im"


@app.route('/sum/<int:a>/<int:b>/')
def sum_num(a, b):
    return f"{a}+{b}={a + b}"


@app.route('/len/<s>')
def str_(s):
    return f'{len(s)}'


@app.route('/news/<int:num>/')
def get_news(num):
    base = [{'title': 'title1', 'name': 'name1', 'date_pub': '2022'},
            {'title': 'title2', 'name': 'name2', 'date_pub': '2023'},
            {'title': 'title3', 'name': 'name3', 'date_pub': '2024'}
            ]
    context = base[num - 1]
    print(context)
    return render_template('news.html', news=context)


@app.route('/e-com/')
def e_com():
    context = {
        'img_header': os.path.join(app.config['UPLOAD_FOLDER'], 'Header.png'),
        'img_main': os.path.join(app.config['UPLOAD_FOLDER'], 'Feature.png'),
        'img_footer': os.path.join(app.config['UPLOAD_FOLDER'], 'Copyright.png')}
    return render_template('e-com.html', **context)


@app.route('/e-com/jacket')
def e_com_j():
    context = {'title': 'Куртки',
               'prod_name': 'Куртка',
               'img_header': os.path.join(app.config['UPLOAD_FOLDER'], 'Header.png'),
               'img_main': os.path.join(app.config['UPLOAD_FOLDER'], 'Feature.png'),
               'img_footer': os.path.join(app.config['UPLOAD_FOLDER'], 'Copyright.png'),
               'prod_img': os.path.join(app.config['UPLOAD_FOLDER'], 'jacket.png'),
               }
    return render_template('jacket.html', **context)


@app.route('/e-com/boots')
def e_com_b():
    context = {'title': 'Куртки',
               'prod_name': 'Ботинки',
               'img_header': os.path.join(app.config['UPLOAD_FOLDER'], 'Header.png'),
               'img_main': os.path.join(app.config['UPLOAD_FOLDER'], 'Feature.png'),
               'img_footer': os.path.join(app.config['UPLOAD_FOLDER'], 'Copyright.png'),
               'prod_img': os.path.join(app.config['UPLOAD_FOLDER'], 'boots.png'),
               }
    return render_template('boots.html', **context)


@app.route('/e-com/t-shirt')
def e_com_t():
    context = {'title': 'Куртки',
               'prod_name': 'Футболка',
               'img_header': os.path.join(app.config['UPLOAD_FOLDER'], 'Header.png'),
               'img_main': os.path.join(app.config['UPLOAD_FOLDER'], 'Feature.png'),
               'img_footer': os.path.join(app.config['UPLOAD_FOLDER'], 'Copyright.png'),
               'prod_img': os.path.join(app.config['UPLOAD_FOLDER'], 't_shirt.png'),
               }
    return render_template('t_shirt.html', **context)


if __name__ == "__main__":
    app.run(debug=True)
