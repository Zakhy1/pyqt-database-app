import sqlite3
from typing import Optional, List
import pandas as pd


class DataBaseAdapter:
    def __init__(self, db: str):
        self.db = db

    def check_unique(self, table_name: str, name: str, col_name: Optional[str] = None) -> bool:
        try:
            con = sqlite3.connect(self.db)
            cursor = con.cursor()
            if col_name:
                cursor.execute(f"SELECT id FROM {table_name} WHERE {col_name} = '{name}' ")
            else:
                cursor.execute(f"SELECT id FROM {table_name} WHERE name = '{name}' ")
            data = cursor.fetchone()

            cursor.close()
            con.close()

            if data:
                return False
            return True

        except sqlite3.Error as error:
            print(error)

    def check_exist(self, table_name: str, pk: int) -> bool:
        try:
            con = sqlite3.connect(self.db)
            cursor = con.cursor()
            cursor.execute(f"SELECT id FROM {table_name} WHERE id = {pk}")

            data = cursor.fetchone()

            cursor.close()
            con.close()

            if data:
                return True
            return False

        except sqlite3.Error as error:
            print(error)

    def insert(self, table_name: str, form_data: List) -> None:
        try:
            con = sqlite3.connect(self.db)
            cursor = con.cursor()
            if len(form_data) > 1:
                cols = ""
                vals = ""
                for i in range(len(form_data)):
                    if i == len(form_data) - 1:
                        vals += f"'{form_data[i][1]}'"
                        cols += f"{form_data[i][0]}"
                    else:
                        cols += f"{form_data[i][0]},"
                        vals += f"'{form_data[i][1]}',"

                cursor.execute(f"INSERT INTO {table_name}({cols}) VALUES({vals})")
            else:
                cursor.execute(f"INSERT INTO {table_name}({form_data[0][0]}) VALUES('{form_data[0][1]}')")

            con.commit()
            cursor.close()

        except sqlite3.Error as error:
            print(error)

    def delete(self, table_name: str, pk: int) -> None:
        try:
            con = sqlite3.connect(self.db)
            cursor = con.cursor()

            cursor.execute(f"DELETE FROM {table_name} WHERE id = {pk}")

            con.commit()
            cursor.close()
        except sqlite3.Error as error:
            print(error)

    # def update(self, table_name: str, pk: int, *form_data) -> None: впадлу
    #     pass

    def extract(self, table_name: str) -> None:
        try:
            con = sqlite3.connect(self.db)

            query = f"SELECT * FROM {table_name}"
            df = pd.read_sql(query, con)
            df.to_excel(f"{table_name}.xlsx")

            con.close()
        except sqlite3.Error as error:
            print(error)

    def get_names(self, table_name: str) -> List[str]:
        try:
            con = sqlite3.connect(self.db)
            cursor = con.cursor()
            cursor.execute(f"""SELECT name FROM {table_name}""")
            res = []
            for i in cursor.fetchall():
                res.append(i[0])
            return res
        except sqlite3.Error as error:
            print(error)

    def auth(self):
        pass

    def register(self):
        pass
