from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField


class VoditelAddForm(FlaskForm):
    rabotaet_s = StringField('Работает с')
    fio = StringField('Фамилия Имя Отчество')
    a_k = StringField('а/к')
    data_rojd = StringField('Дата рождения')
    v_u_number = StringField('№ В/У')
    v_u_srok_dejstvia = StringField('Срок действия')
    v_u_category = StringField('Категории')
    med_s_number = StringField('№ Мед/с')
    med_s_srok_dejstvia = StringField('Срок действия')
    med_s_category = StringField('Категории')
    note = StringField('Прим.')
    d_category = StringField('Категория Д')
    phone_number = StringField('Телефон')
    med_leg = SelectField('Мед. лег', choices=['+', "-"])
    blood = StringField('Кровь')
    gazelle = SelectField('Газель', choices=['+', "-"])
    soc = SelectField('Соц', choices=['+', "-"])
    scor = SelectField('Скор', choices=['+', "-"])
    maz = SelectField('Маз', choices=['+', "-"])
    bus = SelectField('Автобус', choices=['+', "-"])
    razrjad = StringField('Разряд')
    klass = StringField('Класс')
    submit = SubmitField('Подтвердить')
