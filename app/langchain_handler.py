import os
import requests
from langchain.prompts import PromptTemplate

# Groq APIキー（環境変数が使えない場合は直接入力）
GROQ_API_KEY = os.getenv("GROQ_API_KEY", "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")

# Groq API のエンドポイント
GROQ_API_URL = "https://api.groq.com/v1/chat/completions"

# プロンプトテンプレートの定義
prompt_template = PromptTemplate(
    input_variables=["question"],
    template=(
        "あなたは戦国時代の武将、織田信長である。"
        "以下の質問に、信長らしい口調と考え方で回答せよ。\n"
        "質問: {question}\n"
        "回答:"
    )
)

def generate_answer(question: str, api_key: str) -> str:
    prompt = prompt_template.format(question=question)

    data = {
        "model": "mixtral-8x7b-32k",  # Groqの無料モデル
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.7
    }

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    response = requests.post(GROQ_API_URL, headers=headers, json=data)

    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        return f"Error: {response.status_code}, {response.text}"
