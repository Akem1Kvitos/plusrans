from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, IntegerField


class VoditelAddForm(FlaskForm):
    rabotaet_s = StringField('Работает с')
    fio = StringField('Фамилия Имя Отчество')
    a_k = StringField('а/к')
    data_rojd = StringField('Дата рождения')
    v_u_number = StringField('№ В/У')
    v_u_srok_dejstvia = StringField('Срок действия')
    v_u_category = StringField('Категории')
    med_s_number = StringField('№ Мед/с')
    med_s_srok_dejstvia = DateField('Срок действия')
    med_s_category = StringField('Категории')
    note = StringField('Прим.')
    d_category = StringField('Категория Д')
    phone_number = StringField('Телефон')
    med_leg = IntegerField('Мед. лег')
    blood = IntegerField('Кровь')
    gazelle = IntegerField('Газель')
    soc = IntegerField('Соц')
    scor = IntegerField('Скор')
    maz = IntegerField('Маз')
    bus = IntegerField('Автобус')
    razrjad = IntegerField('Разряд')
    v_class = IntegerField('Класс')
    submit = SubmitField('Подтвердить')
