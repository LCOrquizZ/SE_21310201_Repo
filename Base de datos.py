import sqlite3

class SistemaExpertoConBaseDeDatos:
    def __init__(self, db_name="sistema_experto.db"):
        self.db_name = db_name
        self.conexion = sqlite3.connect(self.db_name)
        self.cursor = self.conexion.cursor()
        self.crear_tablas()
    
    def crear_tablas(self):
        """Crea las tablas necesarias en la base de datos."""
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS reglas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            condiciones TEXT NOT NULL,
            conclusion TEXT NOT NULL
        )
        ''')
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS hechos (
            hecho TEXT PRIMARY KEY
        )
        ''')
        self.conexion.commit()

    def agregar_regla(self, condiciones, conclusion):
        """Agrega una regla a la base de datos."""
        self.cursor.execute('''
        INSERT INTO reglas (condiciones, conclusion)
        VALUES (?, ?)
        ''', (condiciones, conclusion))
        self.conexion.commit()
        print(f"Regla añadida: Si {condiciones} entonces '{conclusion}'")

    def agregar_hecho(self, hecho):
        """Agrega un hecho a la base de datos."""
        self.cursor.execute('''
        INSERT OR IGNORE INTO hechos (hecho)
        VALUES (?)
        ''', (hecho,))
        self.conexion.commit()
        print(f"Hecho añadido: {hecho}")

    def obtener_reglas(self):
        """Obtiene todas las reglas de la base de datos."""
        self.cursor.execute('SELECT condiciones, conclusion FROM reglas')
        return self.cursor.fetchall()

    def obtener_hechos(self):
        """Obtiene todos los hechos de la base de datos."""
        self.cursor.execute('SELECT hecho FROM hechos')
        return [hecho[0] for hecho in self.cursor.fetchall()]

    def inferir(self):
        """Realiza inferencias utilizando encadenación hacia adelante."""
        hechos = self.obtener_hechos()
        reglas = self.obtener_reglas()
        inferencias_realizadas = []

        nueva_inferencia = True

        while nueva_inferencia:
            nueva_inferencia = False

            for condiciones, conclusion in reglas:
                condiciones_list = condiciones.split(", ")
                if all(condicion in hechos for condicion in condiciones_list):
                    if conclusion not in hechos:
                        self.agregar_hecho(conclusion)
                        inferencias_realizadas.append((condiciones, conclusion))
                        nueva_inferencia = True
                        print(f"Inferencia: Si {condiciones} entonces '{conclusion}'")
        
        return inferencias_realizadas

    def mostrar_hechos(self):
        """Muestra todos los hechos actuales en la base de datos."""
        hechos = self.obtener_hechos()
        print("\nHechos actuales:")
        for hecho in hechos:
            print(f"- {hecho}")

    def mostrar_inferencias(self, inferencias_realizadas):
        """Muestra las inferencias realizadas."""
        if not inferencias_realizadas:
            print("No se han realizado inferencias.")
        else:
            print("\nInferencias realizadas:")
            for condiciones, conclusion in inferencias_realizadas:
                print(f"Si {condiciones} entonces '{conclusion}'")

    def cerrar(self):
        """Cierra la conexión a la base de datos."""
        self.conexion.close()

# Interfaz de usuario
def interfaz_usuario():
    sistema_experto = SistemaExpertoConBaseDeDatos()

    # Agregar reglas al sistema experto
    sistema_experto.agregar_regla("Temperatura alta (más de 30°C), Humedad alta (más de 60%)", "Encender aire acondicionado")
    sistema_experto.agregar_regla("Temperatura baja (menos de 18°C)", "Encender calefacción")
    sistema_experto.agregar_regla("Temperatura moderada (18-30°C), Humedad moderada (40-60%)", "Ambiente confortable")

    while True:
        print("\n--- Sistema Experto con Base de Datos ---")
        print("1. Agregar hecho")
        print("2. Realizar inferencias")
        print("3. Mostrar hechos")
        print("4. Mostrar inferencias realizadas")
        print("5. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            hecho = input("Introduce un hecho: ").strip()
            sistema_experto.agregar_hecho(hecho)

        elif opcion == "2":
            print("\nRealizando inferencias...")
            inferencias_realizadas = sistema_experto.inferir()
            sistema_experto.mostrar_inferencias(inferencias_realizadas)

        elif opcion == "3":
            sistema_experto.mostrar_hechos()

        elif opcion == "4":
            # Para mostrar inferencias, primero deben ser realizadas
            inferencias_realizadas = sistema_experto.inferir()
            sistema_experto.mostrar_inferencias(inferencias_realizadas)

        elif opcion == "5":
            print("Saliendo del sistema experto.")
            sistema_experto.cerrar()
            break

        else:
            print("Opción no válida. Por favor, intenta de nuevo.")

# Ejecutar la interfaz de usuario
if __name__ == "__main__":
    interfaz_usuario()
