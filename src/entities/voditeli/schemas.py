from dataclasses import dataclass
from datetime import time


@dataclass
class VoditelSchema:
    med_leg: int
    blood: int
    soc: int
    scor: int
    maz: int
    razrjad: int
    v_class: int
    bus: int
    gazelle: int
    rabotaet_s: str = ""
    fio: str = ""
    a_k: str = ""
    data_rojd: str = ""
    v_u_number: str = ""
    v_u_srok_dejstvia: str = ""
    v_u_category: str = ""
    med_s_number: str = ""
    med_s_srok_dejstvia: str = ""
    med_s_category: str = ""
    note: str = ""
    d_category: str = ""
    phone_number: str = ""

    # поле в бд названо зарезервированным словом в python "class"пришлось переименовать в форме
    def reshape_voditel_data(self):
        res = self.__dict__
        if "v_class" in res.keys():
            res['class'] = res.pop('v_class')
        if 'med_s_srok_dejstvia' in res.keys():
            res['med_s_srok_dejstvia'] = res['med_s_srok_dejstvia'].strftime('%Y-%m-%d')
        return res