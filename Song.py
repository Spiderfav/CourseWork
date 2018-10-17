#list_char = ["A","E","I","O","U"]
import random

def remove():
    test = items[i].replace("A","-")
    #print(test)

    test0 = test.replace("E","-")
    #print(test0)

    test1 = test0.replace("I","-")
    #print(test1)

    test2 = test1.replace("O","-")
    #print(test2)

    test3 = test2.replace("U","-")
    print(test3)


Songs = open("Songs.txt", "r")
Artists = open("Artists.txt", "r")
Songs = Songs.read()
items = Songs.split(',')
i = random.randint(0,1)
remove()
Artists = Artists.read()
items = Artists.split(',')
remove()




