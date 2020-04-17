import time

start_time = time.time()

words = ['dog','dark','car','door','dodge']

def arrayContainingPartialPhrase(phrase):
    temp = []
    phraseLength = len(phrase)
    for word in words:
        if(word[0:phraseLength] == phrase):
            temp.append(word)
    return temp

print(arrayContainingPartialPhrase('do'))
print("--- %s seconds ---" % (time.time() - start_time))
