# Ken_Zenn_Publisher

## 概要
Zenn 記事を自動生成するシンプルな FastAPI サービスです。タイトルを送ると、バックエンドが Ollama（llama3）を使って Markdown 形式の記事を返し、`backend/articles/` に保存します。

## セットアップ

### Docker環境での開発

1. Docker と Docker Compose を用意する
2. リポジトリ直下でコンテナを起動:
   ```bash
   docker compose up -d --build
   ```
3. 動作確認:
   - ヘルスチェック: `GET http://localhost:8000/` → `{"status": "running"}`
   - 記事生成: `POST http://localhost:8000/generate`（JSON 例: `{"title": "Python 入門"}`）

生成された記事ファイルは `backend/articles/` にタイムスタンプ付きで保存されます。

### ローカル環境での開発（pre-commit使用時）

ローカルでpre-commitフックを使用する場合や、IDEでコード補完を使いたい場合は以下の手順で環境を構築してください。

1. Python 3.11以上をインストール
2. 仮想環境を作成してアクティベート:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Windowsの場合: .venv\Scripts\activate
   ```
3. 開発用の依存関係をインストール:
   ```bash
   pip install -e ".[dev]"
   ```
4. pre-commitフックをインストール:
   ```bash
   pre-commit install
   ```

これで、コミット時に自動的にRuffやBlackによるコードチェックとフォーマットが実行されます。

### 環境変数の設定

`.env.example`を`.env`にコピーして、必要な環境変数を設定してください:
```bash
cp .env.example .env
```

## プロジェクト構成

```
Kenn_Zenn_Publisher/
├── pyproject.toml          # 依存関係とプロジェクト設定
├── .pre-commit-config.yaml # pre-commit設定
├── docker-compose.yml      # Docker Compose設定
├── .env / .env.example     # 環境変数
└── backend/                # FastAPIアプリケーション
    ├── main.py             # エントリーポイント
    ├── core/               # 共通設定・ロガー
    ├── routers/            # APIエンドポイント
    ├── schemas/            # リクエスト/レスポンススキーマ
    ├── services/           # ビジネスロジック
    └── exceptions/         # カスタム例外
```
