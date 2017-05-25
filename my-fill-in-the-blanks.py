# Game has 3 or more levels and each level contains 4 or more blanks to fill in

sentence_level_1 = "A ___ is an immutable list of characters surrounded by quotes" answers = ['string']
sentence_level_2 = "A ___ is an unordered collection of items of any type while a ___ is an ordered collection of a single type." # answers = ['list','array']
sentence_level_3 = "A ___ is an associative array that can contain any Python ___ type" # answers = ['Dictionary', 'data']
sentence_level_4 = "Python supports ___ programming with classes and multiple ___" # answers = [object-oriented', 'inheritance']

sentence_with_blanks = ""

# Checks if a answer is correct
def ans_in_pos(word, parts_of_speech):
    for pos in parts_of_speech:
        if pos in word:
            return pos
    return None

# Start game with a prompt to the user
print "Welcome to the fill-in-the-blanks quiz")

# Immediately after running the program, user is prompted to select a difficulty level from easy / medium / hard
input = raw_input("Please select a level to begin at: (1) Easy (2) Medium or (3) Hard")

# Once a level is selected, game displays a fill-in-the-blank and a prompt to fill in the first blank.
print sentence_with_blanks
input = raw_input("Please fill in the first blank")

# When player guesses correctly, new prompt shows with correct answer in the previous blank and a new prompt for the next blank
print "That's right. 

# When player guesses incorrectly, they are prompted to try again

# If player passes level one, move on to level 2

# If player passes level one, move on to level 3

# If player passes level one, move on to level 4
