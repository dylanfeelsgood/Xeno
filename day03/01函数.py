#你好-函数
# def say_hello(name):
#     print("hello"+","+name+"!")
#
# say_hello("xeno")

#BMI-函数
# def calculate_bmi(weight, height):
#     weight = float(weight)
#     height = float(height)
#
#     if height > 2.5:
#         height = height / 100
#
#     BMI_value = weight / (height * height)
#     return round(BMI_value, 2)
#
# result = calculate_bmi(52.5,1.68)
# print("你的BMI系数为:",result)

#明年的年龄函数
from datetime import date
def calculate_age(birth_date):
    today = date.today()
    age = (
        today.year
        - birth_date.year
        - ((today.month, today.day) < (birth_date.month, birth_date.day))
    +1)

    return age

try:
    year = int(input("请输入出生年份 (如 2000): "))
    month = int(input("请输入出生月份 (如 5): "))
    day = int(input("请输入出生日期 (如 20): "))

    # 将输入的数字转换为日期对象
    user_birth_date = date(year, month, day)

    # 调用函数并打印结果
    user_age = calculate_age(user_birth_date)
    print(f"明年你: {user_age} 岁")

except ValueError:
    print("输入错误！请输入正确的数字和有效的日期（例如2月没有30号）。")