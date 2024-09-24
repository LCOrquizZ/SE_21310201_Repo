import json

# Archivo donde se almacenará el conocimiento
knowledge_file = 'knowledge_base.json'

# Cargar o inicializar la base de conocimiento
def load_knowledge():
    try:
        with open(knowledge_file, 'r') as file:
            knowledge_base = json.load(file)
    except FileNotFoundError:
        # Si no existe el archivo, inicializamos con conocimiento base
        knowledge_base = {
            "Hola": "Hola, ¿cómo estás?",
            "¿Cómo estás?": "Estoy bien, gracias por preguntar.",
            "¿De qué te gustaría hablar?": "Puedo hablar sobre cualquier cosa que quieras."
        }
    return knowledge_base

# Guardar la base de conocimiento
def save_knowledge(knowledge_base):
    with open(knowledge_file, 'w') as file:
        json.dump(knowledge_base, file, indent=4)

# Función de chat
def chat():
    knowledge_base = load_knowledge()
    
    print("ChatBot: Hola, soy tu asistente virtual.")
    
    while True:
        user_input = input("Tú: ").strip()
        
        # Verificar si el usuario quiere salir del chat
        if user_input.lower() in ['salir', 'adiós', 'chao', 'cámara']:
            print("ChatBot: ¡Hasta luego!")
            break
        
        # Verificar si el input del usuario está en la base de conocimiento
        if user_input in knowledge_base:
            print(f"ChatBot: {knowledge_base[user_input]}")
        else:
            # El input no está en la base de conocimiento
            print("ChatBot: No sé la respuesta a esa pregunta.")
            new_response = input("¿Cuál debería ser la respuesta correcta?: ").strip()
            
            # Agregar el nuevo conocimiento a la base de datos
            knowledge_base[user_input] = new_response
            save_knowledge(knowledge_base)
            
            print("ChatBot: ¡Gracias! He aprendido algo nuevo.")

# Iniciar el chat
chat()