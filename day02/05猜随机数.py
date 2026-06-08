import random
from unittest import result

random_number = random.randint(0,20)
print("随机数已经生成，请猜猜看")

while True:
 guess_number = int(input("Enter your guess number: "))
 if guess_number < random_number:
     print("Your guess is too low")
 elif  guess_number > random_number:
      print("Your guess is too high")
 else:
      print("You guessed the number")
      break
