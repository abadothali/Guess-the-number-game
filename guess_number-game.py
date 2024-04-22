# Guess the nunber game:
import random
randnum=random.randint(1,100)

while True:

  usernum=input("Guess number or quit: ")

  if(usernum=="quit"):
    break

  usernum=int(usernum)
  if(usernum == randnum):
    print("Congratulations! You Guess the number...")
    break

  elif(usernum < randnum):
    print("You chose the small number, You Guess the big number...")

  else:
    print("You chose the big number, You guess the small number...")

print("-----Gama Over-----")