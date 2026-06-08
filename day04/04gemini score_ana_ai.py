# 1. 批量输入成绩
def input_scores():
    user_input = input("请输入一组成绩（用空格隔开）: ")
    str_list = user_input.split()
    scores = []
    for s in str_list:
        scores.append(float(s))
    print(f"✅ 成功录入了 {len(scores)} 个成绩！")
    return scores


# 2. 查询成绩的最大值 最小值 平均值 (你写的，非常完美！)
def list_score(scores):
    max_score = max(scores)
    min_score = min(scores)
    avg_score = sum(scores) / len(scores)
    return max_score, min_score, avg_score


# 3. 成绩对应的评级人数统计
def count_grade(scores):
    grade_counts = {"A": 0, "B": 0, "C": 0, "D": 0, "不及格": 0}
    for score in scores:
        if score >= 90:
            grade_counts["A"] += 1
        elif score >= 80:
            grade_counts["B"] += 1
        elif score >= 70:
            grade_counts["C"] += 1
        elif score >= 60:
            grade_counts["D"] += 1
        else:
            grade_counts["不及格"] += 1
    return grade_counts


# 4. 展示总体报告
def display_result(scores):
    print("\n📊 --- 总体成绩分析报告 ---")
    print(f"当前成绩列表: {scores}")

    max_s, min_s, avg_s = list_score(scores)
    print(f"最高分: {max_s} \t 最低分: {min_s} \t 平均分: {avg_s:.2f}")

    print("\n📈 --- 评级分布 ---")
    counts = count_grade(scores)
    for grade, count in counts.items():
        print(f"等级 {grade}: {count} 人")
    print("--------------------------\n")


# 主菜单
def main():
    # 🔥 核心改动：在主程序里准备一个空列表，用来贯穿所有操作
    global_scores = []

    while True:
        print("""
        ====== 学生成绩分析系统 ======
        1. 输入成绩 (可输入多个空格隔开)
        2. 分析成绩 (最高/最低/平均)
        3. 评级统计 (A/B/C/D人数)
        4. 总体报告
        5. 退出
        ===========================
        """)
        choice = input("请选择操作(1-5):")

        if choice == "1":
            # 把 input_scores 返回的结果赋值给 global_scores
            global_scores = input_scores()

        elif choice == "2":
            # 增加一个容错：如果没有成绩，先提示用户录入
            if not global_scores:
                print("❌ 请先选择 1 录入成绩！")
            else:
                # 把列表传给你写的 list_score，并接收返回的三个值
                mx, mn, avg = list_score(global_scores)
                print(f"最高分: {mx}, 最低分: {mn}, 平均分: {avg:.2f}")

        elif choice == "3":
            if not global_scores:
                print("❌ 请先选择 1 录入成绩！")
            else:
                # 接收 count_grade 返回的字典并打印
                counts_dict = count_grade(global_scores)
                print(counts_dict)

        elif choice == "4":
            if not global_scores:
                print("❌ 请先选择 1 录入成绩！")
            else:
                display_result(global_scores)

        elif choice == "5":
            print("感谢使用，再见！")
            break
        else:
            print("操作无效，请输入1,2,3,4或5！")


if __name__ == '__main__':
    main()