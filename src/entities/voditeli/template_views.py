from flask import Blueprint, current_app as app, render_template, redirect, request

from src.entities.tools import exclude_keys, get_entry_data_and_id_form, TablesEnum
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
        data = VoditelSchema(**exclude_keys(form.data))
        app.config.voditeli_service.insert(data.__dict__)
        return redirect('/voditeli')
    return render_template('voditeli_add_form.html', title='Добавить водителя', form=form)


@voditeli_temp.route("/change", methods=["GET", "POST"])
def change_voditeli():
    entry_data, entry_id = get_entry_data_and_id_form(request, TablesEnum.VODITEL)
    form = VoditelAddForm(**entry_data)
    if form.validate_on_submit():
        data = VoditelSchema(**exclude_keys(form.data))
        app.config.voditeli_service.update(field_id=entry_id, body=data.__dict__)
        return redirect('/voditeli')
    return render_template('/voditeli_add_form.html', title='Изменить водителя', form=form)


@voditeli_temp.route('/<int:field_id>', methods=["GET"])
def delete_voditeli(field_id: int):
    app.config.voditeli_service.delete(field_id)
    return redirect('/voditeli')
