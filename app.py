from flask import Flask, request, jsonify
from traductor import traducir
from utils.procesamiento import detectar_emocion, generar_respuesta

app = Flask(__name__)

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    mensaje_usuario = data["message"]

    emocion = detectar_emocion(mensaje_usuario)
    respuesta_ingles = generar_respuesta(mensaje_usuario, emocion)
    respuesta_espanol = traducir(respuesta_ingles)

    return jsonify({
        "respuesta": respuesta_espanol,
        "emocion": emocion
    })

if __name__ == "__main__":
    app.run(debug=True)
