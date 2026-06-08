#学生信息管理系统
student_info = []

#成绩判断函数
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

#学生信息输入函数
def information_student():
    name = input("请输入学生姓名：")
    try:
      score = float(input("请输入学生成绩："))
      if score > 100 or score < 0:
        print("成绩必须在0-100之间")
        return
    except ValueError:
        print("输入有误，成绩必须为数字")
        return
    grade = get_grade(score)
    student = {"name":name, "score":score, "grade":grade}
    student_info.append(student)
    print(f"已成功添加学生:{name}的信息")

#信息展示函数
def display_student_info():
    if not student_info:
        print("当前系统未录入学生信息，请等待")
        return
    for student in student_info:
        print(f"姓名: {student['name']}\t分数: {student['score']}\t等级: {student['grade']}")
        print("-----------------\n")

#查看平均分
def average_score():
    if not student_info:
        print("无学生信息，无法计算平均分")
        return

    total_score = 0
    for student in student_info:
        total_score += student["score"]

    average_score = total_score / len(student_info)
    print(f"当前全班平均分为:{round(average_score,2)}分")

#删除学生信息
def del_student_info():
    name_to_del = input("请输入要删除的学生姓名：")
    found = False
    for student in student_info:
        if student["name"] == name_to_del:
            student_info.remove(student)
            print(f"已成功删除学生{name_to_del}的信息")
            found = True
            break
    if not found:
        print(f"没有该学生{name_to_del}的相关信息")

#更新学生信息
def change_student_info():
    name_to_change =input("请输入要修改信息的学生姓名:")
    found = False
    for student in student_info:
        if student["name"] == name_to_change:
            score_input = float(input("请输入该学生的新成绩:"))
            student["score"] = float(score_input)
            student["grade"] = get_grade(score_input)
            print(f"已成功修改学生{name_to_change}的信息")
            found = True
            break
    if not found:
            print(f"没有该学生{name_to_change}的相关信息")

#主菜单
def main():
    while True:
        print("""
              ====== 学生成绩管理系统 ======
              1. 添加学生
              2. 显示所有学生
              3. 查看平均分
              4. 删除学生
              5. 修改信息
              6. 退出系统
              ============================
              """)
        choice = input("请选择操作(1-6):")
        if choice == "1":information_student()
        elif choice == "2":display_student_info()
        elif choice == "3":average_score()
        elif choice == "4":del_student_info()
        elif choice == "5":change_student_info()
        elif choice == "6":
          print("感谢使用，再见！")
          break
        else:
          print("操作无效，请输入1,2,3,4,5或6！")

if __name__ == "__main__":
    main()