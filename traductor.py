import requests

def traducir_texto(texto, idioma_destino="en"):
    url = "https://api.mymemory.translated.net/get"
    params = {
        "q": texto,
        "langpair": f"es|{idioma_destino}"
    }

    try:
        response = requests.get(url, params=params)
        data = response.json()

        if "responseData" in data and "translatedText" in data["responseData"]:
            return data["responseData"]["translatedText"]
        else:
            print("⚠️ Respuesta inesperada de la API:", data)
            return texto  # Devuelve el original si falla
    except Exception as e:
        print(f"❌ Error al traducir: {e}")
        return texto

def traducir_lista(lista_texto, idioma_destino="en"):
    traducciones = []
    for texto in lista_texto:
        traduccion = traducir_texto(texto, idioma_destino)
        traducciones.append(traduccion)
    return traducciones


# 🚀 EJEMPLO: traducir preguntas del chatbot automáticamente
preguntas = [
    "¿Cuál es tu nombre?",
    "¿Cómo estás?",
    "¿En qué puedo ayudarte hoy?",
    "¿Cuál es tu comida favorita?"
]

idioma_destino = "en"
traducidas = traducir_lista(preguntas, idioma_destino)

print("\n📋 Preguntas traducidas:")
for original, traducida in zip(preguntas, traducidas):
    print(f"- {original} -> {traducida}")
