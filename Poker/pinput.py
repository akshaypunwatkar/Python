from deck import Deck
from card import Card
from future import FutureCards

def hand_from_string(s, fc):
    pass

def read_input(file, fc):
    f =  open(file)
    lst = []
    for line in f:
        d = Deck()
        card_list = line.split()
        for c in card_list:
            try:
                d.add_card(Card(c[0],c[1:]))
            except:
                if(c[0]== "?"):
                    newcard = d.add_empty_card()
                    fc.add_future_card(int(c[1:]),newcard)
        lst.append(d)    
    return lst
    pass
