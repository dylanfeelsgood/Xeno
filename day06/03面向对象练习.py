# 1. 创建 Student 类
class Student:
    # 初始化方法（构造函数）：定义这个对象出生时带有什么属性
    def __init__(self, name, scores):
        self.name = name
        self.scores = scores  # 期望传入一个成绩列表，如 [90, 85, 88]

    # 方法：计算平均分
    def avg_score(self):
        if not self.scores:  # 防御性编程：防止没有成绩时除以 0 报错
            return 0
        return sum(self.scores) / len(self.scores)

    # 方法：判断等级
    def grade(self):
        avg = self.avg_score()  # 在类内部，方法之间互相调用也要加上 self.
        if avg >= 90:
            return "A"
        elif avg >= 80:
            return "B"
        elif avg >= 70:
            return "C"
        elif avg >= 60:
            return "D"
        else:
            return "不及格"

# 2. 创建 3 个 Student 对象，放到列表里
s1 = Student("小明", [95, 90, 92])
s2 = Student("小红", [75, 80, 82])
s3 = Student("小刚", [60, 55, 65])

student_list = [s1, s2, s3]

# 3. 用列表推导式找出所有平均分 >= 80 的学生名字
# 语法复习：[想要的结果 for 遍历的元素 in 列表 if 满足的条件]
excellent_students = [student.name for student in student_list if student.avg_score() >= 80]

print("--- 基础任务测试 ---")
print(f"小明的平均分: {s1.avg_score():.2f}, 等级: {s1.grade()}")
print(f"平均分大于等于80的优秀学生有: {excellent_students}")


# 挑战：创建一个 Classroom 类
class Classroom:
    def __init__(self):
        # 一个班级刚创建时，里面是空的，准备装 Student 对象
        self.students = []

    # 方法：添加学生
    def add_student(self, student):
        self.students.append(student)
        print(f"✅ 成功将 {student.name} 加入班级！")

    # 方法：班级平均分
    def class_avg(self):
        if not self.students:
            return 0

        # 把班里所有学生的平均分加起来，除以总人数
        total_score = sum(student.avg_score() for student in self.students)
        return total_score / len(self.students)

    # 方法：寻找最高分学生
    def top_student(self):
        if not self.students:
            return None

        # 🔥 高能技巧：还记得你在搜索系统里用过的 lambda 吗？
        # 这里用 max() 函数，并告诉它：请按照每个学生的 avg_score() 来比大小！
        best = max(self.students, key=lambda s: s.avg_score())
        return best


print("\n--- 挑战任务测试 ---")
# 创建一个班级
my_class = Classroom()

# 把之前创建的学生加进班级
my_class.add_student(s1)
my_class.add_student(s2)
my_class.add_student(s3)

# 测试班级平均分
print(f"\n📊 班级总平均分: {my_class.class_avg():.2f}")

# 测试最高分学生
best_student = my_class.top_student()
if best_student:
    print(f"👑 班级第一名是: {best_student.name}，平均分高达 {best_student.avg_score():.2f} 分！")