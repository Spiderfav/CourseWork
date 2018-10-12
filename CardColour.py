#Convert the both choices to functions so they can be called instead of being repeated!



import random

#Red beats black, yellow beats Red and black beats Yellow
#Add user authorisation here

card_colours = ["RED","BLACK","YELLOW"]
card_numbers = [1,2,3,4,5,6,7,8,9,10]
used_card_and_numbers = []

print("Let's get started!")

#while number

card_choice = random.randint(0,2)
choice1 = card_colours[card_choice]

numb_choice = random.randint(0,9)
choice2 = card_numbers[numb_choice]
#pop Number of Colour

used_card_and_numbers.extend(p1)
p1 = (choice1,choice2)    

print(p1)

card_choice = random.randint(0,2)
choice1 = card_colours[card_choice]

numb_choice = random.randint(0,9)
choice2 = card_numbers[numb_choice]

used_card_and_numbers.extend(p2)
p2 = (choice1,choice2)

print(p2)

if p1[1] > p2[1]:
    print("P1 wins!")

elif p1[1] == p2[1]:
    if p1[0] == "RED":
        if p2[0] == "BLACK":
            print("P1 Won!")
        else:
            print("P2 Won!")

    elif p1[0] == "BLACK":
        if p2[0] == "YELLOW":
            print("P1 Won!")
        else:
            print("P2 Won!")

    elif p1[0] == "YELLOW":
        if p2[0] == "RED":
            print("P1 Won!")
        else:
            print("P2 Won!")
    
else:
    print("P2 wins!")

print(used_card_and_numbers[])
