# Создайте свой HTML-шаблон (файл base.html).
# Создайте страницы home.html и about.html, которые будут расширять шаблон и заполнять его контентом.

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    context = {
        "title" : "Главная страница сайта"
    }
    return render_template("home.html", **context)

@app.route("/blog/")
def blog():
    context = {
        "title": "Страница блога"
    }
    return render_template("about.html", **context)

if __name__ == "__main__":
    app.run()
