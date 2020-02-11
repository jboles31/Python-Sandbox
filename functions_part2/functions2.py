
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