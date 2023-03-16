from dataclasses import dataclass


@dataclass
class StrahovkaSchema:
    garage_num: str = ""
    avto_marka: str = ""
    gos_avto_num: str = ""
    num_strah_sved: str = ""
    data_vidachi: str = ""
    srok_strah: str = ""
    zastrah_po: str = ""
    note: str = ""

