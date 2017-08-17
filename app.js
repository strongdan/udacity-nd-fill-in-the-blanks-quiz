
// built in JavaScript, utilizes functionality of Python command line fill-in-the-blanks script
let script = document.createElement('script');
script.src = 'https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js';
script.type = 'text/javascript';

let sentencesWithAnswers = { // sentences and their corresponding answers, organized by level 1-3
  1: {'sentence': '_1_ is a programming language named for Monty Pythons Flying Circus. A _2_ is an immutable list of characters surrounded by quotes. A _3_ is an unordered collection of items of any type while a _4_ is an ordered collection of a single type.',
      'answers': ['Python','string','list','array']},
  2: {'sentence': 'A _1_ is an associative array that can contain any Python _2_ type. The print() function and integer division are key differences between Python _3_ and _4_',
      'answers': ['dictionary', 'data', '2', '3']},
  3: {'sentence': 'Python supports _1_ programming with classes and multiple _2_. Python _3_ are defined by creating a function and inheriting from a _4_ eg. variable = Class(parameters)',
      'answers': ['object-oriented', 'inheritance','objects','class']}
  }

// Game has 3 or more levels and each level contains 4 or more blanks to fill in

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
 let filledSentence = sentencesWithAnswers[level]['sentence'].split(' ');
 let currentPos = 0;
 while (currentPos <= position) {
   for (let i = 0; i < filledSentence.length; i++) {
     if (filledSentence[i] === `_${position}_`) {
       filledSentence[i] = sentencesWithAnswers[level]['answers'][position];
     }
   }
 }
 return filledSentence.join(' ');
}

const startGame = () => {
  // Prompts user and plays through game
  $()
}

start_game() // game play starts when file is run
