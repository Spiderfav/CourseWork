list_char = "AEIOU"
Songs = open("Admin.txt", "r")
Songs = Songs.read()
#Splits into a dictionary using the character to differenciate
items = Songs.split(',')
item1 = items[0]
item1.replace('H','-')
print(item1)
