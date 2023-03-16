from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


class StrahAddForm(FlaskForm):
    garage_num = StringField('Гаражный номер')
    avto_marka = StringField('Марка А/м')
    gos_avto_num = StringField('Гос № а/м')
    num_strah_sved = StringField('№ Страхов. Свидет')
    data_vidachi = StringField('Дата выдачи')
    srok_strah = StringField('Срок страх.')
    zastrah_po = StringField('Застрах. По')
    note = StringField('Примечание')
    submit = SubmitField('Подтвердить')
