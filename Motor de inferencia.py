# Sistema experto con motor de inferencia (encadenación hacia adelante)

class SistemaExperto:
    def __init__(self):
        # Base de conocimiento (reglas) y base de hechos
        self.base_conocimiento = []  # Lista de reglas (tuplas)
        self.base_hechos = []        # Lista de hechos
        self.inferencias_realizadas = []  # Lista para registrar conclusiones inferidas

    # Método para agregar reglas a la base de conocimiento
    def agregar_regla(self, condiciones, conclusion):
        """Agrega una regla a la base de conocimiento."""
        self.base_conocimiento.append((condiciones, conclusion))
        print(f"Regla añadida: Si {condiciones} entonces '{conclusion}'")

    # Método para agregar hechos a la base de hechos
    def agregar_hecho(self, hecho):
        """Agrega un hecho a la base de hechos."""
        if hecho not in self.base_hechos:
            self.base_hechos.append(hecho)
            print(f"Hecho añadido: {hecho}")

    # Motor de inferencia: encadenación hacia adelante
    def inferir(self):
        """Realiza inferencias utilizando encadenación hacia adelante."""
        nueva_inferencia = True  # Controla si se han encontrado nuevas inferencias

        while nueva_inferencia:
            nueva_inferencia = False  # Inicialmente no hay nuevas inferencias

            for condiciones, conclusion in self.base_conocimiento:
                # Comprobamos si todas las condiciones de la regla están en la base de hechos
                if all(condicion in self.base_hechos for condicion in condiciones):
                    if conclusion not in self.base_hechos:
                        # Añadimos la conclusión a la base de hechos
                        self.base_hechos.append(conclusion)
                        self.inferencias_realizadas.append((condiciones, conclusion))
                        nueva_inferencia = True  # Indicamos que se ha hecho una nueva inferencia
                        print(f"Inferencia realizada: Si {condiciones} entonces '{conclusion}'")
    
    # Método para mostrar las inferencias realizadas
    def mostrar_inferencias(self):
        """Muestra las inferencias realizadas."""
        if not self.inferencias_realizadas:
            print("No se han realizado inferencias.")
        else:
            print("\nInferencias realizadas:")
            for condiciones, conclusion in self.inferencias_realizadas:
                print(f"Regla aplicada: Si {condiciones} entonces '{conclusion}'")
    
    # Método para mostrar los hechos conocidos
    def mostrar_hechos(self):
        """Muestra todos los hechos conocidos en la base de hechos."""
        if not self.base_hechos:
            print("No hay hechos en la base de hechos.")
        else:
            print("Hechos actuales en la base de hechos:")
            for hecho in self.base_hechos:
                print(f"- {hecho}")


# Ejemplo de uso

# Crear instancia del sistema experto
sistema_experto = SistemaExperto()

# Agregar reglas al sistema experto (base de conocimiento)
sistema_experto.agregar_regla(["el cielo está nublado"], "lleva un paraguas")
sistema_experto.agregar_regla(["tienes hambre"], "come algo")
sistema_experto.agregar_regla(["es de noche"], "enciende la luz")
sistema_experto.agregar_regla(["es de noche", "estás cansado"], "ve a dormir")

# Agregar hechos a la base de hechos
sistema_experto.agregar_hecho("el cielo está nublado")
sistema_experto.agregar_hecho("tienes hambre")
sistema_experto.agregar_hecho("es de noche")

# Mostrar hechos iniciales
print("\nHechos iniciales:")
sistema_experto.mostrar_hechos()

# Realizar inferencias
print("\nRealizando inferencias:")
sistema_experto.inferir()

# Mostrar inferencias realizadas
print("\nInferencias realizadas:")
sistema_experto.mostrar_inferencias()

# Mostrar hechos después de las inferencias
print("\nHechos después de las inferencias:")
sistema_experto.mostrar_hechos()
