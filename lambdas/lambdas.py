
# Lambdas
# similar to anonymous functions
# has to be one line

def square(num):
  return num*num

print(square(5))

# NOT USUALLY STORED IN A VARIABLE

square2 = lambda num: num * num

add = lambda a,b: a + b

print(square2(7))
print(add(5,4))

# COMMON USE CASE

# main use is for using a function as a parameter in another function