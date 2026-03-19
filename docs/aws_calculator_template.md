
# Template — AWS Pricing Calculator

## Objetivo
Comparar o custo mensal **On-Demand 100%** entre:
- **South America (São Paulo)**
- **US East (N. Virginia)**

## Configuração solicitada pelo enunciado
- Sistema operacional: Linux
- 2 CPUs
- 1 GiB de memória
- Até 5 Gigabit de rede
- 50 GB de armazenamento (HD)

## Recurso sugerido
### EC2
- Instância sugerida: **t3.micro**
- Motivo: atende de forma próxima os requisitos de 2 vCPU, 1 GiB RAM e até 5 Gigabit

### Armazenamento
- Volume EBS com **50 GB**
- Selecionar o tipo de armazenamento mais aderente ao pedido de “HD” na calculadora

---

## Resultado — preencher manualmente

### Região: São Paulo
- Custo da instância: `PREENCHER`
- Custo do armazenamento: `PREENCHER`
- Custo total mensal: `PREENCHER`

**Print da calculadora:**  
Inserir imagem aqui.

---

### Região: Norte da Virgínia
- Custo da instância: `PREENCHER`
- Custo do armazenamento: `PREENCHER`
- Custo total mensal: `PREENCHER`

**Print da calculadora:**  
Inserir imagem aqui.

---

## Análise comparativa
Texto sugerido:

A região **US East (N. Virginia)** tende a apresentar menor custo mensal, sendo normalmente a opção mais barata para workload simples em Linux.  
Entretanto, considerando a necessidade de acessar rapidamente os dados dos sensores e a existência de restrições legais para armazenamento no exterior, a região **São Paulo** se torna a escolha mais adequada para o cenário da fazenda, pois favorece menor latência e aderência regulatória.

---

## Passo a passo rápido
1. Acessar a AWS Pricing Calculator.
2. Criar uma estimativa nova.
3. Adicionar **Amazon EC2**.
4. Escolher **Linux**, **On-Demand**, **t3.micro**.
5. Confirmar a região.
6. Adicionar **50 GB** de armazenamento.
7. Repetir nas duas regiões.
8. Tirar prints e colar no README.
