import os
import zipfile

# --- 1. CONFIGURAÇÃO (Obrigatório fazer antes de importar ou usar o Kaggle) ---
# Pega o caminho absoluto da pasta onde este script está (pasta src)
script_dir = os.path.dirname(os.path.abspath(__file__))

# Define a variável de ambiente para que o Kaggle procure o json AQUI, e não na home
os.environ['KAGGLE_CONFIG_DIR'] = script_dir

# Agora sim importamos a API (ela vai ler a variável acima)
from kaggle.api.kaggle_api_extended import KaggleApi

def download_dataset():
    # --- 2. Verificação de Segurança ---
    # Verifica se o kaggle.json realmente está na mesma pasta do script
    kaggle_json_path = os.path.join(script_dir, 'kaggle.json')
    if not os.path.exists(kaggle_json_path):
        print(f"❌ ERRO CRÍTICO: O arquivo 'kaggle.json' não foi encontrado em: {script_dir}")
        print("Certifique-se de que o arquivo está na mesma pasta deste script.")
        return

    # Proteção de permissão (necessário em alguns Linux/Mac para evitar outro erro)
    os.chmod(kaggle_json_path, 0o600)

    # --- 3. Definir caminhos de saída ---
    # Sobe um nível para sair de 'src' e ir para a raiz, depois entra em data/raw
    project_root = os.path.dirname(script_dir) 
    raw_data_path = os.path.join(project_root, 'data', 'raw')
    
    dataset_name = 'olistbr/brazilian-ecommerce'
    
    if not os.path.exists(raw_data_path):
        os.makedirs(raw_data_path)

    # --- 4. Baixar e Extrair ---
    try:
        print("🔑 Autenticando...")
        api = KaggleApi()
        api.authenticate() # Agora ele vai ler o json na pasta src
        
        print(f"⬇️ Baixando {dataset_name}...")
        api.dataset_download_files(dataset_name, path=raw_data_path, unzip=False)

        print("📦 Descompactando arquivos...")
        zip_path = os.path.join(raw_data_path, 'brazilian-ecommerce.zip')
        
        if os.path.exists(zip_path):
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                zip_ref.extractall(raw_data_path)
            
            os.remove(zip_path) 
            print(f"✅ Sucesso! Dados salvos em: {raw_data_path}")
            
            # Mostra apenas os arquivos CSV
            files = [f for f in os.listdir(raw_data_path) if f.endswith('.csv')]
            print(f"📂 {len(files)} arquivos CSV extraídos.")
        else:
            print("⚠️ Erro: O arquivo ZIP não foi encontrado após o download.")
            
    except Exception as e:
        print(f"❌ Erro durante o processo: {e}")
        # Dica extra caso seja erro de autenticação
        if "403" in str(e) or "401" in str(e):
             print("💡 Dica: Verifique se o seu kaggle.json é recente e válido.")

if __name__ == "__main__":
    download_dataset()