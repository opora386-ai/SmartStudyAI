import os
from flask import Flask, request, jsonify
from groq import Groq

app = Flask(__name__)

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

@app.route("/")
def home():
    return "SmartStudy AI server is running!"

@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json(silent=True) or {}
    question = data.get("question", "").strip()

    if not question:
        return jsonify({"error": "Введите вопрос"}), 400

    try:
        response = client.chat.completions.create(
            model=os.environ.get(
                "GROQ_MODEL",
                "llama-3.3-70b-versatile"
            ),
            messages=[
                {
                    "role": "system",
                    "content": (
                        "Ты SmartStudy AI — дружелюбный "
                        "помощник для учёбы. Объясняй понятно "
                        "и помогай ученикам разбираться в темах."
                    )
                },
                {"role": "user", "content": question}
            ]
        )

        answer = response.choices[0].message.content
        return jsonify({"answer": answer})

    except Exception:
        app.logger.exception("Ошибка Groq")
        return jsonify({
            "error": "Не удалось получить ответ. Попробуйте позже."
        }), 502
