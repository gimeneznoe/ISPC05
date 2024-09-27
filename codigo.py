
# Silvana

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

# Nombre del commit: Definicion de clases
# Descripcion del commit: Definimos las clases principales del programa.

# Nahir

    def select_normativas(self):
        cursor = self.connection.cursor()
        cursor.execute("""
            SELECT *
            FROM Normativa
        """)
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

# Nombre del commit: Seleccion
# Descripcion del commit: Definimos el menu principal de la seleccion de normativas

#Noe

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

# Nombre del commit: Insertar/Actualizar
# Descripcion del commit: Se insertan o actualizan las normativas existentes

#Agustin

    def delete_normativa(self, normativa_id):
        cursor = self.connection.cursor()
        cursor.execute("""
            DELETE FROM Normativa
            WHERE id_Normativa = ?
        """, (normativa_id,))
        self.connection.commit()
        print("\033[;32m"+"La normativa ha sido eliminada exitosamente.")

    def search_normativas(self):
        cursor = self.connection.cursor()
        selec = input(
            "Seleccione como buscar el registro de ley: a)Número de ley | b)Palabras claves: ")
        if selec == "a":
            numero_normativa = float(
                input("ingrese el numero de normativa a buscar: "))
            cursor.execute(f"""
                SELECT *
                FROM Normativa
                WHERE NroNormativa= {numero_normativa}
            """)

        else:
            palabras_clave = input(
                "Ingrese las palabras clave para buscar normativas: ")
            cursor.execute("""
                SELECT *
                FROM Normativa
                WHERE PalabrasClave LIKE ?
            """, ('%' + palabras_clave + '%',))

# Nombre del commit: Borrar/Consultar
# Descripcion del commit: Se borran o consultan las normativas existentes.

#Milton

        normativas_data = cursor.fetchall()

        if normativas_data:
            normativas = []
            for normativa_data in normativas_data:
                normativa = Normativa(*normativa_data)
                normativas.append(normativa)
            print("\033[;35m"+"="*80)
            print("Normativas encontradas:")
            for normativa in normativas:
                print("ID:", normativa.id_normativa)
                print("Tipo de Normativa:", normativa.tipo_normativa)
                print("Número de Normativa:", normativa.nro_normativa)
                print("Fecha:", normativa.fecha)
                print("Nombre:", normativa.nombre)
                print("Descripción:", normativa.descripcion)
                print("Categoría:", normativa.categoria)
                print("Jurisdicción:", normativa.jurisdiccion)
                print("Órgano Legislativo:", normativa.organo_legislativo)
                print("Palabras Clave:", normativa.palabras_clave)
                print("--" * 50)
        else:
            print("\033[;31m"+"No se encontraron normativas especificadas.")

    def run(self):
        self.open_connection()

        while True:
            print("\x1b[1;33m"+"\n=== GESTIÓN DE NORMATIVAS ===")
            print("OPCIONES DISPONIBLES:")
            print("1. Ver todas las normativas")
            print("2. Insertar una nueva normativa")
            print("3. Actualizar una normativa existente")
            print("4. Eliminar una normativa existente")
            print("5. Buscar normativas ")
            print("0. Salir")

# Nombre del commit: Reinsercion 
# Descripcion del commit: Se busca reinsertar las opciones, en el caso de que sean incorrectas

#Florencia

            opcion = input(
                "Ingrese el número de la opción deseada: "+"\33[0;m")

            if opcion == "1":
                self.select_normativas()
            elif opcion == "2":
                tipo_normativa = input("Ingrese el tipo de normativa: ")
                nro_normativa = input("Ingrese el número de normativa: ")
                fecha = input("Ingrese la fecha de la normativa: ")
                nombre = input("Ingrese el nombre de la normativa: ")
                descripcion = input(
                    "Ingrese la descripción de la normativa: ")
                categoria = input("Ingrese la categoría de la normativa: ")
                jurisdiccion = input(
                    "Ingrese la jurisdicción de la normativa: ")
                organo_legislativo = input(
                    "Ingrese el órgano legislativo de la normativa: ")
                palabras_clave = input(
                    "Ingrese las palabras clave de la normativa (separadas por comas): ")
                self.insert_normativa(tipo_normativa, nro_normativa, fecha, nombre,
                                      descripcion, categoria, jurisdiccion, organo_legislativo, palabras_clave)
                self.select_normativas()  # Mostrar las normativas después de insertar una nueva
            elif opcion == "3":
                normativa_id = input(
                    "Ingrese el ID de la normativa que desea actualizar: ")
                self.update_normativa(normativa_id)
                self.select_normativas()  # Mostrar las normativas después de actualizar una normativa
            elif opcion == "4":
                normativa_id = input(
                    "Ingrese el ID de la normativa que desea eliminar: ")
                self.delete_normativa(normativa_id)
                self.select_normativas()  # Mostrar las normativas después de eliminar una normativa
            elif opcion == "5":
                self.search_normativas()
            elif opcion == "0":
                break
            else:
                print("Opción inválida. Por favor, ingrese una opción válida.")

        self.close_connection()

# Crear una instancia de NormativaManager y ejecutar el programa
normativa_manager = NormativaManager("normativas")
normativa_manager.run()

# Nombre del commit: Comandos/Cargar
# Descripcion del commit: Se asignan los comandos (Por numeros), y se carga la base de datos con la que trabaja el programa.


