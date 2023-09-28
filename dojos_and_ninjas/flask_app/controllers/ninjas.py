from flask import render_template, redirect, request
from flask_app import app
from flask_app.models import dojo, ninja

@app.route('/ninja')
def ninjas():
    return render_template('create_ninja.html', dojos = dojo.Dojo.all_dojos())

@app.route('/add/ninja', methods=['POST'])
def add_ninja():
    ninja.Ninja.save_ninja(request.form)
    return redirect('/ninja')

@app.route('/edit/ninja/<int:id>')
def edit_ninja(id):
    data = {
        "id": id
    }
    return render_template("edit_ninja.html", ninja = ninja.Ninja.get_one_db(data))

@app.route('/update/ninja', methods=['POST'])
def update_ninja():
    ninja.Ninja.edit_ninja(request.form)
    return redirect('/dojos/{{int:id}}')

@app.route('/delete/ninja/<int:id>')
def remove_ninja(id):
    data = {
        "id": id
    }
    ninja.Ninja.delete_ninja(data)
    return redirect('/dojos/<int:id>')