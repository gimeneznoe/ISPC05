
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

##Nombre de commit: Buscar Normativa
##Descripcion de commit: Mediante la busqueda de una palabra clave, y un numero de ley, se busca la normativa mediante la base de datos ya establecida.