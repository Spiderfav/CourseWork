import Auth_score
import sys

#from Auth_score import user

#print(user)


Auth_score.input_usr()

print("Player 1:")
from Auth_score import admin_usr

if admin_usr == 1:
    print("Go ahead, you are authorised.")
    print(admin_usr)
    #user = player1

else:
    print("Not authorised to play.")
    print(admin_usr)
    print("")
    sys.exit()


Auth_score.input_usr()

print("Player 2:")
from Auth_score import admin_usr

if admin_usr == 1:
    print("Go ahead, you are authorised.")
    print(admin_usr)
    #user = player2

else:
    print("Not authorised to play.")
    print(admin_usr)
    print("")
    sys.exit()

Songs = open("SongsAndArtists.txt", "r")
Songs = Songs.read()
# Splits into a dictionary using the character to differenciate
items = Songs.split(',')
item1 = items[0]
item1.replace('a'+'e'+'i'+'o'+'u', '--')
print(item1)
