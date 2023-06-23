import sqlite3


class Normativa:
    def __init__(self, id_normativa, tipo_normativa, nro_normativa, fecha, nombre, descripcion, categoria, jurisdiccion, organo_legislativo, palabras_clave):
        self.id_normativa = id_normativa
        self.tipo_normativa = tipo_normativa
        self.nro_normativa = nro_normativa
        self.fecha = fecha
        self.nombre = nombre
        self.descripcion = descripcion
        self.categoria = categoria
        self.jurisdiccion = jurisdiccion
        self.organo_legislativo = organo_legislativo
        self.palabras_clave = palabras_clave

class NormativaManager:
    def __init__(self, db_file):
        self.db_file = db_file
        self.connection = None

    def open_connection(self):
        self.connection = sqlite3.connect(self.db_file)

    def close_connection(self):
        if self.connection:
            self.connection.close()

