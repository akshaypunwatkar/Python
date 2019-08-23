def value_from_letter(let):
    mydict = {"J":11,"Q":12,"K":13,"A":14,"0":10,"?":0,"c":101, "d":102, "h":103, "s":104}
    if(let in mydict.keys()):
        return(mydict[let])
    else:
        return int(let)
    pass

#def check_suit(let):
#    pass

def letter_from_value(val):
    mydict2 = {14:"A",13:"K",12:"Q",11:"J",0:"?",10:"0",101:"c", 102:"d", 103:"h", 104: "s" }
    if(val in mydict2.keys()):
        return(mydict2[val])
    else:
        return str(val)
    pass

#def is_valid_value(value):
#    pass

#def is_valid_suit(suit):
#    pass

class Card:
    """A class to represent a card with a value and suit"""
    
    def __init__(self, value_let = '?', suit_let = '?'):
        if(value_let in ["A","K","Q","J","2","3","4","5","6","7","8","9","0"] and suit_let in ["c","d","s","h"]):
            self.value = value_from_letter(value_let)
            self.suit = suit_let
        elif(value_let == "?" and suit_let=="?"):
            self.value = 0
            self.suit = 0
        else:    
            raise ValueError("Invalid inputs !! Please enter valid inputs")
        pass
    
    def __str__(self):
        return (letter_from_value(self.value)+self.suit)

    
    def __repr__(self):
        return ("Card("+self.__str__()+")")

    def __eq__(self, other):
        return ( self.value == other.value and self.suit == other.suit)
        pass
    
    def __lt__(self, other):
        if(self.value != other.value):
            return (self.value < other.value)
        else:
            return value_from_letter(self.suit) < value_from_letter(other.suit)
        pass
    
    def is_valid(self):
        return ((self.value in range(2,15)) and (self.suit in ["s","h","d","c"]))
        pass
    pass

def card_from_num(num):
    cards = ["A","K","Q","J","2","3","4","5","6","7","8","9","0"]
    suits = ["c","s","d","h"]
    card_suit = []
    for i in cards:
        for j in suits:
            card_suit.append((str(i),str(j)))
    if(num in range(52)):
        return Card(card_suit[num][0],card_suit[num][1])        
    else:
        raise ValueError("Invalid input. Input should be b/w 0-51")
    pass
'''
def main():
    card_dict = {11:"J",12:"Q",13:"K",14:"A","?":"?"}
    suit_dict = {"c":1, "d":2, "s":3, "h":4}
    
    card1 = Card("A","c")
    card2 = Card("?","?")
    print("Is the {} valid : {}".format(card1.__repr__(),str(card1.is_valid())))
    print("Is the {} valid : {}".format(card2.__repr__(),str(card2.is_valid())))
    print("Is {} is less the {} : {}".format(card1.__repr__(), card2.__repr__(),str(card1.__lt__(card2))))
    print(card_from_num(8))
    
if __name__ == main():
    main()
'''
