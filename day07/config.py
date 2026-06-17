#配置API 参数模块

API_KEY = "sk-mvqgksivoxlksbtkeoqmtsyaieenlouowlqbspguipugcqok"
API_URL = "https://api.siliconflow.cn/v1/chat/completions"
MODEL = "Qwen/Qwen2.5-7B-Instruct"

#模型参数
TEMPERATURE = 0.7
MAX_TOKENS = 800

#系统设定
SYSTEM_PROMPT = "你是一个友好、有帮助的聊天助手。"

#历史记录限制
MAX_HISTORY_PAIRS = 10 # 保留最近10轮对话（每轮=用户+助手=2条）
