#tuples are immutable objects

name = ('matt', 'john', 'mark', 'luke')


furniture = ('chairs',)

# getting elements is the same as list
print(name[0])

print(name[0:3])

#updating tuples

items = name + furniture
print(items)

#deleting tuples

del items
print(items)
