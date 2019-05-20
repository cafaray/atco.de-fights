def chatBot(conversations, currentConversation):
    maxWords = -1
    maxRow = -1
    maxPointer = []
    pointer = []
    d = {}    
    for conversation in range(len(conversations)):
        pointer = []
        for word in range(len(currentConversation)):
            if currentConversation[word] in conversations[conversation]:
                d[conversation] = d.get(conversation, 0) + 1
                pointer += [currentConversation[word]]
        if d.get(conversation,-1)>maxWords:
            maxWords = d.get(conversation)
            maxRow = conversation
            maxPointer = pointer
    #print(d)
    #print("maxWords is:", maxWords)
    #print("maxRow is:", maxRow)
    #print("maxPointer words:", maxPointer)
    
    if len(maxPointer)>0:
        print("words found:", maxPointer)
        print("conversation to use:", conversations[maxRow])
        useFrom = -1
        for x in range(len(conversations[maxRow])-1,-1,-1):
            if conversations[maxRow][x] not in maxPointer: continue
            #for y in range(len(maxPointer)):
                #print("real coincidence in: ",conversations[maxRow][x], '==', maxPointer[y])
            #    if conversations[maxRow][x]==maxPointer[y]:
            useFrom = x
            break
            #if useFrom>=0: break
            
        #print("useFrom: ", useFrom)
        words = conversations[maxRow][useFrom+1:]
        print("words to complete: ", words)
        currentConversation+=words
    #print("currentConversation: ", currentConversation)
    return currentConversation

conversations= [["where","are","you","live","i","live","in","new","york"], 
 ["are","you","going","somewhere","tonight","no","i","am","too","tired","today"], 
 ["hello","what","is","your","name","my","name","is","john"]]
currentConversation= ["hello", "john", "do",  "you",  "have",  "a",  "favorite",  "city",  "to",  "live",  "in",  "yes",  "it",  "is"]
expected=["hello",  "john",  "do",  "you",  "have",  "a",  "favorite",  "city",  "to",  "live",  "in",  "yes",  "it",  "is",  "new",  "york"]
print("Assertion result 1: ", chatBot(conversations, currentConversation)==expected)

conversations= [["lets","have","some","fun"], 
 ["i","never","get","it"], 
 ["be","aware","of","this","house"], 
 ["he","will","call","her"]]
currentConversation= ["can", 
 "you", 
 "please"]
expected=["can", 
 "you", 
 "please"]
print("Assertion result 2: ", chatBot(conversations, currentConversation)==expected)

conversations= [["it","is","my","favorite","movie"], 
 ["really","i","did","not","know"]]
currentConversation= ["what", 
 "you", 
 "think", 
 "about", 
 "this", 
 "movie"]
expected = ["what", 
 "you", 
 "think", 
 "about", 
 "this", 
 "movie"]
print("Assertion result 3: ", chatBot(conversations, currentConversation)==expected)

conversations= [["tonight","i","need","dollar","bills"], 
 ["i","dont","keep","fun"], 
 ["cheap","thrills","long","to","feel","money"], 
 ["the","bills","dont","need","the","dancing","baby"], 
 ["fun","dollar","dancing","thrills","the","baby","i","need"], 
 ["dont","have","fun"], 
 ["no","no","dont","have","dancing","fun","tonight"]]
currentConversation= ["beat", 
 "the", 
 "can", 
 "as", 
 "i", 
 "dont", 
 "feel", 
 "thrills"]
expected = ["beat", 
 "the", 
 "can", 
 "as", 
 "i", 
 "dont", 
 "feel", 
 "thrills", 
 "need"]
print("Assertion result 4: ", chatBot(conversations, currentConversation)==expected)

conversations= [["fame","what","you","like","is","in","the","limo"], 
 ["fame","what","you","get","is","no","tomorrow"], 
 ["fame","what","you","need","you","have","to","borrow","fame"], 
 ["fame","its","mine","its","mine","its","just","his","line"], 
 ["to","bind","your","time","it","drives","you","to","crime"]]
currentConversation= ["what", 
 "is"] 
expected = ["what", 
 "is", 
 "in", 
 "the", 
 "limo"] 
print("Assertion result 5: ", chatBot(conversations, currentConversation)==expected)
