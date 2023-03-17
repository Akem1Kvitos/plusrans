from flask import Blueprint, current_app as app, render_template, redirect, request

from src.entities.tehosmotri.forms import TehosmotrAddForm
from src.entities.tehosmotri.schemas import TehosmotrSchema
from src.entities.tools import exclude_keys, get_entry_data_and_id_form, TablesEnum

tehosmotri_temp = Blueprint("tehosmotri", __name__, url_prefix="/tehosmotri")


@tehosmotri_temp.route("/", methods=["GET"])
def get_tehosmotri_template():
    result = app.config.tehosmotri_service.select()
    return render_template('tehosmotri.html', tehosmotri=result['results'])


@tehosmotri_temp.route("/add", methods=["GET", "POST"])
def add_tehosmotri_template():
    form = TehosmotrAddForm()
    if form.validate_on_submit():
        data = TehosmotrSchema(**exclude_keys(form.data))
        app.config.tehosmotri_service.insert(data.__dict__)
        return redirect('/tehosmotri')
    return render_template('tehosmotri_add_form.html', title='Добавить техосмотр', form=form)


@tehosmotri_temp.route("/change", methods=["GET", "POST"])
def change_tehosmotri():
    entry_data, entry_id = get_entry_data_and_id_form(request, TablesEnum.TEHOSMOTR)
    form = TehosmotrAddForm(**entry_data)
    if form.validate_on_submit():
        data = TehosmotrSchema(**exclude_keys(form.data))
        app.config.tehosmotri_service.update(field_id=entry_id, body=data.__dict__)
        return redirect('/tehosmotri')
    return render_template('tehosmotri_add_form.html', title='Изменить техосмотр', form=form)


@tehosmotri_temp.route('/<int:field_id>', methods=["GET"])
def delete_tehosmotri(field_id: int):
    app.config.tehosmotri_service.delete(field_id)
    return redirect('/tehosmotri')
