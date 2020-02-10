from random import random

def say_hi():
  print('Hi!')

say_hi()

def flip_coin():
  r = random()
  if r > 0.5:
    return "heads"
  else:
    return "tails"

print(flip_coin())

def generate_evens():
    return [x for x in range(1,50) if x%2 == 0]

# KEYWORD ARGS
# if you use the keywords when providing argument, order doesn't mattter

def exponential(num, power):
  return num**power

print(f"Exponent {exponential(power=3, num=2)}")

# GLOBAL SCOPE

total = 10

def increment():
  global total
  total += 1
  return total

print(increment())
print(increment())
print(increment())

# NON-LOCAL SCOPE
# lets you modify a parents variable in child function

def outer():
  count = 0
  def inner():
    nonlocal count
    count += 1
    return count
  return inner()

print(f"NONLOCAL SCOPE {outer()}")


# DOCUMENTING FUNCTIONS

def say_hello():
  """A simple function explanation that can be accessed with .__doc__"""
  return "Hello"

print(say_hello.__doc__)
