from deck import Deck
from card import Card

class FutureCards:
    ''' This is class to assign a future cards '''

    def __init__(self):
        self.future_cards = []
        pass
    
    def __str__(self):
        s=""
        for d in self.future_cards:
            s = s + str(d) +"\n"            
        return s.rstrip()
        pass
    
    def __repr__(self):
        ss = "FutureCards:\n"
        j= 0
        for i in self.future_cards:
            ss = ss + "?" + str(j) + ": " + str(i) +"\n"
            j +=1
        return ss.rstrip()
        pass
    
    def add_future_card(self, ind, c):
        if(len(self.future_cards) <= ind):
            for i in range(len(self.future_cards),ind+1):
                self.future_cards.append(Deck())
            self.future_cards[i].add_card(c)
        else:
            self.future_cards[ind].add_card(c)
        pass
    
    def future_cards_from_deck(self, d):
        for i in (self.future_cards):
            crd = d.draw()
            for k,v in enumerate(i.cards):
                i.cards[k].value = crd.value
                i.cards[k].suit = crd.suit
        pass
    pass
