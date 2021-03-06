# -*- coding: utf-8 -*-
import sqlite3


class Database:
    def __init__(self):
        self.con = sqlite3.connect('Keys.db')
        self.cur = self.con.cursor()

    def execute(self, sql):
        self.cur.execute(sql)
        self.con.commit()

    def create_table_users(self):
        sql = """
        CREATE TABLE IF NOT EXISTS Keys (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
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

    def select_key_aes(self, user):
        sql = f"""select key_aes from Keys WHERE name='{user}'"""
        self.cur.execute(sql)
        return self.cur.fetchall()

    def insert_key_ceazar(self, key, user):
        sql = f"""
        update Keys set key_ceasar='{key}' WHERE name='{user}'
        """
        self.execute(sql)

    def select_key_ceazar(self, user):
        sql = f"""select key_ceasar from Keys WHERE name='{user}'"""
        self.cur.execute(sql)
        return self.cur.fetchall()

    def insert_key_rsa(self, key_open, key_privat, user):
        sql = f"""
                update Keys set key_rsa_open='{key_open}', key_rsa_privat='{key_privat}' WHERE name='{user}'
                """
        self.execute(sql)

    def select_key_rsa(self, user):
        sql = f"""select key_rsa_open, key_rsa_privat from Keys WHERE name='{user}'"""
        self.cur.execute(sql)
        return self.cur.fetchall()

    def delete_key_rsa(self, user):
        sql = f'''update Keys set key_rsa_open='', key_rsa_privat='' WHERE name='{user}'
        '''
        self.execute(sql)

    def insert_name(self, name):
        sql = f"""
                INSERT INTO Keys (name) VALUES('{str(name).replace("'", '')}')
                """
        self.execute(sql)

# pyinstaller --onefile --noconsole main.py encryption_algorithms/AES.py encryption_algorithms/caesar_cipher.py encryption_algorithms/RSA.py ui_designs/aes_dec_py.py ui_designs/aes_enc_py.py ui_designs/algoritm_encript_py.py ui_designs/caesar_py.py ui_designs/ceasar_dec_py.py ui_designs/rsa_dec_py.py ui_designs/rsa_enc_py.py ui_designs/untitled.py DB_API.py