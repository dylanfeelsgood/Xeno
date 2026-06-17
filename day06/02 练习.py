nums = [1,2,2,3,3,3,4,4,4,4]
print(list(set(nums)))

skills_a = {"Python", "SQL", "Excel"}
skills_b = {"Python", "SQL", "Go"}

print(skills_a & skills_b)
print(skills_a | skills_b)
print(skills_a - skills_b)

fruits = {"apple", "orange", "cherry"}
print(f"现在有这些：",fruits)
fruits.add("banana")
print(f"新增香蕉后：",fruits)
fruits.discard("apple")
print(f"删除苹果后：",fruits)

# 1. 创建一个包含 3 个 Python 知识点的元组
knowledge_points = ("列表推导式", "装饰器", "上下文管理器")
print("元组内容:", knowledge_points)

# 2. 尝试修改元组 —— 下面这行会引发 TypeError
# knowledge_points[0] = "生成器"  # TypeError: 'tuple' object does not support item assignment

# 3. 写一个返回 (最大值, 最小值) 的函数，并用解包接收
def max_min(numbers):
    """返回序列中的最大值和最小值"""
    return max(numbers), min(numbers)

data = [7, 2, 9, 1, 5]
maximum, minimum = max_min(data)   # 解包接收
print(f"最大值: {maximum}, 最小值: {minimum}")

# 1. 用列表推导式生成 1-20 的偶数列表
squares = [x for x in range(1,21) if x % 2 == 0]
print(squares)

#2. 给定 words = ["Python", "AI", "Transformer", "GPU", "RAG"]
#    用列表推导式筛选出长度大于3的词
words = ["Python", "AI", "Transformer","GPU","RAG"]
word_len = [word for word in words if len(word) > 3]
print(word_len)

## 3. 用字典推导式把上面的词变成 {词: 长度} 的字典
words = ["Python", "AI", "Transformer","GPU","RAG"]
word_lenlen = {word: len(word) for word in words}
print(word_lenlen)

# 4. 挑战：用列表推导式重写你Day02的累加——
total = sum([i for i in range(0,101)])
# for i in range(101):
#     total += i
# print(f"此时 i的值为{i},累加后 total={total}")
print("最终的总和是:", total)

#5. 求1+2+...+100的结果（提示：sum() + 列表推导式）
all_total = sum(range(0,101))
print("最终的总和是:", all_total)