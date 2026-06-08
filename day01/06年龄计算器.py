from datetime import date #导入工具箱

def calculate_age(birth_date):
    # 1. 获取今天的日期
    today = date.today()

    # 2. 核心逻辑：计算年份差，并根据是否过了生日进行调整
    age = (
        today.year
        - birth_date.year
        - ((today.month, today.day) < (birth_date.month, birth_date.day))
    )

    return age

# 3. 用户交互与防错处理
try:
    year = int(input("请输入出生年份 (如 1995): "))
    month = int(input("请输入出生月份 (如 5): "))
    day = int(input("请输入出生日期 (如 20): "))

    # 将输入的数字转换为日期对象
    user_birth_date = date(year, month, day)

    # 调用函数并打印结果
    user_age = calculate_age(user_birth_date)
    print(f"你的精准年龄是: {user_age} 岁")

except ValueError:
    print("输入错误！请输入正确的数字和有效的日期（例如2月没有30号）。")