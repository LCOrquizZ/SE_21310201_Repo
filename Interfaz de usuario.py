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

# Función para la interfaz de usuario
def interfaz_usuario():
    sistema_experto = SistemaExperto()

    while True:
        print("\n--- Sistema Experto ---")
        print("1. Agregar regla")
        print("2. Agregar hecho")
        print("3. Realizar inferencias")
        print("4. Mostrar hechos")
        print("5. Mostrar inferencias realizadas")
        print("6. Salir")
        
        opcion = input("Elige una opción: ")

        if opcion == "1":
            condiciones = input("Introduce las condiciones de la regla (separadas por comas): ").split(",")
            condiciones = [condicion.strip() for condicion in condiciones]  # Eliminar espacios en blanco
            conclusion = input("Introduce la conclusión de la regla: ").strip()
            sistema_experto.agregar_regla(condiciones, conclusion)

        elif opcion == "2":
            hecho = input("Introduce un hecho: ").strip()
            sistema_experto.agregar_hecho(hecho)

        elif opcion == "3":
            print("\nRealizando inferencias...")
            sistema_experto.inferir()

        elif opcion == "4":
            print("\nHechos actuales:")
            sistema_experto.mostrar_hechos()

        elif opcion == "5":
            print("\nInferencias realizadas:")
            sistema_experto.mostrar_inferencias()

        elif opcion == "6":
            print("Saliendo del sistema experto.")
            break

        else:
            print("Opción no válida. Por favor, intenta de nuevo.")

# Ejecutar la interfaz de usuario
if __name__ == "__main__":
    interfaz_usuario()
