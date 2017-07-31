#!/usr/bin/env python3

# Game has 3 or more levels and each level contains 4 or more blanks to fill in
sentences = [
"_1_ is a programming language named for Monty Python's Flying Circus. A _2_ is an immutable list of characters surrounded by quotes. A _3_ is an unordered collection of items of any type while a _4_ is an ordered collection of a single type.",
"A _1_ is an associative array that can contain any Python _2_ type. The print() function and integer division are key differences between Python _3_ and _4_",
"Python supports _1_ programming with classes and multiple _2_. Python _3_ are defined by creating a function and inheriting from a _4_ eg. variable = Class(parameters)"]

answers = [['Python','string','list','array'],['dictionary', 'data', '2', '3'],['object-oriented', 'inheritance','objects','class']]

sentence_with_blanks = ""

def level_selector(): 
    """User selected level is printed for user, along with the appropriate sentence
    Args:
        None
    Returns:
        level (int): Returns position of sentence in sentences depending on level chosen
    """
    level = str(input("Please choose a level: (1) Easy (2) Medium or (3) Hard. Type 'Q' to quit\n>> ")).lower()
    if level in ['q', 'Q']:
      quit()
    else:
      if level in ['easy', '1']:
        print('Level is: Easy')
        return 0
      elif level in ['medium','2']:
        print('Level is: Medium')
        return 1
      elif level in ['hard', '3']:
        print('Level is: Hard')
        return 2
      else:
        print("Please enter a valid input") # catches invalid inputs
        level_selector()

def sentence_play(level, blank_position=1, blanks_filled=0):
    """Allows user to enter selection and validates user response
    Args:
        level (int): level selected by user
        blank_position (int): position of blanks within sentence, default is first blank
        blanks_filled (int): number of blanks already filled, default is zero (no blanks filled)
    Returns:
        Does not return anything
    """
    total_blanks = 4
    while blanks_filled <= total_blanks:
      blank_input = input("\nWhat should be substituted in for _" + str(blanks_filled + 1) + "_?\n>>")
      if correct_answer(level, blank_position, blank_input):
             # When player guesses correctly, new prompt shows with correct answer in the previous blank and a new prompt for the next blank
        if blank_position >= total_blanks:
          print("\nGreat! You got them all correct:\n")
          display_filled_sentence(level, blank_position)
          print("\nReturning to the start...")
          start_game()
        print("\nNice work! You got that one.")
        display_filled_sentence(level, blank_position)
        print("\nNow on to the next question...")
        blanks_filled += 1
        blank_position += 1
      else:
        # When player guesses incorrectly, they are prompted to try again
        print('Not quite. Try again.')
        sentence_play(level, blank_position, blanks_filled)

def correct_answer(level, blank_number, answer):
    """Validates user response against answers array
    Args:
        level (int): level selected by user
        blank_number (int): number of blank within sentence
        answer (string): answer provided by user
    Returns:
        boolean: Returns true if answer is correct
    """
    return str(answer).lower().strip() == answers[level][blank_number - 1].lower()

def display_filled_sentence(level, position):
    """Displays the sentence as the user fills it in
    Args:
        level (int): level selected by user
        position (int): position of blank within sentence
    Returns:
        Does not return anything
    """
    #sentence = sentences[level].split(' ')
    replacement_position = 1
    sentence = sentences
    while replacement_position <= position:
      sentences[level] = sentences[level].replace('_' + str(replacement_position) + '_', answers[level][replacement_position - 1])
      replacement_position += 1
    print(sentences[level])

def start_game():
    """Prompts user and plays through game
    Args:
        None
    Returns:
        Does not return anything
    """
    # Start game with a prompt to the user
    print("Welcome to the fill-in-the-blanks quiz")
    while True:
        # Immediately after running the program, user is prompted
        # to select a difficulty level from easy / medium / hard
        level = level_selector()
        print(sentences[level])
        sentence_play(level) # user attempts to fill in blanks
        start_game() # game starts over
    else:
        quit()

start_game() # game play starts when file is run
