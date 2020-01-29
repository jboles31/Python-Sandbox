import random

print("...rock...")
print("...paper...")
print("...scissors...")

player1 = input("(enter Player 1's choice): ")

r = random.randint(1, 3)
if r == 1:
  r = "rock"
elif r == 2:
  r = "paper"
elif r == 3:
  r = "scissors"
print('Computer played ', r)

print("SHOOT!")

if player1 == r:
  print('TIE')
elif player1 == "rock":
  if r == "scissors":
    print('player1 wins!')
  elif r == "paper":
    print('The computer wins!')
elif player1 == "paper":
  if r == "rock":
    print("player1 wins!")
  elif r == "scissors":
    print('The computer wins!')
elif player1 == "scissors":
  if r == "paper":
    print("player1 wins!")
  elif r == "rock":
    print('The computer wins!')
else:
  print("something went wrong")

