# Game has 3 or more levels and each level contains 4 or more blanks to fill in

sentence_lvl_one = "A ___ is an immutable list of characters surrounded by quotes"
answer_lvl_one = ['string']
sentence_lvl_two = "A ___ is an unordered collection of items of any type while a ___ is an ordered collection of a single type."
answers_lvl_two = ['list','array']
sentence_lvl_three = "A ___ is an associative array that can contain any Python ___ type"
answers_lvl_three = ['Dictionary', 'data']
sentence_lvl_four = "Python supports ___ programming with classes and multiple ___"
answers_lvl_four = ['object-oriented', 'inheritance']

sentence_with_blanks = ""

def level_selector(level):
    if level == 1:
        return sentence_lvl_1
    elif level == 2:
        return sentence_lvl_2
    elif level == 3:
        return sentence_lvl_3
    elif level == 4:
        return sentence_lvl_1
    else:
        return "Please enter a valid number from 1-4"

# Checks if a answer is correct
def correct_answer_one(level, answer):
    if level == 1:
        if answer == answer_lvl_one[0]:
            return True
        else:
            return False
    if level == 2:
        if answer == answer_lvl_two[0]:
            return True
        else:
            return False
    if level == 3:
        if answer == answer_lvl_three[0]:
            return True
        else:
            return False
    if level == 4:
        if answer == answer_lvl_four[0]:
            return True
        else:
            return False
    else:
        return "Error"

def correct_answer_two(sentence, answer, answers):
    if sentence == sentence_lvl_2:
        if answer == answers[1]:
            return True
        else:
            return False
    elif sentence == sentence_lvl_3:
        if answer == answers[1]:
            return True
        else:
            return False
    elif sentence == sentence_lvl_4:
        if answer == answers[1]:
            return True
        else:
            return False
    else:
        return "Error - that wasn't a valid sentence"
    
# prompt user and play through game
def play_game():
    # Start game with a prompt to the user
    print "Welcome to the fill-in-the-blanks quiz"

    # Immediately after running the program, user is prompted to select a difficulty level from easy / medium / hard
    level_input = raw_input("Please select a level to begin at: (1) Easy (2) Medium or (3) Hard")

    # Once a level is selected, game displays a fill-in-the-blank and a prompt to fill in the first blank.
    level_selector(input)
    blank_one_input = raw_input("Please fill in the first blank")
    correct_answer_one(level_input, blank_one_input)

    # When player guesses correctly, new prompt shows with correct answer in the previous blank and a new prompt for the next blank
    print "That's right. 

# When player guesses incorrectly, they are prompted to try again

# If player passes level one, move on to level 2

# If player passes level one, move on to level 3

# If player passes level one, move on to level 4
