dict = {
'nuts': 5, 'grapes': 10, 'milk': 2

}
#get an item to dictionary
milk = dict.get('milk') #option1
milk = dict['milk'] #option2

print(milk)

#add item to the dictionary

dict['cheese'] = 4
print(dict)

#remove item from the dictionary
cheese = dict.popitem() #return the tuple of removed key
milk2 = dict.pop('milk') #return the value of removed key
print(dict)
#print(cheese)
print(milk2)
