
for num in range(1,21):
  if num == 13 or num == 4:
    print(f"{num} is unlucky")
  elif num % 2 == 0:
    print(f"{num} is even")
  else:
    print(f"{num} is odd")