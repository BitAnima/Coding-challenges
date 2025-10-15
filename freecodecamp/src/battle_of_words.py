"""
Battle of Words
Given two sentences representing your team and an opposing team,
where each word from your team battles the corresponding word from the opposing team,
determine which team wins using the following rules:

The given sentences will always contain the same number of words.
Words are separated by a single space and will only contain letters.
The value of each word is the sum of its letters.
Letters a to z correspond to the values 1 through 26. For example, a is 1, and z is 26.
A capital letter doubles the value of the letter. For example, A is 2, and Z is 52.
Words battle in order: the first word of your team battles the first word of the opposing team, and so on.
A word wins if its value is greater than the opposing word's value.
The team with more winning words is the winner.
Return "We win" if your team is the winner, "We lose" if your team loses, and "Draw" if both teams have the same number of wins.
"""

"""
Calcula el valor de cada palabra
Crea una función para calcular el valor de una palabra:"""

def calculate_word_value(word):

    sum_letters  = 0

    for letter in word:
        base_value = ord(letter.lower()) - ord('a') + 1
        if letter.islower():
            sum_letters += base_value

        if letter.isupper():
            sum_letters += base_value * 2

    return sum_letters


def battle(our_team, opponent):
    our_words = our_team.split()
    opponent_words = opponent.split()

    our_values = [calculate_word_value(word) for word in our_words]
    opponent_values = [calculate_word_value(word) for word in opponent_words]

    print(our_values, opponent_values)

    wins = 0

    for word1, word2 in zip(our_values, opponent_values):
        if word1 > word2:
            wins += 1
        elif word1 < word2:
            wins -= 1

    if wins > 0:
        print("We win")
        return "We win"
    elif wins < 0:
        print("We lose")
        return "We lose"
    else:
        print("Draw")
        return "Draw"

battle("Hello world", "hello world")