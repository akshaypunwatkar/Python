import random
import re
def randomStory(storyFile, wordTypes):

    #reading wordtypes and creating corresponding dictionary 
    word_Dict = {}
    for word_T in wordTypes:
        x = wordlist(word_T,word_Dict)
        word_Dict["_"+word_T]= x
    #print(word_Dict)
    newstory = ""
    #reading story file 
    story = open(storyFile)
    #replacing blanks by words
    replacement_list= []
    for line in story:
        wrdlst = []
        x = re.split(r'(\s+)', line)
        #x = line.split()
        for a in x:
            wrdlst.append(a)

        for i in range(len(wrdlst)):
            if(wrdlst[i].startswith("_")):
                for k,v in word_Dict.items():
                    if wrdlst[i].strip('.,?!') == k:
                        replacement_word = random.choice(word_Dict[k])
                        wrdlst[i] = wrdlst[i].replace(wrdlst[i].strip('.!?,'),replacement_word)
                        replacement_list.append(replacement_word)
                    if (wrdlst[i].strip('_.?,!')).isdigit():
                        replacement_pos = int(wrdlst[i].strip('_.?,!'))
                        wrdlst[i] = wrdlst[i].replace(wrdlst[i].strip('.?!,'),replacement_list[replacement_pos])
                        replacement_list.append(replacement_list[replacement_pos])             
        newline = " "
        newline = "".join(wrdlst)
            
        newstory = newstory + newline

    return newstory    

def wordlist(wordType,wordDict):
    lst = []
    f= open(wordType+".txt")
    for line in f:
        lst.append(line.strip())
    return lst
'''
def main():
    wt = ['animal', 'food', 'greeting', 'magiccreature', 'place', 'said', 'thing', 'time']
    print(randomStory('story.txt',wt))

main()
'''
