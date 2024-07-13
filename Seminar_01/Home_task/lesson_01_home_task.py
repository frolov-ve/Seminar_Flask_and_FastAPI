from flask import Flask, render_template

"""
Создать базовый шаблон для интернет-магазина, содержащий общие элементы дизайна (шапка, меню, подвал),
и дочерние шаблоны для страниц категорий товаров и отдельных товаров.
Например, создать страницы «Одежда», «Обувь» и «Куртка», используя базовый шаблон.
"""

app = Flask(__name__)


@app.route('/')
def base_hw():
	return render_template('base_hw.html')


@app.route('/about_hw/')
def about_hw():
	return render_template('about_hw.html')


@app.route('/contacts_hw/')
def contacts_hw():
	return render_template('contacts_hw.html')


@app.route('/main_hw/')
def main_hw():
	return render_template('main_hw.html')


@app.route('/jacket_hw/')
def jacket_hw():
	return render_template('jacket_hw.html')


@app.route('/clothes_hw/')
def clothes_hw():
	return render_template('clothes_hw.html')


@app.route('/shoes_hw/')
def shoes_hw():
	return render_template('shoes_hw.html')


if __name__ == '__main__':
	app.run(debug=True)
