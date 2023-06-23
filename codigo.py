

# Nombre del commit: Seleccion
# Descripcion del commit: Definimos el menu principal de la seleccion de normativas

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
          

