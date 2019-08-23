from operator import itemgetter

def countWords(counts,line):
    words = line.split()
    for word in words:
        word = word.strip('-?.!,[]—:;"\'')
        word = word.lower()
        counts[word] = counts.get(word,0) + 1
    # You should write this function in Step 1,
    # and improve it in Step 2    
    return counts

def printResults(counts):
    #print(counts)
    # You will replace this code in Step 3 and 4
    lst = []
    for key, values in counts.items():
        lst.append((key,values))

    lst.sort(key=itemgetter(0))
    for item in lst:
        print(str(item[0])+ " : "+str(item[1]))
    pass


# You do not need to modify this function.
# It will call your countWords and printResults functions
def countFile(fname):
    counts={}
    with open(fname) as f:
        for line in f:
            #print(line)
            countWords(counts,line)
            
            pass
        pass
    printResults(counts)
    pass

'''
def main():
    countFile("/usr/local/mids/words/caesar.txt")

main()
'''    
