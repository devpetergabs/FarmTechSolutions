# 🌱 FarmTech — Análise de Produção Agrícola e Estimativa de Custos na AWS

Este projeto tem como objetivo analisar dados de produção agrícola utilizando técnicas de Machine Learning e, posteriormente, estimar o custo de infraestrutura para execução dessa solução na AWS.

---

# 📊 Entrega 1 — Análise de Dados

## 📌 Objetivo

Realizar a análise de dados agrícolas e avaliar modelos de Machine Learning para predição de produtividade.

## 📁 Notebook

A análise completa pode ser acessada no notebook:

👉 `notebooks/GabrielPeter_rm567586.ipynb`

## ⚙️ O que foi realizado

* Carregamento e exploração do dataset
* Pré-processamento dos dados
* Treinamento de modelos de regressão:

  * Linear Regression
  * Random Forest
  * Gradient Boosting
  * Decision Tree
  * SVR
* Avaliação utilizando métricas:

  * RMSE
  * MAE
  * R²

## 📊 Resultados

Os modelos apresentaram desempenho limitado, com **R² negativo em todas as abordagens**, indicando baixa capacidade de explicação dos dados.

O modelo de **Linear Regression** apresentou o melhor desempenho relativo (menor erro), porém ainda insuficiente para uma predição confiável.

## ⚠️ Limitações

* Baixa qualidade ou quantidade de dados
* Poucas variáveis explicativas relevantes
* Alta variabilidade no dataset

## 🚀 Possíveis melhorias

* Aumentar volume de dados
* Realizar feature engineering
* Testar modelos mais avançados
* Aplicar tuning de hiperparâmetros

## 🎥 Vídeo demonstrativo

👉 (INSERIR LINK DO VÍDEO DA ENTREGA 1 AQUI)

---

# ☁️ Entrega 2 — Estimativa de Custos na AWS

## 📌 Objetivo

Realizar a estimativa de custos de infraestrutura na AWS utilizando o AWS Pricing Calculator, comparando diferentes regiões.

## ⚙️ Configuração utilizada

* Instância EC2: `t3.small`
* Sistema operacional: Linux
* Tempo de execução: 730 horas/mês
* Armazenamento: 50 GB (EBS - HDD)

## 🌎 Comparação entre regiões

| Região                | Custo mensal |
| --------------------- | ------------ |
| São Paulo (sa-east-1) | US$ 40,24    |
| Virgínia (us-east-1)  | US$ 23,56    |

## 📉 Análise de custos

A região **US East (N. Virginia)** apresentou uma economia aproximada de:

**~41% em relação à região de São Paulo**

## ⚖️ Justificativa técnica

Apesar do menor custo na região dos Estados Unidos, a escolha da região deve considerar outros fatores importantes:

* **Latência**: aplicações com sensores demandam resposta rápida, favorecendo regiões mais próximas
* **Conformidade legal**: pode haver restrições quanto ao armazenamento de dados fora do país
* **Disponibilidade e desempenho**

Dessa forma, a região de **São Paulo** pode ser mais adequada em cenários onde a proximidade dos dados é essencial, mesmo com custo mais elevado.

## 🖼️ Evidências

As simulações realizadas podem ser visualizadas na pasta:

👉 `figures/`

## 🎥 Vídeo demonstrativo

👉 (INSERIR LINK DO VÍDEO DA ENTREGA 2 AQUI)

---

# 📦 Estrutura do Projeto

```
data/           -> Dataset utilizado
docs/           -> Documentação auxiliar
figures/        -> Imagens das simulações AWS
notebooks/      -> Notebook principal
scripts/        -> Scripts auxiliares
README.md       -> Documentação principal
requirements.txt -> Dependências do projeto
```

---

# ⚙️ Como executar o projeto

## 1. Instalar dependências

```bash
pip install -r requirements.txt
```

## 2. Executar o notebook

Abra o notebook no Jupyter e selecione:

```
Run All
```

---

# 📌 Considerações finais

O projeto demonstra tanto a aplicação de técnicas de análise de dados quanto a avaliação de custos de infraestrutura em nuvem, destacando a importância do equilíbrio entre desempenho, custo e requisitos técnicos na tomada de decisão.

---
