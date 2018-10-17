#list_char = ["A","E","I","O","U"]
Songs = open("Songs.txt", "r")
Artists = open("Artists.txt", "r")
Songs = Songs.read()
#Splits into a dictionary using the character to differenciate
items = Songs.split(',')
test = items[0].replace("A","-")
print(test)

test0 = test.replace("E","-")
print(test0)

test1 = test0.replace("I","-")
print(test1)

test2 = test1.replace("O","-")
print(test2)

test3 = test2.replace("U","-")
print(test3)




