'''
write program ehich sccepts the user's frist and last name and print them in reverse
order with a space between them
'''

"""
my answer
first_name = input('Enter first name:')
last_name = input('Enter your last name:')

print(last_name +' '+ first_name)
"""

first_name = input('Enter first name:')
last_name = input('Enter your last name:')

reversed_name = "{} {}".format(last_name, first_name +'さんこんにちは')
print(reversed_name)
