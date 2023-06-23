##Aca empieza el de silvana

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
   # Aca empieza el de nahir
    def select_normativas(self):

        cursor = self.connection.cursor()
        cursor.execute("""SELECT * FROM Normativa """)
        normativas_data = cursor.fetchall()

        if normativas_data:
            normativas = []
            for normativa_data in normativas_data:
                normativa = Normativa(*normativa_data)
                normativas.append(normativa)
            print("\033[;36m"+"="*110)
            print("Normativas: ")
            print("")
            for normativa in normativas:
                print("ID: ", normativa.id_normativa)
                print("Tipo de Normativa: ", normativa.tipo_normativa)
                print("Número de Normativa: ", normativa.nro_normativa)
                print("Fecha: ", normativa.fecha)
                print("Nombre: ", normativa.nombre)
                print("Descripción: ", normativa.descripcion)
                print("Categoría: ", normativa.categoria)
                print("Jurisdicción: ", normativa.jurisdiccion)
                print("Órgano Legislativo: ", normativa.organo_legislativo)
                print("Palabras Clave: ", normativa.palabras_clave)
                print("-"*110)
        else:
            print("\033[;31m"+"No hay normativas registradas.")
## Aca empieza lo de noe
    def insert_normativa(self, tipo_normativa, nro_normativa, fecha, nombre, descripcion, categoria, jurisdiccion, organo_legislativo, palabras_clave):
        cursor = self.connection.cursor()
        cursor.execute("""
            INSERT INTO Normativa (TipoNormativa, NroNormativa, Fecha, Nombre, Descripcion, Categoria, Jurisdiccion, OrganoLegislativo, PalabrasClave)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (tipo_normativa, nro_normativa, fecha, nombre, descripcion, categoria, jurisdiccion, organo_legislativo, palabras_clave))
        self.connection.commit()
        print("\033[;32m"+"La normativa ha sido insertada exitosamente.")


    def update_normativa(self, normativa_id):
       cursor = self.connection.cursor()
        cursor.execute("""
            SELECT *
            FROM Normativa
            WHERE id_Normativa = ?
        """, (normativa_id,))
        normativa_data = cursor.fetchone()

        if normativa_data:
            Normativa(*normativa_data)
            tipo_normativa = input("Ingrese el nuevo tipo de normativa: ")
            nro_normativa = input("Ingrese el nuevo número de normativa: ")
            fecha = input("Ingrese la nueva fecha de la normativa: ")
            nombre = input("Ingrese el nuevo nombre de la normativa: ")
            descripcion = input(
                "Ingrese la nueva descripción de la normativa: ")
            categoria = input("Ingrese la nueva categoría de la normativa: ")
            jurisdiccion = input(
                "Ingrese la nueva jurisdicción de la normativa: ")
            organo_legislativo = input(
                "Ingrese el nuevo órgano legislativo de la normativa: ")
            palabras_clave = input(
                "Ingrese las nuevas palabras clave de la normativa (separadas por comas): ")

            cursor.execute("""
                UPDATE Normativa
                SET TipoNormativa = ?, NroNormativa = ?, Fecha = ?, Nombre = ?, Descripcion = ?, Categoria = ?, Jurisdiccion = ?, OrganoLegislativo = ?, PalabrasClave = ?
                WHERE id_Normativa = ?
            """, (tipo_normativa, nro_normativa, fecha, nombre, descripcion, categoria, jurisdiccion, organo_legislativo, palabras_clave, normativa_id))
            self.connection.commit()
            print("\033[;32m"+"La normativa ha sido actualizada exitosamente.")
        else:
            print("\033[;31m" +
                  "No se encontró la normativa con el ID especificado.")
