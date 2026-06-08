#列表
# fruits = ["apple", "banana", "cherry"]
# for fruit in fruits:
#     print(fruit)


#字典
# scores = [90, 80, 75, 60]
# calculate_grades = []
# for score in scores:
#     if score >= 90 and score <= 100:
#         calculate_grades.append("A")
#     elif score >= 80 and score < 90:
#         calculate_grades.append("B")
#     elif score >= 70 and score < 80:
#         calculate_grades.append("C")
#     elif score >= 60 and score < 70:
#         calculate_grades.append("D")
#     else:
#         calculate_grades.append("不及格")
#
# print(f"Scores:{scores}",f"Calculate_grades:{calculate_grades}")

# #字典函数
# def get_grade(score):
#     if score >= 90 and score <= 100:
#         return 'A'
#     elif score >= 80 and score < 90:
#         return 'B'
#     elif score >= 70 and score < 80:
#         return 'C'
#     elif score >= 60 and score < 70:
#         return 'D'
#     else:
#         return '不及格'
#
# scores = [99,86,74,64,53]
# calculate_grades = []
#
# for score in scores:
#     calculate_grades.append(get_grade(score))
#
# print(f"Scores{scores}",f"Grade{calculate_grades}")


#个人姓名 年龄 学科
# students ={"name":"xeno","age":25,"major":"AI"}
# print(students["name"],students["age"],students["major"])

#多人成绩 不封装
# students = [
#     {"name": "小明", "score": 95},
#     {"name": "小红", "score": 82},
#     {"name": "小刚", "score": 75},
#     {"name": "小李", "score": 60},
#     {"name": "小张", "score": 45}
# ]
#
# for student in students:
#     score = student["score"]
#     current_name = student["name"]
#     if score >= 90 and score <= 100:
#         grade = "A"
#     elif score >= 80 and score < 90:
#         grade = "B"
#     elif score >= 70 and score < 80:
#         grade = "C"
#     elif score >= 60 and score < 70:
#         grade = "D"
#     else:
#         grade = "不及格"
#
#     print(f"姓名: {current_name} \t 成绩: {grade}")

#多人成绩 封装函数
def get_grade(score):
    if score >= 90 and score <= 100:
        return "A"
    elif score >= 80 and score < 90:
        return "B"
    elif score >= 70 and score < 80:
        return "C"
    elif score >= 60 and score < 70:
        return "D"
    else:
        return "不及格"

students = [
    {"name": "小明", "score": 95},
    {"name": "小红", "score": 82},
    {"name": "小刚", "score": 75},
    {"name": "小李", "score": 60},
    {"name": "小张", "score": 45}
]

for student in students:
    current_name = student["name"]
    current_score = student["score"]
    current_grade = get_grade(current_score)
    print(f"姓名:{current_name}\t成绩: {current_score}\t\t等级:{current_grade}")
