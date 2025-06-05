from flask import Flask, jsonify, request
import datetime

# Cria a aplicação Flask
app = Flask(__name__)

# Rota principal para testar se a API está ativa
@app.route("/")
def home():
    return "🚨 SafeNet-AI API ativa!"

# Rota para receber dados dos sensores via POST
@app.route("/sensores", methods=["POST"])
def receber_dados():
    dados = request.json  # Pega os dados JSON enviados na requisição
    timestamp = datetime.datetime.now().isoformat()  # Data e hora do recebimento
    print(f"[{timestamp}] Dados recebidos: {dados}")  # Log no console
    # Retorna um JSON confirmando o sucesso
    return jsonify({"status": "sucesso", "mensagem": "Dados recebidos com sucesso"}), 200

# Executa a aplicação Flask
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
