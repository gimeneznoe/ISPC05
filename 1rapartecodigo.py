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

##Nombre de commit: Mostrador
##Descripcion de commit: En caso de que la condicion sea real, se vuelve al menu de muestreo.