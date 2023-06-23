    def delete_normativa(self, normativa_id):
        cursor = self.connection.cursor()
        cursor.execute("""
            DELETE FROM Normativa
            WHERE id_Normativa = ?
        """, (normativa_id,))
        self.connection.commit()
        print("\033[;32m"+"La normativa ha sido eliminada exitosamente.")

##Nombre de commit: Borrar Normativa
##Descripcion de commit: Esta funcion, busca eliminar la normativa desde la base de datos.