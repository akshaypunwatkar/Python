Now, you are ready to read the input. 

In input.py,

  - read_input method, which takes as parameters a filename string and
    a FutureCards fc. It reads input from the file (one hand per line)
    and returns a list of hands (Decks) that it read in. If a card is
    a future card (?0, ?1, etc.), it uses add_empty_card to create a
    placeholder in the hand and then uses add_future_card to make sure
    you will update it correctly when you draw later. 
    Hint: abstract out hand_from_string to handle each line of
    input. The split function is useful for parsing each line.

As always, test your code in test-input.py until you are satisfied
with its functionality.
