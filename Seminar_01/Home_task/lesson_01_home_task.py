from flask import Flask, render_template

"""
Создать базовый шаблон для интернет-магазина, содержащий общие элементы дизайна (шапка, меню, подвал),
и дочерние шаблоны для страниц категорий товаров и отдельных товаров.
Например, создать страницы «Одежда», «Обувь» и «Куртка», используя базовый шаблон.
"""

app = Flask(__name__)


@app.route('/')
def base():
	return render_template('base.html')


@app.route('/about/')
def about():
	return render_template('about.html')


@app.route('/contact/')
def contact():
	return render_template('contact.html')


if __name__ == '__main__':
	app.run(debug=True)