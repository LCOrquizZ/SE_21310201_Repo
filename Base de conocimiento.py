# Base de conocimiento en un sistema experto

class BaseDeConocimiento:
    def __init__(self):
        # La base de conocimiento es un diccionario donde las claves son condiciones (hechos)
        # y los valores son las conclusiones (acciones).
        self.conocimiento = {}

    # Método para agregar reglas a la base de conocimiento
    def agregar_regla(self, hecho, conclusion):
        """Agrega una nueva regla (hecho -> conclusión) a la base de conocimiento."""
        self.conocimiento[hecho] = conclusion
        print(f"Regla añadida: Si '{hecho}' entonces '{conclusion}'")

    # Método para obtener la conclusión correspondiente a un hecho
    def obtener_conclusion(self, hecho):
        """Dado un hecho, devuelve la conclusión si existe."""
        return self.conocimiento.get(hecho, "No se encontró ninguna conclusión para este hecho.")

    # Método para mostrar todas las reglas en la base de conocimiento
    def mostrar_conocimiento(self):
        """Muestra todas las reglas de la base de conocimiento."""
        if not self.conocimiento:
            print("La base de conocimiento está vacía.")
        else:
            for hecho, conclusion in self.conocimiento.items():
                print(f"Si '{hecho}' entonces '{conclusion}'")

    # Método para actualizar una regla existente en la base de conocimiento
    def actualizar_regla(self, hecho, nueva_conclusion):
        """Actualiza la conclusión de un hecho en la base de conocimiento."""
        if hecho in self.conocimiento:
            self.conocimiento[hecho] = nueva_conclusion
            print(f"Regla actualizada: Si '{hecho}' entonces '{nueva_conclusion}'")
        else:
            print(f"No existe ninguna regla para el hecho: '{hecho}'")

    # Método para eliminar una regla de la base de conocimiento
    def eliminar_regla(self, hecho):
        """Elimina una regla de la base de conocimiento."""
        if hecho in self.conocimiento:
            del self.conocimiento[hecho]
            print(f"Regla eliminada: '{hecho}'")
        else:
            print(f"No existe ninguna regla para el hecho: '{hecho}'")


# Ejemplo de uso

# Crear una instancia de la base de conocimiento
base_conocimiento = BaseDeConocimiento()

# Agregar reglas a la base de conocimiento
base_conocimiento.agregar_regla("el cielo está nublado", "lleva un paraguas")
base_conocimiento.agregar_regla("tienes hambre", "come algo")
base_conocimiento.agregar_regla("es de noche", "enciende la luz")

# Mostrar todas las reglas actuales en la base de conocimiento
print("\nReglas en la base de conocimiento:")
base_conocimiento.mostrar_conocimiento()

# Consultar una conclusión dado un hecho
print("\nConsultando la conclusión de un hecho:")
hecho = "tienes hambre"
conclusion = base_conocimiento.obtener_conclusion(hecho)
print(f"Si '{hecho}' entonces '{conclusion}'")

# Actualizar una regla existente
print("\nActualizando una regla existente:")
base_conocimiento.actualizar_regla("es de noche", "ve a dormir")

# Mostrar reglas actualizadas
print("\nReglas después de la actualización:")
base_conocimiento.mostrar_conocimiento()

# Eliminar una regla de la base de conocimiento
print("\nEliminando una regla:")
base_conocimiento.eliminar_regla("tienes hambre")

# Mostrar reglas después de la eliminación
print("\nReglas después de la eliminación:")
base_conocimiento.mostrar_conocimiento()
