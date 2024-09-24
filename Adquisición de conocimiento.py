# Sistema experto basado en reglas

class SistemaExperto:
    def __init__(self):
        # Base de conocimiento inicial (vacía)
        self.base_conocimiento = []
    
    # Módulo de adquisición de conocimiento
    def adquirir_conocimiento(self, regla):
        """Adquiere nueva regla y la añade a la base de conocimiento."""
        self.base_conocimiento.append(regla)
        print(f"Regla añadida: {regla}")
    
    # Módulo de inferencia para aplicar reglas y resolver un problema
    def aplicar_reglas(self, hecho):
        """Aplica reglas sobre el hecho proporcionado."""
        for regla in self.base_conocimiento:
            condicion, conclusion = regla
            if hecho == condicion:
                return conclusion
        return "No se encontró ninguna regla aplicable."

    # Actualizar regla existente
    def actualizar_regla(self, indice, nueva_regla):
        """Actualiza una regla existente."""
        if 0 <= indice < len(self.base_conocimiento):
            self.base_conocimiento[indice] = nueva_regla
            print(f"Regla actualizada: {nueva_regla}")
        else:
            print("Índice de regla no válido.")
    
    # Mostrar todas las reglas actuales en la base de conocimiento
    def mostrar_reglas(self):
        """Muestra todas las reglas almacenadas en la base de conocimiento."""
        for i, regla in enumerate(self.base_conocimiento):
            print(f"{i}: Si {regla[0]} entonces {regla[1]}")


# Ejemplo de uso

# Crear instancia del sistema experto
sistema = SistemaExperto()

# Módulo de adquisición de conocimiento: añadir reglas
sistema.adquirir_conocimiento(("el cielo está nublado", "lleva un paraguas"))
sistema.adquirir_conocimiento(("tienes hambre", "come algo"))

# Mostrar reglas actuales
print("\nReglas en la base de conocimiento:")
sistema.mostrar_reglas()

# Aplicar reglas (inferencia) a un hecho
print("\nAplicando reglas:")
hecho = "el cielo está nublado"
resultado = sistema.aplicar_reglas(hecho)
print(f"Si {hecho}, entonces {resultado}")

# Actualizar una regla
print("\nActualizando regla:")
sistema.actualizar_regla(1, ("tienes hambre", "haz un sándwich"))

# Mostrar reglas después de la actualización
print("\nReglas después de la actualización:")
sistema.mostrar_reglas()

# Aplicar reglas con la regla actualizada
hecho = "tienes hambre"
resultado = sistema.aplicar_reglas(hecho)
print(f"Si {hecho}, entonces {resultado}")
