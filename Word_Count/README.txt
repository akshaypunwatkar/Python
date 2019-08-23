For this assignment, you will write a program that counts how many
times each word appears in a text file and prints out the results. For
example, if you look in /usr/local/mids/words/casear.txt, which is
part of the text of Julius Caesar, you will find that the word
"caesar" appears 34 times (ignoring case).

As you have not yet learned to read files, we have provided
the countFile function to you (in countWords.py)

def countFile(fname):
    counts={}
    with open(fname) as f:
        for line in f:
            countWords(counts,line)
            pass
        pass
    printResults(counts)
    pass

This function makes an empty dictionary, and then reads each line in a
file, calling your countWords function and to update the dictionary
which maps words to their counts.  when it finishes with the file, it
calls your printResults function to print out the final results.

Step 1:
--------------------
Write the function
  countWords(counts,line)
which takes:
  counts: a dictionary that maps words to how many times they appear
    and 
  line: a string, which you should split into words and, for each word
    you see, update counts to reflect that occurence of the word.
This function should return the updated "counts" dictionary.

A few hints:
   - If you call line.split(), it will split the line based on
     whitespace, returning a list of each string that the line was
     split into. 
   - We have provided a simple "printResults" which just prints counts:
     you can use it to test your countWords function before you proceed.

Step 2:
--------------------
If you look at the results of countWords, you will see that sometimes
we end up with words like "now," which really just should be "now".
Likewise, "The" and "the" are counted as two separate words.  You can
improve on your countWords by using the following two string
functions:
  - string.strip('-?.!,[]—:;"\'') will return a string with any leading
    or trailing occurences of any of the characters -?.!,[]—:;"' removed 
    from it. 
  - string.lower() will return string converted to all lower case
    letters. 

Step 3:
--------------------
printResults currently just prints the dictionary, using its built in
conversion to a string.  That is fine for testing, but not a great
output format. For this step, you should replace the code in
printResults so that it prints out each word and its corresponding
count, 1 per line, e.g.: 

and : 59
a : 27
the : 72
caesar : 34

Step 4:
--------------------
For this final step, you will make your output a little nicer even
still by sorting it by the words, so that they are in alphabetical order.
To acomplish this, you will want to put the items from the dictionary
into a list, then use 
  thatlist.sort()
However, you will need to pass an extra parameter to .sort() to get the
behavior you desire.  Check out the documentation for .sort() 
  https://docs.python.org/3.3/howto/sorting.html
to find out how to sort by the words (which should be a particular item in
      a tuple).

You may wish to make use of the other files in /usr/local/mids/words
to test out your program.
