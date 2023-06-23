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