
# map(fn, item)

nums = [1,2,3,4]

doubles = list(map(lambda num : num*2, nums))
print(doubles)



names = [{'first': 'Jordan', 'last': 'Boles'},{'first':'Bill', 'last': 'Bob'}]

first_names = list(map(lambda x: x['first'], names))

print(first_names)


# filter(fn, item)

l = [1,2,3,4]

evens = list(filter(lambda x : x % 2 == 0, l))

print(evens)