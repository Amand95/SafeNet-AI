from flask import Flask, jsonify, request
import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return "🚨 SafeNet-AI API ativa!"

@app.route("/sensores", methods=["POST"])
def receber_dados():
    dados = request.json
    timestamp = datetime.datetime.now().isoformat()
    print(f"[{timestamp}] Dados recebidos: {dados}")
    return jsonify({"status": "sucesso", "mensagem": "Dados recebidos com sucesso"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
