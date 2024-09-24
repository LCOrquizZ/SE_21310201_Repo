# Sistema experto con módulo de explicaciones

class SistemaExpertoConExplicaciones:
    def __init__(self):
        # Base de conocimiento (reglas) y base de hechos
        self.base_conocimiento = []
        self.base_hechos = []
        self.explicaciones = []  # Almacena las reglas y hechos utilizados en la inferencia

    # Método para agregar reglas a la base de conocimiento
    def agregar_regla(self, condicion, conclusion):
        """Agrega una regla a la base de conocimiento."""
        self.base_conocimiento.append((condicion, conclusion))
        print(f"Regla añadida: Si '{condicion}' entonces '{conclusion}'")

    # Método para agregar hechos a la base de hechos
    def agregar_hecho(self, hecho):
        """Agrega un hecho a la base de hechos."""
        if hecho not in self.base_hechos:
            self.base_hechos.append(hecho)
            print(f"Hecho añadido: {hecho}")

    # Módulo de inferencia que aplica reglas y almacena explicaciones
    def inferir(self):
        """Realiza inferencias basadas en los hechos conocidos y las reglas."""
        self.explicaciones.clear()  # Limpiamos las explicaciones anteriores
        for regla in self.base_conocimiento:
            condicion, conclusion = regla
            if condicion in self.base_hechos:
                self.base_hechos.append(conclusion)
                self.explicaciones.append((condicion, conclusion))
                print(f"Inferencia: Si '{condicion}', entonces '{conclusion}'")

    # Módulo de explicaciones que muestra cómo se llegó a una conclusión
    def explicar(self):
        """Explica cómo se llegó a las conclusiones actuales."""
        if not self.explicaciones:
            print("No hay inferencias realizadas todavía.")
        else:
            print("\nExplicaciones de cómo se llegó a las conclusiones:")
            for condicion, conclusion in self.explicaciones:
                print(f"Se aplicó la regla: Si '{condicion}', entonces '{conclusion}'")

    # Método para mostrar todos los hechos actuales
    def mostrar_hechos(self):
        """Muestra todos los hechos conocidos en la base de hechos."""
        if not self.base_hechos:
            print("No hay hechos en la base de hechos.")
        else:
            print("Hechos actuales en la base de hechos:")
            for hecho in self.base_hechos:
                print(f"- {hecho}")


# Ejemplo de uso

# Crear instancia del sistema experto con módulo de explicaciones
sistema_experto = SistemaExpertoConExplicaciones()

# Agregar reglas al sistema experto (base de conocimiento)
sistema_experto.agregar_regla("el cielo está nublado", "lleva un paraguas")
sistema_experto.agregar_regla("tienes hambre", "come algo")
sistema_experto.agregar_regla("es de noche", "enciende la luz")
sistema_experto.agregar_regla("estás cansado", "ve a dormir")

# Agregar hechos a la base de hechos
sistema_experto.agregar_hecho("el cielo está nublado")
sistema_experto.agregar_hecho("tienes hambre")

# Mostrar hechos actuales
print("\nHechos actuales:")
sistema_experto.mostrar_hechos()

# Realizar inferencias
print("\nRealizando inferencias:")
sistema_experto.inferir()

# Explicar las conclusiones alcanzadas
print("\nExplicaciones:")
sistema_experto.explicar()

# Mostrar los hechos después de las inferencias
print("\nHechos después de las inferencias:")
sistema_experto.mostrar_hechos()
