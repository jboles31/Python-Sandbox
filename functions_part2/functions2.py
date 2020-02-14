
# Star Arguments
# allows an unspecified amount of arguments
# arguments are put in to a tuple
# args are iterable 

def all_sum(*args):
  total = 0
  for num in args:
    total += num
  return total

print(all_sum(4,5,6))
print(all_sum(4,5,6,7,8,9,10))


# Keyword Arguments
# 

def fav_colors(**kwargs):
  for person, color in kwargs.items():
    print(f"{person}'s fav color is {color}'")

fav_colors(colt="purple", ruby="red", ethel="teal")
fav_colors(colt="purple", ruby="red", ethel="teal", ed="blue")
fav_colors(colt="purple")

# Exercise in Keyword Arguments

def combine_words(word, **kwargs):
  if "prefix" in kwargs:
    return kwargs['prefix'] + word
  elif "suffix" in kwargs:
    return word + kwargs['suffix']
  return word


print(combine_words('child', prefix="man"))
print(combine_words('child', suffix="ish"))


# ORDERING OF PARAMETS

# 1. - parameters
# 2. - *args
# 3. - default parameters
# 4. - **kwargs

# Tuple Unpacking

# Star Args will create a tuple of all the args given. We must unpack the tuple, made from the list provided as an arg
# When you have a function that accepts star args, but is passed a list not multiple args

def sum_all_values(*args):
  total = 0
  for num in args:
    total += num
  print(total)

nums = [1,2,3,4]

# pass list with a star in front
sum_all_values(*nums)



# Dictionary Unpacking

# Use Keyword Args to unpack a dictionary

def display_names(first, second):
  print(f'{first} says hello to {second}')

names = {'first': 'Jordan', 'second': 'Evan'}

display_names(**names)