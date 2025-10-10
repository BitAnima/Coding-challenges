"""
Character Battle
Given two strings representing your army and an opposing army, each character from your army battles the character at the same position from the opposing army using the following rules:

Characters a-z have a strength of 1-26, respectively.
Characters A-Z have a strength of 27-52, respectively.
Digits 0-9 have a strength of their face value.
All other characters have a value of zero.
Each character can only fight one battle.
For each battle, the stronger character wins. The army with more victories, wins the war. Return the following values:

"Opponent retreated" if your army has more characters than the opposing army.
"We retreated" if the opposing army has more characters than yours.
"We won" if your army won more battles.
"We lost" if the opposing army won more battles.
"It was a tie" if both armies won the same number of battles."""

def strength(character):
    if 'a' <= character <= 'z':
        return ord(character) - ord('a') + 1
    elif 'A' <= character <= 'Z':
        return ord(character) - ord('A') + 27
    elif character.isdigit():
        return int(character)
    else:
        return 0
    

def battle(my_army, opposing_army):

    wins1 = 0
    wins2 = 0

    if len(my_army) > len(opposing_army):
        result= "Opponent retreated"
        print(f"{result}")
        return result
    
    elif len(my_army) < len(opposing_army):
        result= "We retreated"
        print(f"{result}")
        return result
 

    for character1, character2 in zip(my_army, opposing_army):
        print(f"{character1} vs {character2}")
        strength1 = strength(character1)
        strength2 = strength(character2)

        if strength1 > strength2:
            wins1 += 1
        elif strength2 > strength1:
            wins2 += 1
    

    if wins1 > wins2:
        result= "We won"
    elif wins2 > wins1:
        result= "We lost"
    else:
        result= "It was a tie"

    print(f"{result}")
    return result        


battle("Hello", "World") # "We lost".
battle("pizza", "salad") # "We won".
battle("C@T5", "D0G$") # "We won".
battle("kn!ght", "orc") # "Opponent retreated".
battle("PC", "Mac") # "We retreated".
battle("Wizards", "Dragons") # "It was a tie".
battle("Mr. Smith", "Dr. Jones") # "It was a tie".
