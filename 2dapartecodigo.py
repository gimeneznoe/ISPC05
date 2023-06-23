
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
            
