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
