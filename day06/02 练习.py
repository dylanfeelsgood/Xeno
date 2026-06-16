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