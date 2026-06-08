name = input("请输入姓名:")

print(f"{len(name)}")  # 字符串的长度

upper_name = name.upper()  # 字符串的大写字母
print(upper_name)

lower_name = name.lower()  # 字符串的小写字母
print(lower_name)

# split_name = name.split()
# print(split_name)

""" 默认情况：按空格切
name = "张三 李四 王五"
print(name.split())  
输出结果是一个列表: ['张三', '李四', '王五']

进阶用法：按指定的符号切
data = "apple,banana,orange"
print(data.split(",")) 
输出结果: ['apple', 'banana', 'orange']"""


# strip_name = name.strip()
# print(strip_name)

""" 注意字符串两端有很多无用的空格和换行
name = "   \n 小明   "

print("清理前:", name)
清理前:    
  小明   

print("清理后:", name.strip())
清理后: 小明

中间的空格不会被清理
test_name = "  小   明  "
print("清理中间有空格的名字:", test_name.strip())
清理中间有空格的名字: 小   明"""


# scores = [90,85,77,66]
# max_score = max(scores)
# min_score = min(scores)
# avg_score = sum(scores)/len(scores)
# print(max_score,min_score,avg_score)

#成绩最大值 最小值 平均值函数
def list_scores(scores):
    max_score = max(scores)
    min_score = min(scores)
    avg_score = sum(scores) / len(scores)
    return max_score,min_score,avg_score

scores = [90,87,92,85,77,66,56,44]
max_score,min_score,avg_score = list_scores(scores)
print(max_score,min_score,avg_score)

#等级统计
grades = {"A":0,"B":0,"C":0,"D":0,"不及格":0}
for score in scores:
    if score >= 90 and score <= 100:
        grades["A"] += 1
    elif score >= 80 and score < 90:
        grades["B"] += 1
    elif score >= 70 and score < 80:
        grades["C"] += 1
    elif score >= 60 and score < 70:
        grades["D"] += 1
    else:
        grades["不及格"] +=1
print(grades)
