import pickle
from keras.models import load_model

# Cargar modelos
modelo_emociones = pickle.load(open("../modelos/modelo_emocional.pkl", "rb"))
vectorizador = pickle.load(open("../modelos/vectorizador_emocional.pkl", "rb"))
modelo_chatbot = load_model("../modelos/chatbot_encoder.weights.h5")

# Tokenizers aquí...

def detectar_emocion(texto):
    texto_vector = vectorizador.transform([texto])
    emocion = modelo_emociones.predict(texto_vector)
    return emocion[0]

def generar_respuesta(texto, emocion):
    # Aquí iría la lógica que usa el modelo para generar una respuesta
    return "I'm here to help you feel better."  # ejemplo simple
