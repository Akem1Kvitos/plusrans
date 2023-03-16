from flask import Blueprint, current_app as app, render_template, redirect

from src.entities.tools import exclude_keys
from src.entities.voditeli.forms import VoditelAddForm
from src.entities.voditeli.schemas import VoditelSchema

voditeli_temp = Blueprint("voditeli", __name__, url_prefix="/voditeli")


@voditeli_temp.route("/", methods=["GET"])
def get_voditeli_template():
    result = app.config.voditeli_service.select()
    return render_template('voditely.html', voditeli=result['results'])


@voditeli_temp.route("/add", methods=["GET", "POST"])
def add_voditeli_template():
    form = VoditelAddForm()
    if form.validate_on_submit():
        data = VoditelSchema(**exclude_keys(form.data)).reshape_voditel_data()
        app.config.voditeli_service.insert(data)
        return redirect('/voditeli')
    return render_template('voditeli_add_form.html', title='Добавить водителя', form=form)
