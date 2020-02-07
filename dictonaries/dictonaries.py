
example = dict(key = 'value')
print(example['key'])

jordan = {
  'lastname': 'Boles',
  'age': 24
}

for value in jordan.values():
  print(value)

for keys in jordan.keys():
  print(keys)

for key,value in jordan.items():
  print(f'key is {key}, value is {value}')

# searching for existence of a key
print('age' in jordan)

# searching for existance of a vlaue
print('Boles' in jordan.values())
print('Jordan' in jordan.values())


# DICTIONARY METHODS

# clear()
clear_example = {
  'a': 'b'
}
clear_example.clear()
print(f'Clear Example: {clear_example}')

# copy()
copy = jordan.copy()
print('COPY')
print(copy == jordan)
print(copy is jordan)

# fromkeys()
# creates key-value pairs from CSVs
# assignes multiple keys the same value
key_example = {}.fromkeys(['a','b'], ['unknown', 'known'])
print(key_example)

# get()
#  retrieves the value of a given key in an object
# returns none instead of KeyError for nonexistent keys!!!!
print('GET')
print(jordan.get('lastname'))
print(jordan.get('favorite_show'))
