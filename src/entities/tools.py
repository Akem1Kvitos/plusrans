import ast
from enum import Enum
from flask import Request


class TablesEnum(Enum):
    STRAHOVKA = "STRAHOVKA"
    VODITEL = "VODITEL"
    TEHOSMOTR = "TEHOSMOTR"


def exclude_keys(data: dict):
    if 'submit' and 'csrf_token' in data.keys():
        data.pop('submit')
        data.pop('csrf_token')
    return data


def get_entry_data_and_id_form(request: Request, table: TablesEnum):
    data_dict = ast.literal_eval(request.args.to_dict()['entry'])
    entry_id = None

    if table == TablesEnum.STRAHOVKA:
        entry_id = data_dict['id_strahovki']

    elif table == TablesEnum.VODITEL:
        entry_id = data_dict['iddrivers']

    elif table == TablesEnum.TEHOSMOTR:
        entry_id = data_dict['id_teh_osmotri']

    return data_dict, entry_id
