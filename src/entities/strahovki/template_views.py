import ast

from flask import Blueprint, current_app as app, render_template, redirect, request

from src.entities.strahovki.forms import StrahAddForm
from src.entities.strahovki.schemas import StrahovkaSchema
from src.entities.tools import exclude_keys, TablesEnum, get_entry_data_and_id_form

strahovki_temp = Blueprint("strahovki", __name__, url_prefix="/strahovki")


@strahovki_temp.route("/", methods=["GET"])
def get_strahovki_template():
    result = app.config.strahovki_service.select()
    return render_template('strahovki.html', strahovki=result['results'])


@strahovki_temp.route("/add", methods=["GET", "POST"])
def add_strahovki_template():
    form = StrahAddForm()
    if form.validate_on_submit():
        data = StrahovkaSchema(**exclude_keys(form.data))
        app.config.strahovki_service.insert(data.__dict__)
        return redirect('/strahovki')
    return render_template('strahovki_add_form.html', title='Добавить страховку', form=form)


@strahovki_temp.route("/change", methods=["GET", "POST"])
def change_strahovka():
    entry_data, entry_id = get_entry_data_and_id_form(request, TablesEnum.STRAHOVKA)
    form = StrahAddForm(**entry_data)
    if form.validate_on_submit():
        data = StrahovkaSchema(**exclude_keys(form.data))
        app.config.strahovki_service.update(field_id=entry_id, body=data.__dict__)
        return redirect('/strahovki')
    return render_template('strahovki_add_form.html', title='Добавить страховку', form=form)


@strahovki_temp.route('/<int:field_id>', methods=["GET"])
def delete_strahovka(field_id: int):
    app.config.strahovki_service.delete(field_id)
    return redirect('/strahovki')