from flask import render_template, redirect, request
from flask_app import app
from flask_app.models.dojo import Dojo

@app.route('/')
def index():
    return redirect('/dojos')

@app.route('/dojos')
def dojos():
    dojos = Dojo.all_dojos()
    return render_template("create_dojo.html", dojo = dojos)

@app.route('/add/dojo', methods=['POST'])
def add_dojo():
    Dojo.save_dojo_db(request.form)
    return redirect('/dojos')

@app.route('/dojo/<int:id>')
def dojo_show(id):
    data = {
        "id": id
    }
    return render_template('view_user.html', dojo = Dojo.get_dojo_ninja(data))