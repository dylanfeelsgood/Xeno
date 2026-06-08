#求和
def add(a,b):
    return a+b
result = add(1,2)
print(result)

#求平均值
def avg(a,b):
    return (a+b)/2
result = avg(5.5,4)
# print(f"{result:.2f}") #方法一  保留两位数 print(f"{变量名:.2f}")
# print("{:.2f}".format(result)) #方法三  传统的 .format() 方法
round_result = round(result,2)
print(round_result) #方法二  使用 round() 函数

#求最大值
def max_value(a,b):
    return max(a,b)
result = max_value(6,9)
print(result)

def min_value(a,b):
    return min(a,b)
result = min_value(6,9)
print(result)
