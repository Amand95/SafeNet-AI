# Coleta de Dados – Monitoramento de Seca CEMADEN

## Descrição
Script que automatiza a coleta, extração e transformação dos dados de monitoramento de seca no Brasil, utilizando o relatório oficial do CEMADEN.

## Passos:
1. Baixa automaticamente o relatório em PDF.
2. Extrai o texto e eventuais tabelas.
3. Salva em arquivos `.txt` e `.csv` para análise e posterior uso no banco de dados.

## Como rodar:
```bash
pip install requests pdfplumber pandas
python coleta_seca_cemaden.py
