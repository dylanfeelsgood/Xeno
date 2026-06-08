import random
from unittest import result

random_number = random.randint(0,20)
print("随机数已经生成，请猜猜看")

# while True:
#  guess_number = int(input("Enter your guess number: "))
#  if guess_number < random_number:
#      print("Your guess is too low")
#  elif  guess_number > random_number:
#       print("Your guess is too high")
#  else:
#       print("You guessed the number")
#       break

guess_number = None
while guess_number != random_number:
    guess_number = int(input("请输入猜的数字"))
    if guess_number > random_number:
        print("唔，猜大了呢")
    elif guess_number < random_number:
        print("这次猜小了")
    else:
        print("猜对了，恭喜恭喜")