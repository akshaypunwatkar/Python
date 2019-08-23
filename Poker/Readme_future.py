Now, you are going to write a class to handle unknown/future cards. In
most poker variants, there are stages of the hand where some cards are
yet to be dealt, so we will need a way to represent unknown, future
cards. 

In addition to known cards in the input string (As, 0h, 8c, etc.),
there may be future cards, These will have a '?' and number indicating
the index of the future card (?0, ?1, ?2, etc.).

In future.py, write:

FutureCards class
  - future_cards field, which is a list of decks.
  - __init__ method, which should initialize future_cards to be an
    empty list.
  - __str__ method, which creates a string of each deck, followed by a
    newline.
  - __repr__ method, which prints 'FutureCards:', then each future
    card index, a colon, and the future cards at that index, e.g.
      FutureCards:
      ?0: ??
      ?1: ?? ??
      ?2: 
      ?3: 
      ?4: ??
    if the cards have not been filled in yet, or 
      FutureCards:
      ?0: 4s
      ?1: 9c 9c
      ?2: 
      ?3: 
      ?4: Qs
    if the cards have been filled in by future_cards_from_deck (see
    below).
  - add_future_card method, which takes as parameters an index and the
    card to be added and adds the card to the deck in future_cards at
    the appropriate index. Note that the index might be greater than
    the size of future_cards. You could have input like      
      Kh Qh As 4c 2c ?3 ?4
      Ac Qc As 4c 2c ?3 ?4
    which might happen if e.g., someone edited a file that originally
    have ?0, ?1, and ?2 but replaced them when they became known. Or
    you might see ?3 before ?2. 
  - future_cards_from_deck method, which takes a deck d (already
    shuffled) as a parameter. For each deck in future_cards, this
    method draws a card from d then assigns the value and suit of each
    placeholder card in the current deck to the drawn card's value and
    suit, thus "filling in" each of the unknown cards with a card
    drawn from d. For example, if the input deck began:
      As Kh 8c ...
    and future_cards was created from the input
      3c 4c ?0 ?1 ?2
      5h 9d ?0 ?1 ?2
    then this function will draw As for ?0 and fill in the two
    placeholders for ?0. Then it will draw Kh for ?1 and fill those
    in; then it will draw 8c for ?2 and fill those in.
  - Don't forget a docstring!

As always, test your FutureCards class in test-future.py. You do not
need to read input at this point (that is the next step)--you can
create sample hands with cards of your choosing and blank cards
(Card()) using add_card. You can make a full deck, assert it is full,
shuffle, then pass it to future_cards_from_deck. 
