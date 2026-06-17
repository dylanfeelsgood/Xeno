"""
主程序：聊天机器人入口
"""

from api import call_model, check_api_status
from history import ConversationHistory
from config import API_KEY


def print_welcome():
    """打印欢迎界面"""
    print("\n" + "🌟" * 25)
    print("      欢迎使用大模型聊天机器人！")
    print("🌟" * 25)
    print("\n📌 指令：")
    print("   输入内容 - 和AI对话")
    print("   clear     - 清空对话历史")
    print("   history  - 查看对话历史")
    print("   quit     - 退出程序\n")


def print_response(text):
    """美化输出"""
    print("\n" + "=" * 50)
    print("🤖 AI 助手：")
    print(text)
    print("=" * 50 + "\n")


def main():
    # 检查API配置
    if API_KEY == "YOUR_API_KEY":
        print("⚠️  请先编辑 config.py，填入你的 API Key！\n")
        print("   1. 打开 config.py")
        print("   2. 把 API_KEY = \"YOUR_API_KEY\" 改成你的密钥")
        print("   3. 保存后重新运行\n")
        return

    # 检查API连接
    print("🔍 检查API连接...", end=" ")
    if check_api_status():
        print("✅ 连接成功！\n")
    else:
        print("❌ 连接失败，请检查API Key和网络\n")
        return

    print_welcome()

    # 初始化历史记录管理器
    chat_history = ConversationHistory()

    while True:
        user_input = input("👤 你：").strip()

        if not user_input:
            print("📝 请说点什么吧...\n")
            continue

        # 处理特殊指令
        if user_input.lower() in ["quit", "exit", "退出"]:
            print("\n👋 再见！下次再聊\n")
            break

        if user_input.lower() == "clear":
            chat_history.clear()
            continue

        if user_input.lower() == "history":
            chat_history.show()
            continue

        # 调用模型
        print("🤖 思考中...", end="", flush=True)
        reply = call_model(user_input, chat_history.get())

        # 输出回复
        print("\r" + " " * 15 + "\r", end="")  # 清除"思考中"
        print_response(reply)

        # 保存历史
        chat_history.add(user_input, reply)


if __name__ == "__main__":
    main()
