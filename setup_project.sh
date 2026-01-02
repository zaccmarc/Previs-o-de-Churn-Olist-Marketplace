#!/bin/bash

# Nome do diretório raiz
PROJECT_NAME="olist-churn-prediction"

echo "Criando estrutura do projeto: $PROJECT_NAME..."

# 1. Criar a árvore de diretórios principal
# O comando mkdir -p cria pastas pais e filhas de uma vez
mkdir -p "$PROJECT_NAME"/data/{raw,processed,feature_store}
mkdir -p "$PROJECT_NAME"/notebooks
mkdir -p "$PROJECT_NAME"/src
mkdir -p "$PROJECT_NAME"/models
mkdir -p "$PROJECT_NAME"/app/pages

# 2. Criar arquivos da pasta 'notebooks'
touch "$PROJECT_NAME"/notebooks/1.0_eda_inicial.ipynb
touch "$PROJECT_NAME"/notebooks/1.1_analise_temporal.ipynb
touch "$PROJECT_NAME"/notebooks/2.0_feature_engineering.ipynb
touch "$PROJECT_NAME"/notebooks/3.0_model_prototyping.ipynb

# 3. Criar arquivos da pasta 'src'
touch "$PROJECT_NAME"/src/__init__.py
touch "$PROJECT_NAME"/src/data_prep.py
touch "$PROJECT_NAME"/src/feature_eng.py
touch "$PROJECT_NAME"/src/model_train.py

# 4. Criar placeholders na pasta 'models' 
# (Nota: Na prática, estes arquivos serão gerados pelo Python, aqui criamos apenas arquivos vazios para ilustrar)
touch "$PROJECT_NAME"/models/churn_model_v1.pkl
touch "$PROJECT_NAME"/models/preprocessor.pkl

# 5. Criar arquivos da pasta 'app' e subpasta 'pages'
touch "$PROJECT_NAME"/app/main.py
touch "$PROJECT_NAME"/app/utils.py
touch "$PROJECT_NAME"/app/pages/1_Engenharia_Dados.py
touch "$PROJECT_NAME"/app/pages/2_Modelagem.py
touch "$PROJECT_NAME"/app/pages/3_Explicabilidade.py

# 6. Criar arquivos da raiz
touch "$PROJECT_NAME"/requirements.txt
touch "$PROJECT_NAME"/README.md

# 7. Adicionar .gitkeep em pastas vazias que precisam ser versionadas (Opcional, mas recomendado para o git)
touch "$PROJECT_NAME"/data/raw/.gitkeep
touch "$PROJECT_NAME"/data/processed/.gitkeep
touch "$PROJECT_NAME"/data/feature_store/.gitkeep

echo "✅ Estrutura criada com sucesso em ./$PROJECT_NAME"
echo "   Lembre-se de colocar os CSVs do Kaggle em: $PROJECT_NAME/data/raw/"

