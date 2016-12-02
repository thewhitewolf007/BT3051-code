words=["abc","fghihgh","1234567"]

for w in words: 
    if len(w) > 6:
        words.insert(0, w)
    # if(len(words)==10):
    #    	break
print(words)