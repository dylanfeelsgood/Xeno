import requests

url = "https://api.siliconflow.cn/v1/chat/completions"
headers = {
    "Authorization": "Bearer sk-mvqgksivoxlksbtkeoqmtsyaieenlouowlqbspguipugcqok",
    "Content-Type": "application/json"
}
data = {
    "model": "Qwen/Qwen2.5-7B-Instruct",
    "messages": [{"role": "user", "content": "你好"}],
    "max_tokens": 50
}

r = requests.post(url, headers=headers, json=data, timeout=60)
print("状态码:", r.status_code)
print("响应:", r.text)