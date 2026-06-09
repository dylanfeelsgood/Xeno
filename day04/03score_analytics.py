# 输入成绩列表
def input_scores():
    user_input = input("请输入一组成绩(每个成绩须用空格隔开):")
    str_list = user_input.split()
    scores = []
    for item in str_list:
        try:
          scores.append(float(item))
        except ValueError:
          print(f"无效输入:{item}")
    print(f"成功输入了{len(scores)}个成绩！")
    return scores


# 查询成绩的最大值 最小值 平均值
def list_score_stats(scores):
    max_score = max(scores)
    min_score = min(scores)
    avg_score = sum(scores) / len(scores)
    return max_score, min_score, avg_score


# 成绩对应的评级人数统计
def count_grade(scores):
    grades = {"A": 0, "B": 0, "C": 0, "D": 0, "不及格": 0}
    for score in scores:
        if 90 <= score <= 100:
            grades["A"] += 1
        elif 80 <= score < 90:
            grades["B"] += 1
        elif 70 <= score < 80:
            grades["C"] += 1
        elif 60 <= score < 70:
            grades["D"] += 1
        else:
            grades["不及格"] += 1
    return grades


# 展示菜单
def display_result(scores,stats,grade):
    print("\n --- 总体成绩分析报告 ---")
    print(f"当前成绩列表:{scores}")
    max_score, min_score, avg_score = stats
    print(f"最高分:{max_score},最低分:{min_score},平均分:{avg_score}")
    print("\n ------  评级分布  ------")
    for grade, count in grade.items():
        print(f"等级{grade}:{count}人")
    print("------------------------")


# 主菜单
def main():
    global_scores = []
    while True:
        print("""
        ====== 学生成绩分析系统 ======
        1.输入成绩
        2.分析成绩
        3.评级人数统计
        4.评级分布
        5.退出
        ===========================
        """)
        choice = input("请选择操作(1-5):")
        if choice == "1":
            global_scores = input_scores()
        elif choice == "2":
            if not global_scores:
                print("❌ 当前没有任何成绩数据，请先选择 1 输入成绩！")
            else:
             max_score, min_score, avg_score = list_score_stats(global_scores)
             print(f"最高分:{max_score},最低分:{min_score},平均分:{avg_score}")
        elif choice == "3":
            if not global_scores:
                print("❌ 当前没有任何成绩数据，请先选择 1 输入成绩！")
            else:
             grades = count_grade(global_scores)
             print(f"每个等级人数为:{grades}")
        elif choice == "4":
            if not global_scores:
                print("❌ 当前没有任何成绩数据，请先选择 1 输入成绩！")
            else:
             stats = list_score_stats(global_scores)
             grades = count_grade(global_scores)
             display_result(global_scores,stats,grades)
        elif choice == "5":
            print("感谢使用，再见！")
            break
        else:
            print("操作无效，请输入1,2,3,4或5！")


if __name__ == '__main__':
    main()
