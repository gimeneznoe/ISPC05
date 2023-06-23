    def insert_normativa(self, tipo_normativa, nro_normativa, fecha, nombre, descripcion, categoria, jurisdiccion, organo_legislativo, palabras_clave):
        cursor = self.connection.cursor()
        cursor.execute("""
            INSERT INTO Normativa (TipoNormativa, NroNormativa, Fecha, Nombre, Descripcion, Categoria, Jurisdiccion, OrganoLegislativo, PalabrasClave)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (tipo_normativa, nro_normativa, fecha, nombre, descripcion, categoria, jurisdiccion, organo_legislativo, palabras_clave))
        self.connection.commit()
        print("\033[;32m"+"La normativa ha sido insertada exitosamente.")

##Nombre del commit: Insertar
##Descripcion del commit: En esta funcion, se buscan insertar las normativas.