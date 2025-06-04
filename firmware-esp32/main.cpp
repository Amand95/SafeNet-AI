#include <WiFi.h>
#include <DHT.h>
#include <HTTPClient.h>

#define DHTPIN 4
#define DHTTYPE DHT22

const char* ssid = "Wokwi-GUEST";
const char* password = "";

const char* serverName = "https://seu-endpoint.azurewebsites.net/api/sensores";

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
}

void loop() {
  float temperatura = dht.readTemperature();
  float umidade = dht.readHumidity();

  if (!isnan(temperatura) && !isnan(umidade)) {
    Serial.printf("Temp: %.2f °C | Umidade: %.2f %%\n", temperatura, umidade);

    WiFiClient client;
    HTTPClient http;

    http.begin(client, serverName);
    http.addHeader("Content-Type", "application/x-www-form-urlencoded");

    String dados = "temperatura=" + String(temperatura) + "&umidade=" + String(umidade);
    int httpResponseCode = http.POST(dados);

    if (httpResponseCode > 0) {
      Serial.println("Dados enviados com sucesso.");
    } else {
      Serial.printf("Erro no envio: %d\n", httpResponseCode);
    }

    http.end();
  } else {
    Serial.println("Erro ao ler sensores.");
  }

  delay(10000);  // Aguarda 10 segundos
}
