from mysql.connector import Error
from src.entities.base_service import BaseService


class StrahovkiService(BaseService):
    def select(self) -> dict:
        query = "select * from strahovki"
        with self.connection.cursor() as cursor:
            cursor.execute(query)
            results = cursor.fetchall()
        return {
            "code": 200,
            "message": "OK",
            "results": [
                {
                    "id_strahovki": res[0],
                    "garage_num": res[1],
                    "avto_marka": res[2],
                    "gos_avto_num": res[3],
                    "num_strah_sved": res[4],
                    "data_vidachi": res[5],
                    "srok_strah": res[6],
                    "zastrah_po": res[7],
                    "note": res[8]
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
        query = f"insert into strahovki ({fields}) values ({str(values)[1:-1]});"
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

        query = f"update strahovki set {set_update} where id_strahovki={field_id}"
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
        query = f"delete from strahovki where id_strahovki={field_id}"
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
