from flask import Flask, redirect, url_for, render_template, request
from langtool import json_to_list, add_term, delete_term, edit_term, obtain_translation, practice_import, add_practice, reset_practice, validate, complete_practice, settings_import, change_settings

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")


@app.route('/<name>')
def namepage(name):
    return render_template('index.html', content=name, terms=json_to_list())


@app.route("/addTerm/", methods=['POST', 'GET'])
def new_term():
    if request.method == "POST":
        term = request.form['tm']
        trans = request.form['tl']
        add_term(term, trans)
        return redirect(url_for("term_list"))
    else:
        return render_template("addTerm.html")


@app.route('/edit/<name>/', methods=['POST', 'GET'])
def edit(name):
    if request.method == "POST":
        term = request.form['tm']
        trans = request.form['tl']
        edit_term(term, trans)
        return redirect(url_for("term_list"))
    else:
        return render_template("editTerm.html", termdefault=name.replace(' ', '_'), transdefault=obtain_translation(name).replace(' ', '_'))


@app.route("/<usr>")
def user(usr):
    return f"<h1>{usr}</h1>"


@app.route("/list/", methods=['POST', 'GET'])
def term_list():
    if request.method == 'POST':
        return redirect(url_for("term_list"))
    else:
        return render_template("termlist.html", terms=json_to_list())


@app.route("/practice/settings/", methods=['POST', 'GET'])
def practice_settings():
    if request.method == 'POST':
        mode = request.form['mode']
        length = int(request.form['length'])
        change_settings('mode', mode)
        change_settings('length', length)
        reset_practice()
        return redirect(url_for("practice"))
    else:
        return render_template("settings.html", settings=settings_import(), totalTerms=len(json_to_list()))


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
def practice_reset():
    reset_practice()
    return redirect(url_for("practice"))


@app.route("/practice/complete/", methods=['GET'])
def practice_complete():
    complete_practice()
    return redirect(url_for("home"))


@app.route('/submit/<name>/', methods=['GET'])
def submit(name):
    add_practice(name)
    return redirect(url_for("practice"))


@app.route('/delete/<name>/', methods=['GET'])
def delete(name):
    delete_term(name)
    return redirect(url_for("term_list"))


@app.route("/admin/")
def admin():
    return redirect(url_for("namepage", name="Admin!"))


if __name__ == '__main__':
    app.run(debug=True)