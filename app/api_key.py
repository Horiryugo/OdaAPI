# ※本番では、初期化時に外部データベースやキャッシュから API key をロードするなどの工夫が必要です
import os

# 例として、事前に生成・保存した API key 一覧をメモリ上にロード（ここではシンプルな例）
# 実際にはファイルやクラウドデータストアからの読み込みを検討
VALID_API_KEYS = set()

def load_api_keys():
    # 例: ファイル "api_keys.txt" に 1 行につき 1 API key が記載されていると仮定
    file_path = os.getenv("API_KEYS_FILE", "api_keys.txt")
    try:
        with open(file_path, "r") as f:
            for line in f:
                key = line.strip()
                if key:
                    VALID_API_KEYS.add(key)
    except FileNotFoundError:
        # ローカル開発用にテストデータを設定
        VALID_API_KEYS.update({"testkey123", "samplekey456"})

# プロセス起動時にロード
load_api_keys()

def validate_api_key(api_key: str) -> bool:
    return api_key in VALID_API_KEYS
