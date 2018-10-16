list_char = "AEIOU"
Songs = open("Songs.txt", "r")
Artists = open("Artists.txt", "r")
Songs = Songs.read()
#Splits into a dictionary using the character to differenciate
items = Songs.split(',')
print(items)
for list_char in items:
    items[1].append("-")
    print(items)





##item1 = str(items[0])
##item1.replace('H','-')
##print(item1)
##mainStr = "Hello, This is a sample string"
##otherStr = mainStr.replace('s' , 'X') 
##print(otherStr)
##for character in secretWord:
##        guess_word.append("-")
