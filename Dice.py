import random
import time

p1_dice = random.randint(1,6)
p1_2_dice = random.randint(1,6)

p2_dice = random.randint(1,6)
p2_2_dice = random.randint(1,6)

p1_total = p1_dice + p1_2_dice
p2_total = p2_dice + p2_2_dice

print("Player 1 rolls...")
time.sleep(2)
print("Player 1 rolls a total of:",p1_total)
time.sleep(1)
print("Player 2 rolls...")
time.sleep(2)
print("Player 2 rolls a total of:",p2_total)

if (p1_total % 2) == 0:
   print("It's even! Add 10 points!")
   p1_total2 = p1_total + 10
else:
   print("It's odd! Subtract 5 points!")
   p1_total2 = p1_total - 5


print(p1_total2)
