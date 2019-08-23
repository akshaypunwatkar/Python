from card import Card, card_from_num,  value_from_letter, letter_from_value
from deck import Deck
from operator import itemgetter,attrgetter

# finds flush suit
def find_flush(hand):
    hand.sort() 
    suits_dic = {}
    for card in hand.cards:
        suits_dic[card.suit] = suits_dic.get(card.suit,0)+1
    lst = sorted(suits_dic.items(), key= itemgetter(1), reverse=True)   
    if (lst[0][1] >= 5):
        return lst[0][0]
    else:
        return None
    pass

# makes dictionary of cards values to count of their occurances
def count_values(hand):
    hand.sort()
    card_log = {}
    for x in range(2,15):
        card_log[x] = 0
    for card in hand.cards:
        val = value_from_letter(card.value)
        card_log[val] = card_log.get(val, 0) + 1
    return card_log    
    pass

# uses counts dict and returns a tuple (value with most n of a kind, n)
def get_max_count(hand, counts):
    hand.sort()
    max_lst = []
    sort_lst = sorted(counts.items(),key=itemgetter(1), reverse=True)
    if(sort_lst[0][1] != sort_lst[1][1]):
        return(letter_from_value(sort_lst[0][0]),sort_lst[0][1])
    else:
        max_val = sort_lst[0][1]
        for a in sort_lst:
            if(a[1] == max_val):
                max_lst.append(a)
            else:
                continue
        max_lst = sorted(max_lst, key = itemgetter(0), reverse=True)    
        return (letter_from_value(max_lst[0][0]),max_lst[0][1])
    pass

# finds index of second pair or returns -1 for no sec pair
def find_secondary_pair(hand, counts, val):
    hand.sort()
    crd_val, prim_oc  = get_max_count(hand,counts)
    counts.pop(value_from_letter(crd_val))
    sec_crd, sec_oc = get_max_count(hand,counts)
    if sec_oc < 2:
        return -1
    else:
        return get_kind_index(hand,sec_crd)
        pass
    pass

# get first index of value in hand
def get_kind_index(hand, value):
    hand.sort()
    for pos,card in enumerate(hand.cards):
        if card.value == value_from_letter(value):
            return pos
        else:
            continue
    pass

# build hand with n of a kind starting at ind
def build_of_a_kind(hand, n, ind):
    hand.sort()
    answerDeck = Deck()
    card_val = list(hand.cards)[ind].value
    i = 0 
    for pos,card in enumerate(hand.cards):
        if pos >= ind:
            if card.value == card_val:
                answerDeck.add_card(card)
                i +=1
            else:
                continue
        else:
            continue
    for caard in hand.cards:
        if (not answerDeck.contains(caard)) and (i <  5):
            answerDeck.add_card(caard)
            i +=1
            pass
        else:
            continue
    return answerDeck
    pass

# adds secondary pair (for full house or two pair)
def add_pair(hand, pi, ans, ai):
    hand.sort()
    newDck = Deck()
    sec_crd_val = list(hand.cards)[pi].value
    x =0
    for i in range(ai):
        newDck.add_card(list(ans.cards)[i])
        x +=1
    count = 5-ai+1

    for cardd in hand.cards:
        if cardd.value == sec_crd_val and x < 5:
            newDck.add_card(cardd)
            x +=1
            pass
        else:
            continue    
    for caard in hand.cards:    
        if (not newDck.contains(caard) and x < 5):
            newDck.add_card(caard)
            x +=1
        else:
            continue
    return newDck    
        
    pass

