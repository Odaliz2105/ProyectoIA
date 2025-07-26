import requests

def traducir(texto_en_ingles):
    url = "https://libretranslate.de/translate"
    payload = {
        "q": texto_en_ingles,
        "source": "en",
        "target": "es",
        "format": "text"
    }
    response = requests.post(url, data=payload)
    if response.status_code == 200:
        traduccion = response.json()["translatedText"]
        return traduccion
    else:
        return "Error en la traducción"
