def calculate_salary(base_salary, bonus):
    # 1. 计算应发工资（税前总额）
    gross_salary = base_salary + bonus

    # 2. 计算社保/五险一金扣除（假设占税前总额的 14%）
    insurance = gross_salary * 0.14

    # 3. 计算应纳税所得额（税前总额减去社保）
    taxable_income = gross_salary - insurance

    # 4. 计算个人所得税（假设税率为 5%）
    tax = taxable_income * 0.05 if taxable_income > 0 else 0

    # 5. 计算实发工资（真正到手的钱）
    net_salary = gross_salary - insurance - tax

    return gross_salary, insurance, tax, net_salary


# 主程序交互
try:
    # 6. 获取用户输入
    input_base = float(input("请输入您的基本工资（元）: "))
    input_bonus = float(input("请输入您的奖金/补贴（元）: "))

    # 7. 调用函数进行计算
    gross_salary, insurance, tax, net_salary = calculate_salary(input_base, input_bonus)

    # 8. 格式化打印工资单
    print("\n" + "=" * 10 + " 您的电子工资单 " + "=" * 10)
    print(f"1. 应发工资（税前）: {gross_salary:.2f} 元")
    print(f"2. 五险一金扣除 (14%): {insurance:.2f} 元")
    print(f"3. 个人所得税 (5%):   {tax:.2f} 元")
    print("-" * 32)
    print(f"4. 实发工资（到手）: {net_salary:.2f} 元")
    print("=" * 32)

except ValueError:
    print("输入错误！请请输入正确的数字（例如: 8500 或 1200.50）。")