# helper for is_straight_at
def is_n_length_straight_at(hand, ind, fs, n):
    hand.sort()
    num_of_card_in_straight = 0
    Straight_card_list = []
    card_list_n = []
    for pos,card in enumerate(hand.cards):
        card_list_n.append((card.value,card.suit))
    starting_card = card_list_n[1][0]
    for i in range(ind,len(card_list_n)-1):
        if(len(Straight_card_list) == n):
            break
        if(i == ind and (card_list_n[i][0] - card_list_n[i+1][0] != 1)):
            break
        elif(card_list_n[i][0] - card_list_n[i+1][0]) == 1 :
            if (card_list_n[i][0] not in Straight_card_list ):
                Straight_card_list.append(card_list_n[i][0])
                num_of_card_in_straight  = 1
            if (card_list_n[i+1][0] not in Straight_card_list):
                Straight_card_list.append(card_list_n[i+1][0])
                num_of_card_in_straight +=1
            pass
        elif (card_list_n[i][0] == card_list_n[i+1][0]):
            continue
        else:
            Straight_card_list = []
            num_of_card_in_straight = 0
            break
            pass
    #print("Index: "+str(ind))    
    #print("Straight_card_list :"+str(Straight_card_list) )
    #print("num_of_card_in_straight :" +str( num_of_card_in_straight))
    #print(fs)
    if(num_of_card_in_straight >= n):
        if (fs == None):
            return True
        else:
            for scard in Straight_card_list:
                if not hand.contains(Card(letter_from_value(scard),fs)):
                    return False
            return True    
    else:
        return False
    pass

# helper for is_straight_at
def is_ace_low_straight_at(hand, ind, fs):
    hand.sort()
    flag = False
    ace_exists = False
    ace_low_list = []
    for pos,card in enumerate(hand.cards):
        ace_low_list.append((card.value,card.suit))
        if card.value == 14:
            ace_exists = True
        else:
            continue
    for x in range(4):
        if (ace_low_list[x][0] == 5 and ace_exists == True):
            flag = is_n_length_straight_at(hand,x,fs,4)
            if (fs == None and flag == True):
                return True
            elif(flag == True and hand.contains(Card('A',fs))):
                return True
                pass
        else:
            continue
    return False
    pass

# if fs = None, look for any straight
# if fs = suit, look for straight in suit
# returns -1 for ace-low, 1 for straight, 0 for no straight
def is_straight_at(hand, ind, fs):
    flag_for_ace_low = is_ace_low_straight_at(hand,ind,fs)
    flag_for_Straight = is_n_length_straight_at(hand,ind,fs,5)
    if (flag_for_Straight == True):
        return 1
    elif(flag_for_ace_low == True):
        return -1
    else:
        return 0    
    pass

# provided
def copy_straight(hand, ind, fs, ace_low=False):
    ACE = 14
    ans = Deck()
    last_card = None
    target_len = 5
    idx = ind
    #assert (not fs or hand.cards[ind].suit == fs) 
    if ace_low:
        assert hand.cards[ind].value == ACE
        last_card = hand.cards[ind]
        target_len = 4
        to_find = 5
        ind += 1
        pass
    elif(hand.cards[ind].value == hand.cards[ind-1].value):
        to_find = hand.cards[ind-1].value
        ind = ind - 1
    else:    
        # regular straight
        to_find = hand.cards[ind].value
        pass
    while len(ans.cards) < target_len:
        assert ind < len(hand.cards)
        if hand.cards[ind].value == to_find:
            if not fs or hand.cards[ind].suit == fs:
                ans.add_card(hand.cards[ind])
                to_find -= 1
                pass
            pass
        ind += 1
        pass
    if last_card is not None:
        ans.add_card(last_card)
        pass
    assert len(ans.cards) == 5
    return ans

# provided
# looks for a straight (or straight flush if fs is not None)
# calls the student's is_straight_at for each index
# if found, copy_straight returns cards used for straight
def find_straight(hand, fs):
    for i in range(0, len(hand.cards) - 4):
        is_straight = is_straight_at(hand, i, fs)
        if is_straight == 1:
            # straight
            return copy_straight(hand, i, fs)
        pass
    for i in range(0, len(hand.cards) - 4):
        is_straight = is_straight_at(hand, i, fs)
        if is_straight == -1:
            # ace-low straight ( ****************************** Made change, replaced fs with None) ***************
            return copy_straight(hand, i, None, True)
        pass
    return None

# provided
# builds hand with flush suit fs
def build_flush(hand, fs):
    ans = Deck()
    i = 0
    while len(ans.cards) < 5:
        assert i < len(hand.cards)
        if hand.cards[i].suit == fs:
            ans.add_card(hand.cards[i])
            pass
        i += 1
        pass
    return ans

