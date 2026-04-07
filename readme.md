# 📊 Análise de Ações Fiscais e Trabalho Análogo à Escravidão no Brasil

Este projeto realiza a extração, tratamento e análise de dados do cadastro oficial de empregadores flagrados utilizando trabalho em condições análogas à escravidão no Brasil.

---

## Fonte dos dados

Dados oficiais disponíveis em:

https://www.gov.br/trabalho-e-emprego/pt-br/assuntos/inspecao-do-trabalho/areas-de-atuacao/cadastro_de_empregadores.pdf

- Formato original: PDF
- Extração automatizada via Python

---

## Tecnologias utilizadas

- Python
- pandas
- matplotlib
- pdfplumber

---

## Pipeline do projeto

1. Extração de dados do PDF
2. Limpeza e estruturação em DataFrame
3. Análise exploratória
4. Geração de gráficos

---

## Resultados

### Estados por ações fiscais (por ano)

#### 2024
![Top estados 2024](output/top_estados_2024.png)

#### 2025
![Top estados 2025](output/top_estados_2025.png)

#### 2026
![Top estados 2026](output/top_estados_2026.png)

---

### Evolução de ações fiscais por ano

![Evolução ações](output/acoes_por_ano.png)

---

### Estados por número de trabalhadores (geral)

![Top trabalhadores geral](output/top_trabalhadores_geral.png)

---

### Estados por número de trabalhadores (por ano)

#### 2023
![Trabalhadores 2023](output/top_trabalhadores_2023.png)

#### 2024
![Trabalhadores 2024](output/top_trabalhadores_2024.png)

#### 2025
![Trabalhadores 2025](output/top_trabalhadores_2025.png)

#### 2026
![Trabalhadores 2026](output/top_trabalhadores_2026.png)

---

### Evolução de ações fiscais e trabalhadores

![Evolução geral](output/acoes_trabalhadores.png)

---


## Limitações

- A extração pode não capturar 100% dos registros
- Possíveis inconsistências nos dados extraídos

---

## Como executar :

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/seu-repo.git
cd seu-repo

pip install -r requirements.txt

python analisadado.py ```



#### Autor:

Renan Tomazini e Copilot (apenas sintaxe, recuse trocar sua cognição pela máquina)
