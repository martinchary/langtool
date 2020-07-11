from flask import Flask, redirect, url_for, render_template, request
from langtool import json_to_list, add_term

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")


@app.route('/<name>')
def namepage(name):
    return render_template('index.html', content=name, terms=json_to_list())


@app.route("/addTerm/", methods=['POST', 'GET'])
def addTerm():
    if request.method == "POST":
        term = request.form['tm']
        trans = request.form['tl']
        add_term(term, trans)
        # return redirect(url_for("user", usr=term+trans))
        return redirect(url_for("termlist"))
    else:
        return render_template("addTerm.html")


@app.route("/<usr>")
def user(usr):
    return f"<h1>{usr}</h1>"


@app.route("/list/")
def termlist():
    return render_template("termlist.html", terms=json_to_list())


@app.route("/admin/")
def admin():
    return redirect(url_for("namepage", name="Admin!"))


if __name__ == '__main__':
    app.run(debug=True)