import random

Name = "Ray"
Question = "Do you like candy?" 
answer = "Yes" or "No"
random_number = random.randint(1, 10)
print()

if random_number == 1:
  answer = "Yes - definitely"
elif random_number == 2:
  answer = "It is decidedly so"
elif random_number == 3:
  answer = "Without a doubt"
elif random_number == 4:
  answer = "Reply hazy, try again"
elif random_number == 5:
  answer = "Ask again later"
elif random_number == 6:
  answer = "Better not tell you now"
elif random_number == 7:
  answer = "My sources say no"
elif random_number == 8:
  answer = "Outlook not so good"
elif random_number == 9:
  answer = "Very doubtful"
elif random_number != (1,10):
  answer = "Error"
elif random_number == 10:
  answer = "R U Crazy!"

print(f"{[Name]} asks: {[Question]}")
print(answer)
print(f"Magic 8-Ball's answer: {answer}")
print(Name + " asks: " + Question)
print("Magic 8 Ball's answer: " + answer)
