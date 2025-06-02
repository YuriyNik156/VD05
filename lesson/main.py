from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def chessmans(password = None):
    context = {
        "caption" : "Сильнейшие шахматисты",
        "number" : 8,
        "list" : ["Yura", "Karina", "Anton", "Nikita"],
        "poem" : ["Мороз и солнце; день чудесный!",
                    "Еще ты дремлешь, друг прелестный —",
                    "Пора, красавица, проснись:",
                    "Открой сомкнуты негой взоры",
                    "Навстречу северной Авроры,",
                    "Звездою севера явись!"
                  ]
    }
    return render_template("shablon.html")

@app.route("/shablon/")
def chessmans2(password = None):
    context = {
        "magnus_ex_carlson" : "Перейти на сайт Магнуса Карлсона",
    }
    return render_template("hometask_cards.html", **context)

@app.route("/sportsmans/")
def sportsmans(password = None):
    context = {
        "magnus_ex_carlson": "Перейти на сайт Магнуса Карлсона",
    }
    return render_template("practice.html", **context)

@app.route("/new/")
@app.route("/newpage/")
@app.route("/новаястраница/")
def new():
    return "new page"

if __name__ == "__main__":
    app.run()
