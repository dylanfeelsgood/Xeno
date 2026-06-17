"""
Flask 后端：接收网页请求，调用大模型API
"""

from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
import requests
from config import API_KEY, API_URL, MODEL

app = Flask(__name__)
CORS(app)  # 允许跨域访问

# 对话历史
conversation_history = []


@app.route("/")
def index():
    """返回网页前端"""
    return send_file("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    """处理聊天请求"""
    global conversation_history

    user_message = request.json.get("message", "")

    # 构建消息
    messages = [
                   {"role": "system", "content": "你是一个友好、有帮助的AI助手。"}
               ] + conversation_history + [
                   {"role": "user", "content": user_message}
               ]

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": MODEL,
        "messages": messages,
        "temperature": 0.7,
        "max_tokens": 1000
    }

    try:
        response = requests.post(API_URL, json=payload, headers=headers, timeout=60)
        result = response.json()
        assistant_message = result["choices"][0]["message"]["content"]

        # 保存历史
        conversation_history.append({"role": "user", "content": user_message})
        conversation_history.append({"role": "assistant", "content": assistant_message})

        # 限制长度
        if len(conversation_history) > 20:
            conversation_history = conversation_history[-20:]

        return jsonify({"reply": assistant_message})

    except Exception as e:
        return jsonify({"reply": f"出错了：{e}"}), 500


@app.route("/clear", methods=["POST"])
def clear():
    """清空对话"""
    global conversation_history
    conversation_history = []
    return jsonify({"status": "ok"})


if __name__ == "__main__":
    print("\n🌐 网页版聊天机器人已启动！")
    print("📍 打开浏览器访问：http://127.0.0.1:5000\n")
    app.run(debug=True, port=5000)
