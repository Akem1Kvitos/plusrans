from mysql.connector import Error

from src.entities.base_service import BaseService


class TehosmotriService(BaseService):
    def select(self) -> dict:
        query = "select * from teh_osmotri"
        with self.connection.cursor() as cursor:
            cursor.execute(query)
            results = cursor.fetchall()
        return {
            "code": 200,
            "message": "OK",
            "results": [
                {
                    "id_teh_osmotri": res[0],
                    "garage_num": res[1],
                    "data_prohojd_tehosmotra": res[2],
                    "to_deistvitelen_do": res[3],
                    "razreshenie_na_dopusk": res[4],
                    "raznica": res[5],
                    "spisannie": res[6]
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
        query = f"insert into teh_osmotri ({fields}) values ({str(values)[1:-1]});"
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

        query = f"update teh_osmotri set {set_update} where id_teh_osmotri={field_id}"
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
        query = f"delete from teh_osmotri where id_teh_osmotri={field_id}"
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