from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


class TehosmotrAddForm(FlaskForm):
    garage_num = StringField('Гаражный номер')
    data_prohojd_tehosmotra = StringField('Дата прохождения техосмотра')
    to_deistvitelen_do = StringField('ТО действителен до')
    razreshenie_na_dopusk = StringField('Разрешение на допуск')
    raznica = StringField('Разница (количество дней до конца ТО)')
    spisannie = StringField('Списанные')
    submit = SubmitField('Подтвердить')
