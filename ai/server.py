from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/analise", methods=["POST"])
def analisar():
    dados = request.get_json()

    temperatura = dados.get("temperatura", 0)
    umidade = dados.get("umidade", 0)
    movimento = dados.get("movimento", False)

    if temperatura > 30 and umidade > 60 and movimento:
        resultado = "Risco elevado: ambiente quente e úmido com movimento detectado"
    elif temperatura > 30:
        resultado = "Alerta: temperatura alta"
    elif umidade > 70:
        resultado = "Alerta: umidade excessiva"
    else:
        resultado = "Ambiente seguro"

    return jsonify({"resultado": resultado})

if __name__ == "__main__":
    app.run(debug=True, por
