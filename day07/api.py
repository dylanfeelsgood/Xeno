"""
API模块：与大模型通信
"""

import requests
from config import API_KEY, API_URL, MODEL, TEMPERATURE, MAX_TOKENS, SYSTEM_PROMPT


def build_messages(conversation_history, user_message):
    """
    构建完整的消息列表
    格式：[系统设定] + [历史对话] + [当前问题]
    """
    messages = [{"role": "system", "content": SYSTEM_PROMPT}]
    messages.extend(conversation_history)
    messages.append({"role": "user", "content": user_message})
    return messages


def call_model(user_message, conversation_history=None):
    """
    调用大模型API，返回回复文本

    参数：
        user_message: 用户输入
        conversation_history: 历史对话列表

    返回：
        模型回复字符串，或错误信息
    """
    if conversation_history is None:
        conversation_history = []

    messages = build_messages(conversation_history, user_message)

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": MODEL,
        "messages": messages,
        "temperature": TEMPERATURE,
        "max_tokens": MAX_TOKENS
    }

    try:
        response = requests.post(API_URL, json=payload, headers=headers, timeout=60)
        response.raise_for_status()
        result = response.json()
        return result["choices"][0]["message"]["content"]
    except requests.exceptions.Timeout:
        return "❌ 请求超时，请检查网络连接"
    except requests.exceptions.RequestException as e:
        return f"❌ 请求失败：{e}"
    except KeyError:
        return "❌ API返回格式异常，请检查API Key和余额"


def check_api_status():
    """检查API是否可用"""
    test_message = [{"role": "user", "content": "Hi"}]

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": MODEL,
        "messages": test_message,
        "max_tokens": 10
    }

    try:
        response = requests.post(API_URL, json=payload, headers=headers, timeout=10)
        return response.status_code == 200
    except:
        return False


