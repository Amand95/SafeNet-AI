<p align="center">
  <img src="https://github.com/Amand95/SafeNet-AI/blob/6d1e324affc86a5ccf37fb3ee8041588bd78a7a3/SafeNet%20logo.png?raw=true" alt="SafeNet AI Logo" width="300"/>
</p>

# SafeNet AI – Sistema Inteligente de Monitoramento de Desastres Naturais 

## Visão Geral

O **SafeNet AI** é uma solução inteligente que utiliza sensores embarcados com **ESP32** e o poder da **Inteligência Artificial** para monitorar, prever e alertar sobre desastres naturais. Ao integrar **hardware de baixo custo**, **servidores em nuvem** e um **dashboard interativo**, o sistema visa proteger vidas e otimizar respostas emergenciais.

📡 **Sensores conectados** → ☁️ **Análise com IA na Azure** → 📊 **Visualização em tempo real via Streamlit**

---

## Objetivos

- Monitorar condições ambientais críticas (chuvas intensas, calor extremo, vibrações sísmicas, etc).
- Aplicar modelos de IA para prever eventos como enchentes, incêndios e terremotos.
- Enviar alertas antecipados com base em dados preditivos.
- Facilitar a tomada de decisões por meio de um painel web intuitivo.
- Reduzir custos com uma arquitetura baseada em **ESP32**, **cloud computing** e **open source**.

---

## Arquitetura do Projeto

### 🔧 1. ESP32 Firmware (Wokwi)
- Simulação de sensores: temperatura, umidade, pressão e vibração.
- Armazenamento local de dados críticos.
- Transmissão dos dados via Wi-Fi para a nuvem.

### ☁️ 2. Servidor Azure + IA
- Recebe dados dos dispositivos em tempo real.
- Processamento com **modelos preditivos (ML/LLM)**.
- Armazenamento e categorização dos alertas em banco de dados na nuvem.
- Resposta em tempo real para o frontend.

### 💻 3. Dashboard Interativo (Streamlit)
- Interface leve e acessível para visualização.
- Módulos:
  - Painel de dados em tempo real
  - Previsões geradas por IA
  - Histórico de alertas e eventos
- Acesso via desktop ou mobile (responsivo).

---

## 🌐 Acesso ao Dashboard Streamlit

Acesse o painel de visualização em tempo real:

🔗 [http://57.154.50.104:8506/](http://57.154.50.104:8506/)

Este painel exibe:
- Leituras dos sensores (temperatura, umidade, movimento)
- Gráficos em tempo real
- Análises fornecidas pela IA via Azure
  
---  

#### Simulação no Wokwi

Você pode testar a simulação do circuito ESP32 com DHT22 clicando no link abaixo:

[Simulação Wokwi - ESP32 com DHT22](https://wokwi.com/projects/432958048477552641)

### 🖼️ Diagrama do Circuito  
![Circuito Simulado no Wokwi](./esp32/esp32.JPG)

---

⚙️ Lógica do Código ESP32
O código C++ foi desenvolvido para simular um sistema de monitoramento de desastres naturais com base em sensores conectados ao ESP32.

Principais funções:
Leitura dos sensores:
O sensor DHT22 coleta temperatura e umidade do ambiente, enquanto o sensor de vibração simula tremores sísmicos.

Ação sobre o relé virtual:
Um relé é acionado automaticamente quando os dados indicam condições críticas, como:

Temperatura > 35°C

Vibração detectada

Umidade acima ou abaixo de limiares pré-definidos

---

## 🛠️ Tecnologias Utilizadas

| Tecnologia      | Uso Principal                                 |
|-----------------|-----------------------------------------------|
| ESP32         | Captura e envio de dados dos sensores         |
| Wokwi         | Simulação do hardware para testes iniciais    |
| Python        | Backend, IA e integração geral                |
| Flask         | API REST entre ESP32 e servidor Azure         |
| Azure         | Processamento e armazenamento na nuvem        |
| Streamlit     | Visualização dos dados e alertas em tempo real |
| Scikit-learn  | Modelos de Machine Learning para predição     |

---

## 📌 Funcionalidades

- ✅ Monitoramento contínuo e automatizado
- ✅ IA preditiva com base em histórico e padrões climáticos
- ✅ Painel web com alertas e insights
- ✅ Design modular e escalável
- ✅ Simulação 100% funcional via Wokwi

---

## 🌟 Diferenciais

- Baixo custo e fácil escalabilidade
- Solução conectada e adaptável a qualquer região
- Pensado para segurança e acessibilidade em situações críticas
- Alinhado aos ODS da ONU (Objetivos de Desenvolvimento Sustentável)

---

## 🚀 Como Executar

1. Clone o repositório:
   ```bash
   git clone https://github.com/Amand95/SafeNet-AI.git
   cd safenet-ai


