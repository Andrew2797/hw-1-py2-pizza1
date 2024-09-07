from flask import Flask , render_template


app=Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/page_2/")
def page_2():
    return render_template("page_2.html")
