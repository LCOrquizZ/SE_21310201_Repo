class SistemaExpertoConCognicion:
    def __init__(self):
        # Base de conocimiento con ponderación de reglas
        # Cada regla tiene la forma (condiciones, conclusión, peso)
        self.base_conocimiento = []  # Lista de tuplas: (condiciones, conclusion, peso)
        self.base_hechos = []        # Lista de hechos conocidos
        self.inferencias_realizadas = []  # Conclusiones inferidas

    # Método para agregar una regla a la base de conocimiento
    def agregar_regla(self, condiciones, conclusion, peso_inicial=1.0):
        """Agrega una regla con un peso inicial a la base de conocimiento."""
        self.base_conocimiento.append((condiciones, conclusion, peso_inicial))
        print(f"Regla añadida: Si {condiciones} entonces '{conclusion}', peso: {peso_inicial}")

    # Método para agregar hechos a la base de hechos
    def agregar_hecho(self, hecho):
        """Agrega un hecho a la base de hechos."""
        if hecho not in self.base_hechos:
            self.base_hechos.append(hecho)
            print(f"Hecho añadido: {hecho}")

    # Motor de inferencia: encadenación hacia adelante con ponderación
    def inferir(self):
        """Realiza inferencias utilizando encadenación hacia adelante y ajuste cognitivo."""
        nueva_inferencia = True

        while nueva_inferencia:
            nueva_inferencia = False

            for condiciones, conclusion, peso in self.base_conocimiento:
                if all(condicion in self.base_hechos for condicion in condiciones):
                    if conclusion not in self.base_hechos:
                        # Realiza la inferencia basada en las condiciones de la regla
                        self.base_hechos.append(conclusion)
                        self.inferencias_realizadas.append((condiciones, conclusion, peso))
                        nueva_inferencia = True
                        print(f"Inferencia: Si {condiciones} entonces '{conclusion}' (Peso: {peso})")
    
    # Ajuste cognitivo de reglas basado en el feedback del usuario
    def ajustar_confianza(self):
        """Ajusta la confianza de las reglas basándose en el feedback del usuario."""
        for i, (condiciones, conclusion, peso) in enumerate(self.base_conocimiento):
            feedback = input(f"¿La conclusión '{conclusion}' derivada de la regla Si {condiciones} fue correcta? (s/n): ")
            if feedback.lower() == 's':
                # Incrementa el peso de la regla si fue correcta
                self.base_conocimiento[i] = (condiciones, conclusion, min(peso + 0.1, 1.0))
                print(f"Peso incrementado a {self.base_conocimiento[i][2]} para la regla: Si {condiciones} entonces '{conclusion}'")
            elif feedback.lower() == 'n':
                # Decrementa el peso de la regla si fue incorrecta
                self.base_conocimiento[i] = (condiciones, conclusion, max(peso - 0.1, 0.0))
                print(f"Peso decrementado a {self.base_conocimiento[i][2]} para la regla: Si {condiciones} entonces '{conclusion}'")

    # Método para mostrar los hechos
    def mostrar_hechos(self):
        """Muestra los hechos conocidos."""
        print("Hechos actuales en la base de hechos:")
        for hecho in self.base_hechos:
            print(f"- {hecho}")

    # Método para mostrar las inferencias realizadas
    def mostrar_inferencias(self):
        """Muestra las inferencias realizadas."""
        print("Inferencias realizadas:")
        for condiciones, conclusion, peso in self.inferencias_realizadas:
            print(f"Si {condiciones} entonces '{conclusion}' (Peso: {peso})")

# Función de interfaz de usuario
def interfaz_usuario():
    sistema_experto = SistemaExpertoConCognicion()

    while True:
        print("\n--- Sistema Experto con Cognición ---")
        print("1. Agregar regla")
        print("2. Agregar hecho")
        print("3. Realizar inferencias")
        print("4. Ajustar confianza de las reglas (cognición)")
        print("5. Mostrar hechos")
        print("6. Mostrar inferencias realizadas")
        print("7. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            condiciones = input("Introduce las condiciones de la regla (separadas por comas): ").split(",")
            condiciones = [condicion.strip() for condicion in condiciones]
            conclusion = input("Introduce la conclusión de la regla: ").strip()
            peso_inicial = float(input("Introduce el peso inicial de la regla (0.0 - 1.0): ").strip())
            sistema_experto.agregar_regla(condiciones, conclusion, peso_inicial)

        elif opcion == "2":
            hecho = input("Introduce un hecho: ").strip()
            sistema_experto.agregar_hecho(hecho)

        elif opcion == "3":
            print("\nRealizando inferencias...")
            sistema_experto.inferir()

        elif opcion == "4":
            print("\nAjustando confianza de las reglas basado en el feedback del usuario...")
            sistema_experto.ajustar_confianza()

        elif opcion == "5":
            print("\nHechos actuales:")
            sistema_experto.mostrar_hechos()

        elif opcion == "6":
            print("\nInferencias realizadas:")
            sistema_experto.mostrar_inferencias()

        elif opcion == "7":
            print("Saliendo del sistema experto.")
            break

        else:
            print("Opción no válida. Por favor, intenta de nuevo.")

# Ejecutar la interfaz de usuario
if __name__ == "__main__":
    interfaz_usuario()

