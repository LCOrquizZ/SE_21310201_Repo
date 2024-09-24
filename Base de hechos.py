# Base de hechos en un sistema experto

class BaseDeHechos:
    def __init__(self):
        # La base de hechos es una lista que almacena hechos conocidos.
        self.hechos = []

    # Método para agregar un hecho a la base de hechos
    def agregar_hecho(self, hecho):
        """Agrega un hecho a la base de hechos si no está presente."""
        if hecho not in self.hechos:
            self.hechos.append(hecho)
            print(f"Hecho añadido: {hecho}")
        else:
            print(f"El hecho '{hecho}' ya existe en la base de hechos.")

    # Método para eliminar un hecho de la base de hechos
    def eliminar_hecho(self, hecho):
        """Elimina un hecho de la base de hechos si está presente."""
        if hecho in self.hechos:
            self.hechos.remove(hecho)
            print(f"Hecho eliminado: {hecho}")
        else:
            print(f"El hecho '{hecho}' no se encontró en la base de hechos.")

    # Método para comprobar si un hecho existe en la base de hechos
    def existe_hecho(self, hecho):
        """Comprueba si un hecho existe en la base de hechos."""
        return hecho in self.hechos

    # Mostrar todos los hechos en la base de hechos
    def mostrar_hechos(self):
        """Muestra todos los hechos conocidos."""
        if not self.hechos:
            print("La base de hechos está vacía.")
        else:
            print("Hechos conocidos en la base de hechos:")
            for hecho in self.hechos:
                print(f"- {hecho}")


# Ejemplo de uso

# Crear una instancia de la base de hechos
base_hechos = BaseDeHechos()

# Agregar hechos a la base de hechos
base_hechos.agregar_hecho("el cielo está nublado")
base_hechos.agregar_hecho("tienes hambre")

# Mostrar hechos actuales
print("\nHechos en la base de hechos:")
base_hechos.mostrar_hechos()

# Comprobar si un hecho existe
print("\nComprobando si el hecho 'tienes hambre' existe:")
existe = base_hechos.existe_hecho("tienes hambre")
print(f"'tienes hambre' existe: {existe}")

# Eliminar un hecho
print("\nEliminando el hecho 'tienes hambre':")
base_hechos.eliminar_hecho("tienes hambre")

# Mostrar hechos después de la eliminación
print("\nHechos después de la eliminación:")
base_hechos.mostrar_hechos()
