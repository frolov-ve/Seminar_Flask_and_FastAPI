from flask import Flask, render_template
from datetime import datetime

"""
Задание №1
📌 Напишите простое веб-приложение на Flask, которое будет
выводить на экран текст "Hello, World!".

Задание №2
📌 Дорабатываем задачу 1.
📌 Добавьте две дополнительные страницы в ваше веб-
приложение:
○ страницу "about"
○ страницу "contact".

Задание №3
📌 Написать функцию, которая будет принимать на вход два
числа и выводить на экран их сумму.

Задание №4
📌 Написать функцию, которая будет принимать на вход строку и
выводить на экран ее длину.

Задание №5
📌 Написать функцию, которая будет выводить на экран HTML
страницу с заголовком "Моя первая HTML страница" и
абзацем "Привет, мир!".

Задание №6
📌 Написать функцию, которая будет выводить на экран HTML
страницу с таблицей, содержащей информацию о студентах.
📌 Таблица должна содержать следующие поля: "Имя",
"Фамилия", "Возраст", "Средний балл".
📌 Данные о студентах должны быть переданы в шаблон через
контекст.

Задание №7
📌 Написать функцию, которая будет выводить на экран HTML
страницу с блоками новостей.
📌 Каждый блок должен содержать заголовок новости,
краткое описание и дату публикации.
📌 Данные о новостях должны быть переданы в шаблон через
контекст.

Задание №8
📌 Создать базовый шаблон для всего сайта, содержащий
общие элементы дизайна (шапка, меню, подвал), и
дочерние шаблоны для каждой отдельной страницы.
📌 Например, создать страницу "О нас" и "Контакты",
используя базовый шаблон.
"""

app = Flask(__name__)


@app.route('/')
def hello_world():
	return 'Hello World!'


@app.route('/about/')
def about():
	return 'about'


@app.route('/contact/')
def contact():
	return 'contact'


@app.route('/<int:num_1>/<int:num_2>/')
def sum_nums(num_1: int, num_2: int) -> str:
	return str(num_1 + num_2)


@app.route('/string/<string:word>')
def word_count(word: str) -> str:
	return str(len(word))


@app.route('/world')
def world():
	return render_template('index.html')


@app.route('/students')
def students():
	header = {
		'firstname': 'Имя',
		'lastname' : 'Фамилия',
		'age'      : 'Возраст',
		'rating'   : 'Средний балл',
		}
	students_list = [
		{
			'firstname': 'Иван',
			'lastname' : 'Иванов',
			'age'      : 18,
			'rating'   : 4,
			},
		{
			'firstname': 'Федор',
			'lastname' : 'Федоров',
			'age'      : 20,
			'rating'   : 3,
			},
		{
			'firstname': 'Илья',
			'lastname' : 'Егоров',
			'age'      : 19,
			'rating'   : 5,
			}]
	return render_template('index.html', **header, students_list=students_list)


@app.route('/news')
def news():

	news_block = [
		{
			'title': 'Новость_1',
			'description' : 'Описание_1',
			'create_at'      : datetime.now().strftime('%H:%M - %m.%d.%y года'),
			},
		{
			'title': 'Новость_2',
			'description' : 'Описание_2',
			'create_at'      : datetime.now().strftime('%H:%M - %m.%d.%y года'),
			},
		{
			'title': 'Новость_3',
			'description' : 'Описание_3',
			'create_at'      : datetime.now().strftime('%H:%M - %m.%d.%y года'),
			}]
	return render_template('news.html', news_block=news_block)


if __name__ == '__main__':
	app.run(debug=True)
