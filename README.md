# oda-api-server

このリポジトリは織田信長風の回答を生成するAPIサーバー

## 技術

- FastAPI
- LangChain
- Docker

## 環境セットアップ

1.リポジトリのクローン

   ```bash
   git clone [repository-url]
   cd oda_api_server
   ```

2．サーバーの起動
   ```bash
   uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
   ```

-UIでリクエストを送るツール「Postman」等


## プロジェクト構造

   ```sh
   programming-camp-lp/
├── public/          # 静的ファイル（画像など）
├── src/             # ソースコード
│   ├── components/  # Reactコンポーネント
│   │   ├── common/  # 共通コンポーネント
│   │   └── layout/  # レイアウト関連コンポーネント
│   ├── constants/   # 定数定義
│   └── types/       # TypeScript型定義
├── .gitignore      # Git除外設定
├── package.json    # プロジェクト設定
└── vite.config.ts  # Vite設定
```
