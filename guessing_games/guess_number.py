from random import randint

number = randint(1,10)
msg = None

while True:
  msg = int(input("Guess a number between 1 and 10: "))
  if msg < number:
    print("Too low, try again")
  elif msg > number:
    print("Too high, try again!")
  else:
    print("You guessed it! You win!")
    play_again = input("Do you want to play again? (y/n)")
    if play_again == "y":
      number = randint(1,10)
      msg = None
    else:
      print("Thanks for playing")
      break


      
    



