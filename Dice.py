#Import modules random and time from the python library
import random
import time
#Import the file created for checking user permissions
import Auth_score
from Auth_score import admin_usr

#Setting 4 variables as zero for later
p1_wins = 0

p2_wins = 0

score1total = 0

score2total = 0

#Used at the end to save the scores and names of the players who won
def winners():
    #Opens the file where score was just saved
    ClassA = open("Winners.txt", "r")
    ClassA = ClassA.read()
    print(ClassA)
    # Splits into a dictionary using the character to differenciate
    items = ClassA.split(':')
    print(items)

    
#This is used if at the end, the scores of players are the same
def undicided ( score1total, score2total):
    #Keeps looping while Player 1 wins is equal to player's 2 wins
    while score1total == score2total:
      roll0 = random.randint(1,6)
      roll1 = random.randint(1,6)
      if roll0 > roll1:
         print("P1 wins!")
         score1total = score1total +1
         out_file = open("Winners","a+")
         out_file.write( "Player1" + ":" + int(score1total) + ":" )
         winners()

      elif roll0 == roll1:
         undicided( score1total, score2total)

      else:
         print("P2 Wins!")
         score2total = score2total +1
         out_file = open("Winners","a+")
         out_file.write( "Player2" + ":" + int(score2total) + ":" )
         winners()

#Importing from file containing user permissions
#To be admin, user's file needs to contain "1" inside
while admin_usr != 1:
    Auth_score.input_usr()
    from Auth_score import admin_usr

#Repeat for 5 times for five games
for x in range(1,5):
   #Rolling Player 1's dice
   p1_dice = random.randint(1,6)
   p1_2_dice = random.randint(1,6)

   #Rolling Player 2's dice
   p2_dice = random.randint(1,6)
   p2_2_dice = random.randint(1,6)

   #Added their totals to be compared later
   p1_total = p1_dice + p1_2_dice
   p2_total = p2_dice + p2_2_dice

   print("Player 1 rolls...")
   time.sleep(2)
   print("Player 1 rolls a total of:",p1_total)

   if (p1_total % 2) == 0:
      print("It's even! Add 10 points!")
      p1_total2 = p1_total + 10
   else:
      print("It's odd! Subtract 5 points!")
      p1_total2 = p1_total - 5

   time.sleep(1)

   print("Player 2 rolls...")
   time.sleep(2)
   print("Player 2 rolls a total of:",p2_total)

   if (p2_total % 2) == 0:
      print("It's even! Add 10 points!")
      p2_total2 = p2_total + 10
   else:
      print("It's odd! Subtract 5 points!")
      p2_total2 = p2_total - 5


   print("Player 1's total is:",p1_total2)
   print("Player 2's total is:",p2_total2)

   #If either total falls bellow 0
   if p1_total2 < 0:
      p1_total2 = 0

   elif p2_total2 < 0:
      p2_total2 = 0


   score1total = p1_total2 + score1total

   score2total = p2_total2 + score2total


   #This is to determine which Player wins
   if p1_total2 > p2_total2:
      print("P1 wins!")
      p1_wins = p1_wins + 1

   elif p1_total2 == p2_total2:
      print("It's a draw!")

   else:
      print("P2 wins!")
      p2_wins = p2_wins + 1

   print("")

print("Player 1 has won",p1_wins,"game/s!")
print("Player 2 has won",p2_wins,"game/s!")


if score1total > score2total:
   print("P1 wins the game!")
   out_file = open("Winners","a+")
   out_file.write( "Player1" + ":" + str(score1total) + ":" )

elif score1total == score2total:
   print("Roll one dice to decide!")
   undicided( p1_wins, p2_wins)


else:
   print("P2 wins the gane!")
   out_file = open("Winners","a+")
   out_file.write( "Player2" + ":" + str(score2total) + ":" )


winners()