# provided
def evaluate_hand(hand):
    # straight flush
    fs = find_flush(hand)
    straight = find_straight(hand, fs)
    for i in range(5):
        flag_ace_low = is_ace_low_straight_at(hand,i,fs)
        if flag_ace_low:
            break
    if fs and straight and (not flag_ace_low) :
        return straight, 'straight flush'
    # four of a kind
    val_counts = count_values(hand)
    v, n = get_max_count(hand, val_counts)
    assert n <= 4
    ind = get_kind_index(hand, v)
    if n == 4:
        return build_of_a_kind(hand, 4, ind), 'four of a kind'
    # full house
    sec_pair = find_secondary_pair(hand, val_counts, v)
    if n == 3 and sec_pair >= 0:
        ans = build_of_a_kind(hand, 3, ind)
        ans = add_pair(hand, sec_pair, ans, 3)
        return ans, 'full house'
    # flush
    if fs:
        return build_flush(hand, fs), 'flush'
    # straight
    if straight:
        return straight, 'straight'
    # three of a kind
    if n == 3:
        return build_of_a_kind(hand, 3, ind), 'three of a kind'
    # two pair
    if n == 2 and sec_pair >=0:
        ans = build_of_a_kind(hand, 2, ind)
        ans = add_pair(hand, sec_pair, ans, 2)
        return ans, 'two pair'
    # pair
    if n == 2:
        return build_of_a_kind(hand, 2, ind), 'pair'
    # high card
    ans = Deck()
    ans.cards = hand.cards[0:5]
    return ans, 'high card'

def num_from_rank(r):
    ranks = ['high card', 'pair', 'two pair', 'three of a kind', \
                 'straight', 'flush', 'full house', \
                 'four of a kind', 'straight flush']
    return ranks.index(r)

# returns positive if hand1 > hand2, 
# 0 for tie, or 
# negative for hand2 > hand 1
def compare_hands(hand1, hand2):
    hand1.sort()
    hand2.sort()
    d1,val1 = evaluate_hand(hand1)
    d2,val2 = evaluate_hand(hand2)
    #print(evaluation1)
    #print(evaluation2)
    if (val1 != val2):
        if(num_from_rank(val1) > num_from_rank(val2)):
            return 1
        else:
            return -1
    else:
        lst_card1 = []
        lst_card2 = []
        for card1 in d1.cards:
            lst_card1.append((card1.value,card1.suit))
        for card2 in d2.cards:
            lst_card2.append((card2.value,card2.suit))    
        pass
        for i in range(5):
            if (lst_card1[i][0] > lst_card2[i][0]):
                return 1
            elif(lst_card1[i][0] < lst_card2[i][0]):
                return -1
        return 0
    
from random import sample
'''
#0h Qh Qd Jh Jc 8h 9h
#0h 8h 5c 4c 9h 3c 2c
def main():
    D1 = Deck()
    D2 = Deck()
    D1.add_card(Card('0','h'))
    D1.add_card(Card('Q','h'))
    D1.add_card(Card('Q','d'))
    D1.add_card(Card('J','h'))
    D1.add_card(Card('J','c'))
    D1.add_card(Card('8','h'))
    D1.add_card(Card('9','h'))
    D1.sort()
    D2.add_card(Card("0","h"))
    D2.add_card(Card("8","h"))
    D2.add_card(Card("5","c"))
    D2.add_card(Card("4","c"))
    D2.add_card(Card("9","h"))
    D2.add_card(Card("3","c"))
    D2.add_card(Card("2","c"))
    D2.sort()
    print(D1)
    #print(D2)
    #print(evaluate_hand(D2))
    print(evaluate_hand(D1))
    #print(is_straight_at(Dk,0,'d'))
    #print(compare_hands(D1,D2))
main()
'''
'''
def main():
    card = ["A","K","Q","J","0","9","8","7","6","5","4","3","2"]
    suit = ["s","d","h","c"]
    cards_lst = []
    for crd in card:
        for st in suit:
            cards_lst.append(Card(crd,st))
    
    for i in range(100):
        d1 = Deck()
        hd = sample(cards_lst,7)
        for c in hd:
            d1.add_card(c)
        d1.sort()    
        print("Deck is : "+ str(d1))    
        print("Evaluation result is : "+ str(evaluate_hand(d1))+"\n")    
main()   
'''
#Ah Qh Qd Jh Jc 9d 3s
#Ah 9d 5c 4c 3s 3c 2c
#Ah Jh Jd Jc 9d 5h 3s

