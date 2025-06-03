# Создайте свой HTML-шаблон (файл base.html).
# Создайте страницы home.html и about.html, которые будут расширять шаблон и заполнять его контентом.

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
