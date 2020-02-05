import random

player_wins = 0
comp_wins = 0
winning_score = int(input("What score do you want to play to?"))

while player_wins < winning_score and comp_wins < winning_score:
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
      player_wins += 1
    else:
      print('The computer wins!')
      comp_wins += 1
  elif player1 == "paper":
    if r == "rock":
      print("Player wins!")
      player_wins += 1
    else:
      print('The computer wins!')
      comp_wins += 1
  elif player1 == "scissors":
    if r == "paper":
      print("Player wins!")
      player_wins += 1
    else:
      print('The computer wins!')
      comp_wins += 1
  else:
    print("something went wrong")
if comp_wins == winning_score:
  print(f"Computer Wins {comp_wins} to {player_wins}")
else:
  print(f"Player Wins {player_wins} to {comp_wins}")


