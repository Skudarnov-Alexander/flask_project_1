from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def main():
    return render_template("index.html")


@app.route("/departure")
def departure():
    return render_template("departure.html")


@app.route("/tour")
def tour():
    return render_template("tour.html")


app.run()
