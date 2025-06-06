#include <Arduino.h>
#include "sensores.h"

#define RELE_PIN 5

void setup() {
  Serial.begin(115200);
  pinMode(RELE_PIN, OUTPUT);
  inicializarSensores();
}

void loop() {
  float temperatura = lerTemperatura();
  float umidade = lerUmidade();
  bool movimento = detectarMovimento();

  Serial.printf("Temp: %.2f C, Umid: %.2f %%, Movimento: %d\n", temperatura, umidade, movimento);

  // Lógica para acionar relé (exemplo simples)
  if (temperatura > 30.0 || movimento) {
    digitalWrite(RELE_PIN, HIGH);
  } else {
    digitalWrite(RELE_PIN, LOW);
  }

  delay(2000); // espera 2 segundos
}
