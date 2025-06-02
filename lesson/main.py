from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def chessmans(password = None):
    context = {
        "caption" : "Сильнейшие шахматисты",
        "magnus_ex_carlson" : "Узнать о Магнусе Карлсоне",
    }
    return render_template("hometask_cards.html", **context)

@app.route("/shablon")
def chessmans2(password = None):
    context = {
        "caption" : "Гарри Каспаров",
        "magnus_ex_carlson" : "Перейти на сайт Магнуса Карлсона",
    }
    return render_template("hometask_cards.html", **context)

@app.route("/sportsmans/")
def sportsmans(password = None):
    return render_template("practice.html")

@app.route("/new/")
@app.route("/newpage/")
@app.route("/новаястраница/")
def new():
    return "new page"

if __name__ == "__main__":
    app.run()
