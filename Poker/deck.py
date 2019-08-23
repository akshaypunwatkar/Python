from card import Card, card_from_num
import random

class Deck:
    ''' This class is for decks'''
    def __init__(self):
        self.cards = []
        pass
    
    def __str__(self):
        x= []
        for i in self.cards:
            x.append(str(i))
        return " ".join(x)
        pass
    
    def __repr__(self):
        return "Deck("+self.__str__()+")"
        pass
    
    def add_card(self, c):
        self.cards.append(c)
        pass
    
    def add_empty_card(self):
        c= Card()
        self.cards.append(c)
        return c
        pass
    
    def contains(self, c):
        return c in self.cards
        pass
    
    def shuffle(self):
        random.shuffle(self.cards)
        pass

    def assert_full(self):
        for i in range(52):
            assert card_from_num(i) in self.cards, "{} is missing".format(card_from_num(i))         
        pass
    
    # takes card from from deck, appends it to end, and returns it
    def draw(self):
        x = self.cards.pop(0)
        self.cards.append(x)
        return x
        pass
    
    # sorts high to low
    def sort(self):
        self.cards.sort(reverse=True)
        pass
    pass

# builds and returns complete deck except for cards in hands
def build_remaining_deck(hands):
    hand_cards = Deck()
    new_deck = Deck()
    for decc in hands:
        for card in decc.cards:
            hand_cards.add_card(card)
    for i in range(52):
        if hand_cards.contains(card_from_num(i)):
            continue
        else:
            new_deck.add_card(card_from_num(i))

    return new_deck        
    pass
