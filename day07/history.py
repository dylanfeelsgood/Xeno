"""
历史记录模块：管理对话历史
"""

from config import MAX_HISTORY_PAIRS


class ConversationHistory:
    """对话历史管理器"""

    def __init__(self, max_pairs=MAX_HISTORY_PAIRS):
        """
        初始化
        max_pairs: 最大保留对话轮数
        """
        self.history = []
        self.max_pairs = max_pairs

    def add(self, user_message, assistant_message):
        """添加一轮对话"""
        self.history.append({"role": "user", "content": user_message})
        self.history.append({"role": "assistant", "content": assistant_message})
        self._trim()

    def _trim(self):
        """修剪过长历史"""
        if len(self.history) > self.max_pairs * 2:
            self.history = self.history[-(self.max_pairs * 2):]

    def get(self):
        """获取完整历史"""
        return self.history

    def clear(self):
        """清空历史"""
        self.history = []
        print("🗑️  对话历史已清空")

    def show(self):
        """打印历史（调试用）"""
        print("\n📜 当前对话历史：")
        for i, msg in enumerate(self.history):
            role = "👤" if msg["role"] == "user" else "🤖"
            content = msg["content"][:50] + "..." if len(msg["content"]) > 50 else msg["content"]
            print(f"  {role} {content}")
        print()

    def length(self):
        """返回历史长度"""
        return len(self.history)
