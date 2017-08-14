// built in JavaScript, utilizes functionality of Python command line fill-in-the-blanks script

// Game has 3 or more levels and each level contains 4 or more blanks to fill in
const sentences = [
"_1_ is a programming language named for Monty Python's Flying Circus. A _2_ is an immutable list of characters surrounded by quotes. A _3_ is an unordered collection of items of any type while a _4_ is an ordered collection of a single type.",
"A _1_ is an associative array that can contain any Python _2_ type. The print() function and integer division are key differences between Python _3_ and _4_",
"Python supports _1_ programming with classes and multiple _2_. Python _3_ are defined by creating a function and inheriting from a _4_ eg. variable = Class(parameters)"]

const answers = [['Python','string','list','array'],['dictionary', 'data', '2', '3'],['object-oriented', 'inheritance','objects','class']]

const levelSelector = () => {
  // User selected level is printed for user, along with the appropriate sentence  
}

const sentencePlay = (level, blank_position=1, blanks_filled=0) => {
  // Allows user to enter selection and validates user response
}

const correctAnswer = (level, blank_number, answer) => {
  // Validates user response against answers array
}

const displayFilledSentence = (level, position) => {
 // Displays the sentence as the user fills it in 
}

const startGame = () => {
  // Prompts user and plays through game
}

start_game() // game play starts when file is run
