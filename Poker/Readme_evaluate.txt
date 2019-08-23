The next part of the project that you will do is write some of the
code to evaluate and compare hands. Remember that you have already
written test cases for this code. That means you have already thought
about various corner cases that might come up and will have a nice
suite of tests ready to go when you finish your code.

Your ultimate goal in this step is to write a function that, when
passed two hands of cards, determines which one won (or if they tied).
We'll use the Deck class you worked with in a previous part to
represent a hand of cards as well (a hand of cards is just a much
smaller deck of cards---they are both just sets of cards).

There are three major steps to determining who won:
  (1) Figuring out what ranking each hand has (straight, flush,
      etc.)
  (2) Figuring out which five cards make up the hand (picking out the
      five cards that made the flush or the two pairs and tiebreaker)
  (3) Comparing the rankings, and if they are the same, breaking
      ties by comparing the values in the hands

At this point, you might be thinking that there is going to be a lot
of code to write with all the different possible arrangements of cards
and different possible hand rankings. However, we there are a few
important things that will make this managable:
  (1) You will start by sorting the cards into descending order by
      value. This makes it much easier to find straights (cards in
      order), and you will have "N of a kinds" grouped together. 
  (2) The code to find "N of a kind" is basically the same for 4, 3,
      and 2 (so we can abstract it out into a function). 
  (3) Full house and two pair are just three of a kind and a pair (so
      we already have that code) with another pair (so we can just
      write a function to find a secondary pair).
  (4) We are going to make two simplifying assumptions: 
      - if there is a flush, it will occur in at most one suit.
        (i.e., you won't have As Ah Kh Qs 8s 7h 4s 3s 3h 2h,
        which has two different flushes).
      - if there is an ace-high straight, there is not also
        an ace-low straight.
     (These both hold for all major poker variants)

In eval.py, write:

  - find_flush function, which takes a hand as a parameter and returns
    the suit of the flush if a flush is found and None otherwise. You
    may find it useful to use a dictionary to map each suit to the
    number of times that suit occurs in a hand.
  - count_values helper function, which takes a hand as a parameter
    and returns a dictionary of each card value (we recommend high to
    low) to the number of cards in the hand with that value.
  - get_max_count function, which takes a hand and dictionary returned
    by count_values as parameters and returns that pair in the
    dictionary with the maximum count. If multiple card values tie for
    highest count, return the highest value card.
  - find_secondary_pair function, which takes a hand, dictionary returned
    by count_values, and card value as parameters and looks for a
    secondary pair. If a pair exists that is not the passed-in card
    value, the function should return the index where the second pair
    occurs in the hand; otherwise, it should return -1.
  - get_kind_index function, which takes a hand and card value as
    parameters and returns the index in the hand of the card with that
    value.
  - build_of_a_kind function, which takes a hand, count of n, and an
    index as parameters. It builds the five-card Deck that makes up an
    n of a kind ranking by first adding the n cards starting at
    ind. Then it should fill the remaining cards (until there are
    five) with the highest remaining cards in the hand and return the
    five-card answer. It does not need to worry about secondary
    pairs---these will be added by the next function, add_pair. 
  - add_pair function, which takes a hand, secondary pair index,
    five-card answer Deck, and an answer index as parameters. It
    should add the secondary pair to the answer. If the answer index
    is 3 (as in a full house), it should add the secondary pair to be
    the last two cards. If the answer index is two (as in two pair),
    it should add the secondary pair to be the third and fourth cards,
    then select the next highest card to be the fifth. It returns the
    updated answer Deck.
  - is_straight_at function, which takes a hand, an index, and the
    (potential) flush suit and returns:
       1 if a regular straight is found at that index, 
      -1 if an ace-low straight is found at that index, and 
       0 if no straight is found. 
    If the flush suit is not None, only a straight flush in that suit
    should be considered. We recommend abstracting out two helper
    functions: 
      o is_n_length_straight_at, which can check for either a
        straight of length 5 or 4 depending on whether you're looking
	for a regular straight or an ace-low straight
      o is_ace_low_straight_at, which finds an ace, then calls
        is_n_length_straight_at with n = 4 to find the rest of the
	straight
    Hint: You may have multiple cards with the same value but still
    have a straight: 
      As Ac Ks Kc Qh Jh 0d
    has a straight, even though A K Q do not appear next to each other
    in our sorted order.
  - compare_hands function, which takes two hands as parameters and
    returns an integer that is:
      o positive if hand1 is a higher rank,
      o negative if hand2 is a higher rank, or
      o 0 if they exactly tie.
    This function should sort the hands, call evaluate_hand, get the
    numerical values of the ranks, and determine the winner. 
    Note: ties in hand ranking are broken by a comparison of each
    card's value from first to last---suit does not matter in tie
    breaking.

Provided:

  - find_straight function (and its helper function copy_straight),
    which takes a hand and flush suit and returns an answer Deck if a
    straight exists (or a straight flush if flush suit is not None) by
    calling the student's is_straight_at function
  - build_flush function, which takes a hand and flush suit and
    returns the answer Deck of the flush
  - evaluate_hand function, which calls the functions you wrote to
    decide, according to the rules of poker, which five cards make up
    the best hand and what its ranking is. It returns a tuple of the
    answer Deck and a string for the ranking
  - num_from_rank function, which takes a string representing a hand
    rank as a parameter and returns an integer, such that a
    higher value indicates a higher hand ranking
