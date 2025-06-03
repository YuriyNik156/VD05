# Задание 2:
# Создайте новое приложение Flask, создайте структуру проекта с папками static и templates, в папке templates
# должны быть 3 html файла: index, blog, contacts (главная страница, страница блога и контакты).
# Заполните их информацией и выведите силами flask сервера, используя функцию render_template().
# Обязательно на всех страницах сделайте меню, которое будет работать именно при запуске проекта через flask.

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index(password = None):
    return render_template("index.html")

@app.route("/blog/")
def blog(password = None):
    return render_template("blog.html")

@app.route("/contacts/")
def contacts(password = None):
    return render_template("contacts.html")

if __name__ == "__main__":
    app.run()
