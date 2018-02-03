def Sentencereversal(Sentence):
    words = Sentence.split(" ")
    # Reverse each word and a new list of words is created
    newWords = [word[::-1] for word in words]
    # new sentence is formed with new words
    newSentence = " ".join(newWords)
    return newSentence
#gives the largest word from sentence
def Largest(Sentence):
    pool = Sentence.split()
    pool.sort(key=len, reverse=True)
    return pool[0]
#gives the middle word of the sentence
def middle(Sentence):
    d =Sentence.split(" ")
    print(d)
    if len(d) % 2 == 0:
        return d[int(len(d) / 2)], d[int(len(d) / 2 - 1)]
    else:
        return d[int(len(d) // 2)]
Sentence = input("The Sentence is :\n")
print("Reverse:",Sentencereversal(Sentence))
print("Largest Word:",Largest(Sentence))
print("Middle Word:",middle(Sentence))