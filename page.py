from flask import Flask, redirect, url_for, render_template
from __init__ import json_to_list

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")


@app.route('/<name>')
def namepage(name):
    return render_template('index.html', content=name, terms=json_to_list())


@app.route("/list/")
def termlist():
    return render_template("termlist.html", terms=json_to_list())


@app.route("/admin/")
def admin():
    return redirect(url_for("namepage", name="Admin!"))


if __name__ == '__main__':
    app.run()