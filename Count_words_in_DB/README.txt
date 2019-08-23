A few days ago, you wrote a program that would read a file, count how
many times each word appears, and then print it out.  You are now
going to do something similar, except you will store the results in a
database (rather than print them out) and do it for multiple files.

First, let us create a database and a table for this data:

Run the Linux command
  createdb documents-netid
Where you replace netid with your netid.
This will create a new database called "documents-netid"
(For example, Drew would do createdb documents-adh39 to make the
  documents-adh39 db)

Now do
  psql documents-netid

Next, you want to create a table (we'll call it wordcounts) with three
columns. These columns should be the document id ("docid"), which we'll
make a bigint (64 bits), the word ("word"), which we'll make text, and the
count of how many times it occured ("count"), which we'll make an int
(32-bits). 
We will also make the pair (docid,word) the primary key for the table.
This will require that any given (docid,word) pair be unique, as well
as making the database build some indices, which make queries that
search by docid and/or word go much faster.  We won't cover primary
keys or indices in depth here, but do this because it is the right
thing to do here.  We also tell postgres that count cannot be NULL (we
do not need this for the others as PRIMARY KEY implies NOT NULL).

Enter this at the postgres prompt:
  CREATE TABLE wordcounts (
    docid bigint,
    word text,
    count int NOT NULL,
    PRIMARY KEY (docid,word)
  );

Postgres should respond with the output
  CREATE TABLE
confirming that it created a table.  If you do
  SELECT * from wordcounts;
You should see that there is a table, but it is empty:
  documents-adh39=> select * from wordcounts ;
   docid | word | count 
  -------+------+-------
  (0 rows)

  documents-adh39=>

Now quit the postgres command prompt (Either type \q enter, or control
d).

Now you are ready for the programming part.

Your goal is to write the function putWordCountsInDB in worddb.py.
This function should take two parameters.  The first parameter is a
string, which names the database (you will test this with
'documents-netid', which you created above, but we will grade with a
different db.  Note that when we use a different db to grade, we will
already have it set up as above.). 
The second parameter is a list of tuples.  Each tuple in the list
contains a number (the document id) and a string (the file's name).
For example, the parameter might be
  [ (0, "macbeth.txt"), (14, "hamlet.txt"), (2, "caesar.txt"), 
    (37, "henryviii.txt") ] 

For each tuple in the list, you should
  - Check that the document id is not already in the data base:
    If it is, print an error message, skip that file, and continue
    processing the rest. 
  - Read the file and count how many times each word appears.
    As with your previous assignment, you should convert all words to
    lower case and trim "garbage" characters off the ends.
  - For each word in the file, insert a row into the database with the
    document's id, the word, and the count of how many times it
    appeared. 
  - Commit the transaction. (Note: this means you should insert all
    rows for one document into the wordcounts table using the same
    connection. If you abstract out parts of this code, you can pass
    the connection as a parameter to helper functions.)

NOTE: if you used GOOD ABSTRACTION when you did count_words a few days
      ago, then you should have about 85% of this code already done!
      You can just reuse those functions to read the files and count
      the words.  You would only need to change how you handle the
      output---INSERTing the results into the database rather than
      printing them to the screen. 
