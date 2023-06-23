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