#include <WiFi.h>
#include <DHT.h>
#include <HTTPClient.h>

#define DHTPIN 4
#define DHTTYPE DHT22

const char* ssid = "Wokwi-GUEST"; // Mantenha sua rede Wi-Fi
const char* password = "TumTisTumTisTumTis123";        // Mantenha sua senha

// ▼▼▼ ALTERAÇÃO PRINCIPAL AQUI ▼▼▼
// Em caso do DNS não funcionar, use o IP direto do servidor
const char* serverName = "http://trabalhogs.westus3.cloudapp.azure.com:5000/api/sensores";
// const char* serverName = "http://57.154.50.104:5000/api/sensores";


DHT dht(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(115200);
  dht.begin();

  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Conectando ao WiFi...");
  }
  Serial.println("WiFi Conectado!");
  Serial.print("Endereço IP do dispositivo: ");
  Serial.println(WiFi.localIP());
}

void loop() {
  float temperatura = dht.readTemperature();
  float umidade = dht.readHumidity();

  if (!isnan(temperatura) && !isnan(umidade)) {
    Serial.printf("Lendo... Temp: %.2f °C | Umidade: %.2f %%\n", temperatura, umidade);

    HTTPClient http;
    http.begin(serverName);
    http.addHeader("Content-Type", "application/x-www-form-urlencoded");

    String dados = "temperatura=" + String(temperatura) + "&umidade=" + String(umidade);
    
    Serial.println("Enviando dados para a API...");
    int httpResponseCode = http.POST(dados);

    if (httpResponseCode > 0) {
      String response = http.getString();
      Serial.printf("Resposta da API (Código %d): %s\n", httpResponseCode, response.c_str());
    } else {
      Serial.printf("Erro no envio para a API. Código: %d\n", httpResponseCode);
      Serial.println("Verifique se o IP do servidor está correto e se a API está rodando.");
    }

    http.end();
  } else {
    Serial.println("Erro ao ler sensores.");
  }

  delay(30000); // Aguarda 30 segundos
