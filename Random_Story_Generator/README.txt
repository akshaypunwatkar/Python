In this assignment, you are going to be writing a program
to generate a semi-random story, similar to the game "Mad Libs".

If you have never played Mad Libs, the way that it works it that
one player has a story with blanks in it.  Each blank contains
a description of the kind of word that goes there (like "verb"
or "place" or "food").  The player with the story asks
the other players to name a word of that kind, and writes
it in the blank.  Once all blanks are filled in, the story
is read aloud.

Our random story will follow the same principle, except
that we will also keep track of everything we selected
in the past, and allow reference to it by number.

If you look at the first two lines of story.txt, you will see

Once upon a time there was a _animal.  The _0 lived in a very scary _place.
One day, the _0 left his _2 and went in search of a _food.  

Each _ indicates a blank, and whatever is after the blank indicates
how to fill it in.
  - If the blank is immediately followed by a number, then it
    means to re-use the (number)th selection, counting from 0.
    For example _0 to re-use the first selected word.
    Note that this type of blank is followed by any number of base-10 digits
    (0-9), and ended with anything that is not a digit.
    Multi-digit numbers, such as _10, _123, etc are possible.
  - If the blank is immediately followed by a word, then it
    means to select a random word of that type.
    Note that this type of blank is followed by any number of letters
    (upper and or lower case (a-z, A-Z)).  Any non-alphabetic character
    ends the blank.  So _animal.  is the blank _animal followed
    by the literal character period.


So for example, we might select "cat" for the first blank (_animal).
When we reach the second blank (_0) we re-use cat.  We
might select "castle" for the next blank (_place).  The following
two blanks will be "cat" (_0) and "castle" (_2) since those reference
words already chosen.  Note that _1 would have also chosen
"cat".  We might then pick "pizza" for the final blank.  Any character
which is not part of a blank is returned literally.  We would
then return this string as our "story":
    
Once upon a time there was a cat.  The cat lived in a very scary castle.
One day, the cat left his castle and went in search of a pizza.  

At a high-level, you are going to create the file randomstory.py and write
the function

randomStory(storyFile, wordTypes)

The first parameter is the name of the story file (with the blanks in it).
The second is an iterable (e.g., list or set) which will name all the types
of words that must be selected (other than numbered back references).
In our example above, wordTypes would be ['animal', 'place', food'].
(However, for the full story.txt, the list would be
 ['animal', 'food', 'greeting', 'magiccreature', 'place', 'said', 'thing', 'time']

For each word type, you will read a file whose name is the type with .txt
on the end (e.g., animal.txt, place.txt).  This file will contain the possible
words of that type, one per line.

You are free to implement this any way you want, however, here are some hints:

  (1) Write a function readWordList which takes the name of the word type
      (e.g. 'animal') and returns a list of the words in that file
  (2) Build a dictionary mapping word types to the lists of words
      of that type (e.g.,
        {'animal' : ['cat', 'dog', 'dragon'], 
         'place'  : ['castle', 'cave', 'lake']}
      etc
  (3) Write a function randomWordForType which takes the dictionary
      as described in 2 and the type name, and returns a random word
      of that type
  (4) Keep a list of all the words you have put in blanks so far.  You
      can then index this list for any back references.
      

Note that you may select words randomly however you want, but it must be random:
there must be an (approximately) equal chance of drawing each line from the file.
When we grade this we will accept any random word in a particular story, but will
also run the random story generation multiple times and see how often
each word appears (if a word appears multiple times in the file, it should
be proportionally more likely---e.g., a b c a should have a appear with probability 2/4).

