from mysql.connector import Error

from src.entities.base_service import BaseService


class VoditeliService(BaseService):
    def select(self) -> dict:
        query = "select * from voditeli"
        with self.connection.cursor() as cursor:
            cursor.execute(query)
            results = cursor.fetchall()
        return {
            "code": 200,
            "message": "OK",
            "results": [
                {
                    "iddrivers": res[0],
                    "rabotaet_s": res[1],
                    "fio": res[2],
                    "a_k": res[3],
                    "data_rojd": res[4],
                    "v_u_number": res[5],
                    "v_u_srok_dejstvia": res[6],
                    "v_u_category": res[7],
                    "med_s_number": res[8],
                    "med_s_srok_dejstvia": res[9],
                    "med_s_category": res[10],
                    "note": res[11],
                    "d_category": res[12],
                    "phone_number": res[13],
                    "med_leg": res[14],
                    "blood": res[15],
                    "gazelle": res[16],
                    "soc": res[17],
                    "scor": res[18],
                    "maz": res[19],
                    "bus": res[20],
                    "razrjad": res[21],
                    "class": res[22]
                } for res in results
            ]
        }

    def insert(self, body: dict) -> dict:
        keys = list(body.keys())
        field = ""
        for key in keys:
            field += f"{key}, "
        fields = field[0:-2]
        values = [body[key] for key in keys]
        query = f"insert into voditeli ({fields}) values ({str(values)[1:-1]});"
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query)
                self.connection.commit()
        except Error as e:
            raise Exception(e)
        return {
            "code": 200,
            "message": "OK"
        }

    def update(self, field_id: int, body: dict) -> dict:
        keys = list(body.keys())
        set_update = ""
        for key in keys:
            set_update += f"{key}='{body[key]}', "
        set_update = set_update[0:-2]

        query = f"update voditeli set {set_update} where iddrivers={field_id}"
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query)
                self.connection.commit()
        except Error as e:
            raise Exception(e)
        return {
            "code": 200,
            "message": "OK"
        }

    def delete(self, field_id: int) -> dict:
        query = f"delete from voditeli where iddrivers={field_id}"
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query)
                self.connection.commit()
        except Error as e:
            raise Exception(e)
        return {
            "code": 200,
            "message": "OK"
        }