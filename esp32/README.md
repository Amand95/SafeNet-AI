# Código ESP32 SafeNet-AI

Este diretório contém o código fonte em C++ para o ESP32 responsável pela leitura dos sensores (temperatura, umidade, movimento) e acionamento do relé conforme lógica definida.

## Estrutura

- `main.cpp`: código principal que inicializa sensores, lê valores e controla relé.
- `sensores.cpp` / `sensores.h`: funções simuladas para leitura dos sensores.
- `platformio.ini`: configuração para desenvolvimento com PlatformIO.

## Lógica do Controle

O relé é acionado quando a temperatura ultrapassa 30ºC ou é detectado movimento.

## Como compilar e carregar

- Requer PlatformIO instalado.
- Na raiz desta pasta, rode:

```bash
platformio run
platformio run --target upload
platformio device monitor
