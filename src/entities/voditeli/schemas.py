from dataclasses import dataclass
from datetime import time


@dataclass
class VoditelSchema:
    med_leg: str = ""
    blood: str = ""
    soc: str = ""
    scor: str = ""
    maz: str = ""
    razrjad: str = ""
    klass: str = ""
    bus: str = ""
    gazelle: str = ""
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
