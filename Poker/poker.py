#!/usr/local/bin/python3

import sys
from future import FutureCards
from pinput import read_input
from deck import build_remaining_deck
from evaluate import compare_hands

# provided
def print_results(wins, n):
    for i in range(0, len(wins) - 1):
        print('Hand {} won {} / {} times'.format(i, wins[i], n))
        pass
    print('and there were {} ties'.format(wins[len(wins) - 1]))
    pass

def main():
    # get count of command line arguments
    argc = len(sys.argv)
    # check user input
    inputFile = sys.argv[1]
    nbr_of_simulation = 10000
    if argc == 3:
        nbr_of_simulation = int(sys.argv[2])

    # read from file
    fc= FutureCards()
    hand_lst = read_input(inputFile,fc)
    deck_of_remaining_card = build_remaining_deck(hand_lst)
    wins = []
    for c in range(len(hand_lst)+1):
        wins.append(0)    
    # do monte carlos
    for i in range(nbr_of_simulation):
    
        deck_of_remaining_card.shuffle()
        fc.future_cards_from_deck(deck_of_remaining_card)
        hand_indx = 0
        tie_indx = 0
        for i in range(len(hand_lst)-1):
            #print("Between {} and {}".format(str(hand_lst[hand_indx]),str(hand_lst[i+1])))
            result = compare_hands(hand_lst[hand_indx],hand_lst[i+1])
            #print("Between {} and {} : {} won".format(str(hand_lst[hand_indx]),str(hand_lst[i+1]),str(result)))    
            if (result == 1):
                continue
            elif (result == -1):
                hand_indx = i+1
            else:
                tie_indx = i+1
                hand_indx += 1
            
        if(tie_indx == len(hand_lst)-1):
            wins[-1] = wins[-1]+1
        else:
            wins[hand_indx] = wins[hand_indx]+1
        #print(hand_indx)    
        #print(wins)
        #print("Next itiration : \n")
        # print results
    print_results(wins,nbr_of_simulation)
    pass

if __name__ == '__main__':
    main()
