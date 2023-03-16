from dataclasses import dataclass


@dataclass
class TehosmotrSchema:
    garage_num: str = ""
    data_prohojd_tehosmotra: str = ""
    to_deistvitelen_do: str = ""
    razreshenie_na_dopusk: str = ""
    raznica: str = ""
    spisannie: str = ""
    submit: str = ""

