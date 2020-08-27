from flask import Flask, redirect, url_for, render_template, request
from langtool import json_to_list, add_term,delete_term, edit_term, obtain_translation, practice_import, add_practice, reset_practice, validate

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
        return redirect(url_for("termlist"))
    else:
        return render_template("addTerm.html")


@app.route('/edit/<name>/', methods=['POST', 'GET'])
def edit(name):
    if request.method == "POST":
        term = request.form['tm']
        trans = request.form['tl']
        edit_term(term, trans)
        return redirect(url_for("termlist"))
    else:
        return render_template("editTerm.html", termdefault=name.replace(' ', '_'), transdefault=obtain_translation(name).replace(' ', '_'))


@app.route("/<usr>")
def user(usr):
    return f"<h1>{usr}</h1>"


@app.route("/list/", methods=['POST', 'GET'])
def termlist():
    if request.method == 'POST':
        return redirect(url_for("termlist"))
    else:
        return render_template("termlist.html", terms=json_to_list())


@app.route("/practice/", methods=['POST', 'GET'])
def practice():
    if request.method == "POST":
        word = request.form['word']
        answer = request.form['answer']
        validate(word, answer)
        return redirect(url_for("practice"))
    else:
        return render_template("practice.html",
                               hits=practice_import()['hits'],
                               misses=practice_import()['misses'],
                               terms=practice_import()['terms'],
                               results=practice_import()['results'],
                               answers=practice_import()['answers'],
                               length=practice_import()['length'])


@app.route("/practice/reset/", methods=['GET'])
def practicereset():
    reset_practice()
    return redirect(url_for("practice"))


@app.route('/submit/<name>/', methods=['GET'])
def submit(name):
    add_practice(name)
    return redirect(url_for("practice"))


@app.route('/delete/<name>/', methods=['GET'])
def delete(name):
    delete_term(name)
    return redirect(url_for("termlist"))


@app.route("/admin/")
def admin():
    return redirect(url_for("namepage", name="Admin!"))


if __name__ == '__main__':
    app.run(debug=True)