# -*- coding: utf-8 -*-
import sqlite3


class Database:
    def __init__(self):
        self.con = sqlite3.connect('rest.db')
        self.cur = self.con.cursor()

    def execute(self, sql):
        self.cur.execute(sql)
        self.con.commit()

    def create_table_users(self):
        sql = """
        CREATE TABLE IF NOT EXISTS Keys (
        id SERIAL PRIMARY KEY,
        name TEXT NOT NULL UNIQUE,
        key_rsa_open TEXT NULL,
        key_rsa_privat TEXT NULL,
        key_ceasar TEXT NULL,
        key_aes TEXT NULL
        );
        """
        self.execute(sql)

    def insert_key_aes(self, key, user):
        sql = f"""
        update Keys set key_aes='{key}' WHERE name='{user}'
        """
        self.execute(sql)

    def insert_key_rsa(self, key_open, key_privat, user):
        sql = f"""
                update Keys set key_rsa_open='{str(key_open)}', key_rsa_privat='{str(key_privat)}' WHERE name='{user}'
                """
        self.execute(sql)



    def select_key_aes(self, user):
        sql = f"""select key_aes from Keys WHERE name='{user}'"""
        self.cur.execute(sql)
        return self.cur.fetchall()

    def insert_name(self, name):
        sql = f"""
                INSERT INTO Keys (name) VALUES('{str(name).replace("'", '')}')
                """
        self.execute(sql)

# db = Database()
# db.create_table_users()
# db.insert_name('asdasd')
# con = psycopg2.connect(
#             database="postgres",
#             user="postgres",
#             password="24651asd",
#             host="localhost",
#             port="5432"
#         )
# cur = con.cursor()
# print(cur.execute('select key_aes from Keys'))
# records = cur.fetchall()
# print(records)
# ex = Database()
# print(ex.s('a'))
# ex.insert_key_rsa('sdfsfsdfsdf', '24324234', 'xxx')
