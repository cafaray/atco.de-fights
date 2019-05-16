def chatBot(conversations, currentConversation):
    
    maxWords = -1
    maxRow = -1
    maxPointer = -1
    pointer = -1
    d = {}    
    for conversation in range(len(conversations)):
        for word in range(len(currentConversation)):
            if currentConversation[word] in conversations[conversation]:
                d[conversation] = d.get(conversation, 0) + 1
                pointer = word        
        if d.get(conversation,-1)>maxWords:
            maxWords = d.get(conversation)
            maxRow = conversation
            maxPointer = pointer
    print(d)
    print("maxWords is", maxWords)
    print("maxRow is", maxRow)
    print("maxPointer in", maxPointer)


conversations= [["where","are","you","live","i","live","in","new","york"], 
 ["are","you","going","somewhere","tonight","no","i","am","too","tired","today"], 
 ["hello","what","is","your","name","my","name","is","john"]]

currentConversation= ["hello", 
 "john", 
 "do", 
 "you", 
 "have", 
 "a", 
 "favorite", 
 "city", 
 "to", 
 "live", 
 "in", 
 "yes", 
 "it", 
 "is"]
expected=["hello", 
 "john", 
 "do", 
 "you", 
 "have", 
 "a", 
 "favorite", 
 "city", 
 "to", 
 "live", 
 "in", 
 "yes", 
 "it", 
 "is", 
 "new", 
 "york"]



conversations= [["lets","have","some","fun"], 
 ["i","never","get","it"], 
 ["be","aware","of","this","house"], 
 ["he","will","call","her"]]
currentConversation0 ["can", 
 "you", 
 "please"]
expected=["can", 
 "you", 
 "please"]

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