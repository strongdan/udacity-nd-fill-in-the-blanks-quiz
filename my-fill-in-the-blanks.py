# Game has 3 or more levels and each level contains 4 or more blanks to fill in
sentences = [
"_1_ is a programming language named for Monty Python's Flying Circus. A _2_ is an immutable list of characters surrounded by quotes. A _3_ is an unordered collection of items of any type while a _4_ is an ordered collection of a single type.",
"A _1_ is an associative array that can contain any Python _2_ type. The print() function and integer division are key differences between Python _3_ and _4_",
"Python supports _1_ programming with classes and multiple _2_. Python _3_ are defined by creating a function and inheriting from a _4_, eg. variable = Class(parameters)"]

answers = [['Python','string','list','array'],['dictionary', 'data', '2', '3'],['object-oriented', 'inheritance','objects','class']]

sentence_with_blanks = ""

def level_selector(level):
    if level == 1
        return 'Level is: Easy'
    elif level == 2
        return 'Level is: Medium'
    elif level == 3
        return 'Level is: Hard'
    else:
        return sentences[level - 1]

def sentence_play(level):
    lvl = level
    i = 1
    while i < 4:
        if i == 1:
            blank = 'first'
        elif i == 2:
            blank = 'second'
        elif i == 3:
            blank = 'third'
        else:
            blank = 'fourth'
        blank_input = raw_input("Please fill in the " + blank + " blank")
        if correct_answer(lvl, i, blank_input):
             # When player guesses correctly, new prompt shows with correct answer in the
             # previous blank and a new prompt for the next blank
            display_sentence(lvl, i, blank_input):
            print 'Nice work! You got that one. Now on to the next blank..."
            i += 1
        else:
            # When player guesses incorrectly, they are prompted to try again
            print 'Not quite. Try again.'
    print "Congrats! You got them all right!"
    play_game()
        

# Checks if a answer is correct
def correct_answer(level, blank_number, answer):
    if str(answer) == answers[level - 1][blank_number - 1]:
        return True
    else:
        return False

def display_sentence(level, position, blank_input):
    sentence = sentences[level]
    sentence.split(" ")
    for word in sentence:
        if word == '_' + position + '_':
            word = blank_input
            sentence = " ".join(sentence)
        else:
            sentence = " ".join(sentence)
    print sentence
            
# prompt user and play through game
def play_game():
    # Start game with a prompt to the user
    print "Welcome to the fill-in-the-blanks quiz"

    # Immediately after running the program, user is prompted to select a difficulty level
    # from easy / medium / hard
    first_input = raw_input("Please select a level to begin at: (1) Easy (2) Medium or (3) Hard. Type 'Q' to quit")

    while first_input != 'Q':
        # Once a level is selected, game displays a fill-in-the-blank and a prompt to fill
        # in the first blank.
        level_selector(first_input)
        level = first_input
        sentence_play(level)
        play_game()
        
play_game()
