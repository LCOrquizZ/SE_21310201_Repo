import random
import time

class SistemaExpertoConSensores:
    def __init__(self):
        self.base_conocimiento = []  # Lista de reglas: (condiciones, conclusion)
        self.base_hechos = []        # Lista de hechos
        self.inferencias_realizadas = []  # Lista de inferencias realizadas

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
        nueva_inferencia = True

        while nueva_inferencia:
            nueva_inferencia = False

            for condiciones, conclusion in self.base_conocimiento:
                if all(condicion in self.base_hechos for condicion in condiciones):
                    if conclusion not in self.base_hechos:
                        self.base_hechos.append(conclusion)
                        self.inferencias_realizadas.append((condiciones, conclusion))
                        nueva_inferencia = True
                        print(f"Inferencia: Si {condiciones} entonces '{conclusion}'")

    # Mostrar hechos en la base de hechos
    def mostrar_hechos(self):
        """Muestra todos los hechos actuales."""
        print("\nHechos actuales:")
        for hecho in self.base_hechos:
            print(f"- {hecho}")

    # Mostrar inferencias realizadas
    def mostrar_inferencias(self):
        """Muestra las inferencias realizadas."""
        if not self.inferencias_realizadas:
            print("No se han realizado inferencias.")
        else:
            print("\nInferencias realizadas:")
            for condiciones, conclusion in self.inferencias_realizadas:
                print(f"Si {condiciones} entonces '{conclusion}'")

# Simulaciones de sensores
def sensor_temperatura():
    """Simula la lectura de un sensor de temperatura (en grados Celsius)."""
    return round(random.uniform(15, 35), 2)

def sensor_humedad():
    """Simula la lectura de un sensor de humedad (en porcentaje)."""
    return round(random.uniform(30, 70), 2)

# Función para capturar datos de sensores y agregarlos a la base de hechos
def capturar_datos_de_sensores(sistema_experto):
    """Captura datos de sensores simulados y los agrega como hechos."""
    temperatura = sensor_temperatura()
    humedad = sensor_humedad()
    
    print(f"\nCapturando datos de sensores: Temperatura: {temperatura}°C, Humedad: {humedad}%")
    
    # Agregar hechos basados en las lecturas de los sensores
    if temperatura > 30:
        sistema_experto.agregar_hecho(f"Temperatura alta ({temperatura}°C)")
    elif temperatura < 18:
        sistema_experto.agregar_hecho(f"Temperatura baja ({temperatura}°C)")
    else:
        sistema_experto.agregar_hecho(f"Temperatura moderada ({temperatura}°C)")

    if humedad > 60:
        sistema_experto.agregar_hecho(f"Humedad alta ({humedad}%)")
    elif humedad < 40:
        sistema_experto.agregar_hecho(f"Humedad baja ({humedad}%)")
    else:
        sistema_experto.agregar_hecho(f"Humedad moderada ({humedad}%)")

# Interfaz de usuario
def interfaz_usuario():
    sistema_experto = SistemaExpertoConSensores()

    # Agregar reglas al sistema experto
    sistema_experto.agregar_regla(["Temperatura alta (más de 30°C)", "Humedad alta (más de 60%)"], "Encender aire acondicionado")
    sistema_experto.agregar_regla(["Temperatura baja (menos de 18°C)"], "Encender calefacción")
    sistema_experto.agregar_regla(["Temperatura moderada", "Humedad moderada"], "Ambiente confortable")

    while True:
        print("\n--- Sistema Experto con Sensores ---")
        print("1. Capturar datos de sensores")
        print("2. Realizar inferencias")
        print("3. Mostrar hechos")
        print("4. Mostrar inferencias realizadas")
        print("5. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            print("\nCapturando datos de sensores...")
            capturar_datos_de_sensores(sistema_experto)

        elif opcion == "2":
            print("\nRealizando inferencias...")
            sistema_experto.inferir()

        elif opcion == "3":
            sistema_experto.mostrar_hechos()

        elif opcion == "4":
            sistema_experto.mostrar_inferencias()

        elif opcion == "5":
            print("Saliendo del sistema experto.")
            break

        else:
            print("Opción no válida. Por favor, intenta de nuevo.")

# Ejecutar la interfaz de usuario
if __name__ == "__main__":
    interfaz_usuario()
