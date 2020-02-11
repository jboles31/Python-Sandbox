
def single_letter_count(string, char):
    return len([x for x in string.lower() if x == char.lower()])

print(single_letter_count('Hello', "h"))
print(single_letter_count('Hello', "z"))
print(single_letter_count('Hello', "l"))


# 

def multiple_letter_count(string):
  result = {char: 0 for char in string}
  print(result)
  for x in string:
    result[x] += 1
  return result

print(multiple_letter_count("awesome"))


# 

def is_palindrome(string):
  stripped = string.replace(" ", "")
  # ^gets rid of whitespace
  return stripped == stripped[::-1]
  # [::-1] reveses order

print(is_palindrome('racecar'))


#

def frequency(collection, item):
    return collection.count(item)

print(frequency([1,2,3,4], 1))


#

def multiply_even_numbers(collection):
    result = 0
    evens = [x for x in collection if x%2 == 0]
    for x in evens:
      if result == 0:
        result = x
      else:
        result = result * x
    return result

print(multiply_even_numbers([2,3,4,5,6]))

# my solution is chunkier than his but it accounts for a given list that has no even numbers, by instantiating
# result at 0 instead of 1


#

def intersection(list1, list2):
# using sets alows us the comparison of &
  return [val for val in set(list1) & set(list2)]

print(intersection([1,2,3,4], [3,4,5]))

# return [val for val in list1 if val in list2]


# Callback function

def partition(list1, fn):
  truth = []
  false = []
  for val in list1:
    if fn(val):
      truth.append(val)
    else:
      false.append(val)
  return [truth, false]

def isEven(num):
  return num % 2 == 0

print(partition([1,2,3,4], isEven))