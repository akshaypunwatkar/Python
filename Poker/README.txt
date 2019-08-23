For the next day and a half, you will be working on building a program
that estimates the chances of each hand winning in poker in a
situation described by an input file. 

In this portion of the project, you are going write the Card class, as
well as any additional variables or helper functions you might need.
Specifically, a Card will represent information about a card's value and
suit, as well as convert that information to a human-readable format
with a pair of letters that describe a card. For example, the 2 of
hearts would be '2h', where the first character is one of (2, 3, 4, 5,
6, 7, 8, 9, 0, J, Q, K, A) for the value, and the second character is
one of (s, h, d, c) for the suit.

In card.py, write:

Card class
  - value field, which should be a number 2-14 (inclusive), or 0 for an
    invalid value (consider defining ACE = 14, KING = 13, QUEEN = 12, and
    JACK = 11 to make your code more readable).
  - suit field, which should be a character ('s', 'h', 'd', 'c') or
    '?' for an invalid suit.
  - __init__ method to construct a card from letters for the value and
    suit; if no arguments are given, the default letters should be
    '?'.
  - __str__ method to make a string representation of the card with two
    characters, for example, 'As'.
  - __repr__ method that prints 'Card( )' around the string
    representation, for example, 'Card(As)'.
  - __eq__ (equal to) method, which takes a parameter other and
    returns True if self and other have the same value and same suit
    and False otherwise.
  - __lt__ (less than) method, which takes a parameter other and
    returns True if self is less than other and False otherwise. If
    the cards have the same value, determine which suit is "less
    than": c < d < h < s.
  - is_valid method, which returns True if both the card's value and
    suit are valid.

Other 'public' function (function should be defined in card.py, but it
is not a method of Card)
  - card_from_num function to take a number 0-51 (inclusive) and
    return a Card in the standard deck. This function should make use
    of is_valid. You can do the math however you like, but calling
    card_from_num on 0-51 (inclusive) should build a full deck.

Hint: to make your code for __init__ and __str__ easier to read,
consider abstracting parts out into the following helper functions: 
  - value_from_letter
  - check_suit 
  - letter_from_value

If any of the arguments to the above functions are invalid, you should
raise a ValueError with a meaningful error message, such as 
  'invalid suit: {}'.format(suit)

You may also want the helper functions 
  - is_value_value
  - is_valid_suit
which return booleans.

Now test your Card class in test-card.py. You will want to import Card
and card_from_num.
