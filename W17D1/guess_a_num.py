import random

num_tries = 0
answer = random.randint(1,20)
name = input("please enter your name: ")
number = input(f"well, {name}, I'am thinking a number between 1 and 20: ")
while num_tries <= 6:
  num_tries += 1
  if int(number) > answer:
    print("try a smaller number")
  elif int(number) < answer:
    print("try a larger number")
  elif int(number) == answer:
    break
  number = input("take a guess ")
if answer == int(number):
  print(f"{name}, you guessed correctly via {num_tries} tries!")
else:
  print(f"Sorry, {name}. You could not guess my number {answer}")
