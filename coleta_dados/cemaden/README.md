# Coleta de Dados - Monitoramento de Seca CEMADEN

Este script automatiza a coleta, extração e armazenamento de dados do relatório de monitoramento de seca do CEMADEN (maio 2025).  

Os dados são obtidos diretamente do PDF oficial, baixado automaticamente, e convertidos em texto e tabelas CSV para facilitar análises futuras.

---

## Estrutura dos arquivos

- `coleta_seca_cemaden.py` — Script principal que baixa o PDF, extrai texto e tabelas, e salva os dados localmente.
- `texto_monitoramento.txt` — Arquivo gerado automaticamente contendo o texto extraído do relatório.
- `tabelas_extraidas/` — Pasta contendo arquivos CSV com tabelas extraídas do relatório.

---

## Requisitos

- Python 3.7 ou superior  
- Bibliotecas Python:
  ```bash
  pip install requests pdfplumber pandas


