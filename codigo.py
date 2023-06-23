

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

