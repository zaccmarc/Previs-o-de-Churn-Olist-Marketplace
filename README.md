# 📑 Previsão de Churn - Olist Marketplace

## 1. O Problema de Negócio
A **Olist** conecta pequenas lojas a grandes marketplaces. O custo para adquirir um novo cliente (CAC) é alto, e a rentabilidade do negócio depende diretamente da recorrência de compras (LTV).

* **A Dor:** Atualmente, não há como identificar proativamente quais usuários pararam de engajar com a plataforma.
* **O Desafio Específico:** Diferente de empresas de telecom ou SaaS, o varejo não possui um "cancelamento de contrato". O churn é silencioso (Non-contractual Churn). Um cliente pode não comprar há 3 meses e voltar, ou nunca mais voltar.
* **A Questão Chave:**
    > "Quais clientes têm alta probabilidade de não realizar uma nova compra nos próximos X dias (ex: 90 dias), baseando-se em seu histórico de comportamento, logística e avaliações?"

---

## 2. Objetivo do Projeto
Desenvolver uma solução de Data Science *end-to-end* que transforme dados brutos transacionais em inteligência acionável para a equipe de retenção e marketing.

* **Objetivo Primário:** Criar um modelo de Machine Learning capaz de classificar clientes com risco de abandono (Churn), com foco na maximização da métrica **Recall** (minimizando Falsos Negativos, ou seja, evitar deixar passar um cliente que vai sair).
* **Objetivo Secundário:** Identificar os "drivers" do churn.
    * *Exemplos:* Atraso na entrega impacta mais que o preço do frete? Notas baixas de review são determinantes?

---

## 3. O Entregável (Solução)
A entrega final será uma **Aplicação Web Interativa (Streamlit)** composta por três módulos principais:

### A. Módulo de Engenharia de Dados (Backend)
* Pipeline de ETL que une as tabelas relacionais da Olist (`customers`, `orders`, `order_items`, `reviews`, etc.).
* **Criação da variável Target (Churn):** Definição de uma janela de inatividade baseada em análise de frequência (ex: clientes sem compras há > 90 dias).
* **Engenharia de Features:** RFM (Recência, Frequência, Valor), Tempo médio de entrega, Score médio de satisfação, Geolocalização.

### B. Painel de Controle de Modelagem (Frontend - Streamlit)
* **Sandbox de Hiperparâmetros:** Interface para ajustar *Learning Rate*, *Max Depth* e *Estimators* do modelo (XGBoost/LightGBM) e re-treinar em tempo real.
* **Monitor de Métricas:** Visualização dinâmica da Matriz de Confusão, Curva ROC-AUC, Acurácia e Recall.

### C. Módulo de Explicação e Decisão (Frontend - Streamlit)
* **Análise Global:** Gráficos SHAP (Summary Plot) mostrando quais variáveis (ex: frete, atraso) mais contribuem para o churn no geral.
* **Simulador de Cliente:** Ferramenta onde o usuário insere dados de um cliente hipotético (ou seleciona um ID real) e o modelo retorna a probabilidade de churn com a explicação do "porquê" (SHAP Force Plot).

---

## 📂 Estrutura do Projeto

```text
olist-churn-prediction/
│
├── data/                        # Onde os dados vivem (NUNCA edite o raw manualmente)
│   ├── raw/                     # Os 9 CSVs originais do Kaggle (imutável)
│   ├── processed/               # Dados limpos e tabelas unificadas (o "Tabelão" pré-feature eng)
│   └── feature_store/           # O dataset final pronto para o modelo (X e y definidos)
│
├── notebooks/                   # Seu ambiente de trabalho ATUAL (EDA e Prototipagem)
│   ├── 1.0_eda_inicial.ipynb    # Análise de distribuição, nulos, outliers
│   ├── 1.1_analise_temporal.ipynb # Entender a frequência de compra para definir a janela de churn
│   ├── 2.0_feature_engineering.ipynb # Criação de RFM, Geolocalização e Target
│   └── 3.0_model_prototyping.ipynb   # Testes iniciais com XGBoost/LightGBM
│
├── src/                         # Código Python modularizado (Refatoração dos notebooks)
│   ├── __init__.py
│   ├── data_prep.py             # Funções de limpeza e joins
│   ├── feature_eng.py           # Classes/Funções para calcular RFM e Target
│   └── model_train.py           # Script de treinamento do modelo
│
├── models/                      # Onde os modelos treinados serão salvos
│   ├── churn_model_v1.pkl       # O arquivo binário do modelo (pickle/joblib)
│   └── preprocessor.pkl         # Scalers ou Encoders salvos para usar no app
│
├── app/                         # O código da aplicação Streamlit (Seu entregável final)
│   ├── main.py                  # Ponto de entrada do app
│   ├── utils.py                 # Funções auxiliares de visualização
│   └── pages/                   # Estrutura multipage do Streamlit
│       ├── 1_Engenharia_Dados.py
│       ├── 2_Modelagem.py
│       └── 3_Explicabilidade.py
│
├── requirements.txt             # Bibliotecas do projeto (pandas, streamlit, shap, xgboost)
└── README.md                    # Documentação do projeto
```
## 4. Resultados Esperados
### 🏢 Para o Negócio
* **Segmentação Preventiva:** Geração de lista de clientes em risco para envio de cupons de reativação ou campanhas de e-mail marketing.

* **Diagnóstico Operacional:** Entendimento claro se problemas logísticos (atrasos) estão "matando" a base de clientes (validação se delivery_delay é uma feature importante).

### 💻 Técnicos (Data Science)
* Desenvolvimento de um modelo robusto com capacidade de generalização.

* Criação de uma interface funcional que abstrai a complexidade do código para o usuário final.

* Demonstração de competência em manipulação de SQL/Pandas (joins complexos) e Modelagem Preditiva.