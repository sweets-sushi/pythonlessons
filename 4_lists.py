shopping_list = ['apples', 'grapes', ' nuts', 'milk']
# addning to the list

shopping_list.append('ham')

print(shopping_list)

#remove item from the shopping_list
shopping_list.remove('grapes') #removes specific item

shopping_list.pop() #removes the last item in the list

print(shopping_list)


print(len(shopping_list)) #gives us length of a list

print(shopping_list[-1])

#slicing a shopping_list
print(shopping_list[0:2])

print(shopping_list[0:])
