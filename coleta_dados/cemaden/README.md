# Coleta de Dados - Monitoramento de Seca CEMADEN

Este script automatiza a coleta, extração e armazenamento de dados do relatório de monitoramento de seca do CEMADEN (maio 2025).  

Os dados são obtidos diretamente do PDF oficial, baixado automaticamente, e convertidos em texto e tabelas CSV para facilitar análises futuras.

---

## Estrutura dos arquivos

- `coleta_seca_cemaden.py` — Script principal que baixa o PDF, extrai texto e tabelas, e salva os dados localmente.
- `texto_monitoramento.txt` — Texto extraído do relatório (gerado após execução do script).
- `tabelas_extraidas/` — Pasta que contém os arquivos CSV das tabelas extraídas do PDF.

---

## Requisitos

- Python 3.7 ou superior  
- Bibliotecas Python:
  ```bash
  pip install requests pdfplumber pandas


