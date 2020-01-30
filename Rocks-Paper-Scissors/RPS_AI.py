import random

print("...rock...")
print("...paper...")
print("...scissors...")

player1 = input("(enter Player's choice): ").lower()

r = random.randint(1, 3)
if r == 1:
  r = "rock"
elif r == 2:
  r = "paper"
else:
  r = "scissors"
print(f'Computer played {r}')

print("SHOOT!")

if player1 == r:
  print('TIE')
elif player1 == "rock":
  if r == "scissors":
    print('Player wins!')
  else:
    print('The computer wins!')
elif player1 == "paper":
  if r == "rock":
    print("Player wins!")
  else:
    print('The computer wins!')
elif player1 == "scissors":
  if r == "paper":
    print("Player wins!")
  else:
    print('The computer wins!')
else:
  print("something went wrong")

