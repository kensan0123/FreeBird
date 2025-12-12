from anthropic import Anthropic
from backend.core.settings import settings
from typing import List
from backend.schemas.assistant_schemas import WebSearchResponse, RelatedLink
from backend.exceptions.exceptions import AgentException


class WebSearchAgent:
    def __init__(self):
        self._client = Anthropic(api_key=settings.ANTHROPIC_API_KEY)

    def search_web(self, query: str) -> WebSearchResponse:
        """web search agent"""

        _system_prompt = ""
        _tools = [{"type": "web_search_20250305", "name": "web_search", "max_uses": 5}]
        _prompt = ""
        _messages = [{"role": "user", "content": _prompt}]

        response = self._client.messages.create(
            model="claude-3-5-haiku-latest",
            max_tokens=500,
            system=_system_prompt,
            tools=_tools,
            messages=_messages,
        )

        if response.stop_reason == "end_turn":
            _related_links: List[RelatedLink] = []
            for block in response.content:
                if block.type == "web_search_tool_result":
                    for b in block.content:
                        if b.type == "web_search_result":
                            _related_links.append(b.url)

                elif block.type == "text":
                    _search_result: str = block.text

                    search_response: WebSearchResponse = WebSearchResponse(
                        search_result=_search_result, related_links=_related_links
                    )

                    return search_response
            raise AgentException(
                message="Web search agent error: response not exist",
                endpoint="/assist",
            )
        else:
            raise AgentException(
                message="Web search agent error",
                endpoint="/assist",
            )

    def _system_prompt(self):
        _system_prompt = """
        ## 役割
        あなたはWeb検索、レポートエージェントです。親エージェントから検索指示が与えられるので、Web検索ツールを使って
        親エージェントが求める情報を検索し、親エージェントに端的に検索結果を報告します。

        ## ツール
        - Web search

        ## 出力要件
        - JSONのみで出力
        - 下記で指定したJSONスキーマを厳守すること。

        ## 出力スキーマ
        
        ```output_schema.json
        {
            "type": "object",
            "property": {
                "report": {
                    "type": "string(markdown)",
                    "description": "summary of this search",
                },
            },
        }
        ```

        ##出力例

        ```output_example.json
        {
            "report": "## Zenn CLI応用（CI/CD）レポート
            
            ### **1. GitHub連携による自動公開**
            GitHubリポジトリと連携することで、`main`ブランチへのpushで記事が自動的にZennに公開され
            ます。コミットメッセージに`[ci skip]`または`[skip ci]`を含めるとデプロイをスキップで
            きます。

            ### **2. GitHub Actionsとの統合**

            **品質チェック自動化:**
            - textlint/markdownlintでMarkdownの自動校正
            - 日本語表記ゆれの検出
            - PRトリガーでのLint実行

            **予約投稿機能:**
            - Front Matterの`published_at`で公開日時を指定
            - GitHub Actionsのcron設定で定期チェック
            - 指定時刻に自動で`published: true`に更新

            **自動レビューシステム:**
            - LLM（Gemini/Claude）による機密情報チェック
            - レビュワーの自動アサイン
            - Teams/Slackへの通知連携

            ### **3. ブランチ戦略**
            - ブランチ名プレフィックス（`draft/`, `review/`, `publish/`）で処理を自動分岐
            - Publication Proの特性に最適化された段階的公開フロー

            ### **4. その他の応用**
            - pre-commitフック（husky/lefthook）でローカルでのLint実行
            - 画像最適化スクリプトの自動実行
            - Git履歴管理によるバージョン管理とバックアップ

            CI/CDを活用することで、記事品質の担保、チーム執筆の効率化、安全な公開フローを実現できます。"
        }
        ```
        """
