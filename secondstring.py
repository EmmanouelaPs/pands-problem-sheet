sentence = input("Please enter a sentence:The quick brown fox jumps over the lazy dog.")#asks from the user to type: The quick brown fox jumps over the lazy dog
type(sentence)#check what is the type of my variable as we want it to be a string
print (sentence)#print variable to make sure its working
#for i in sentence[::-2]:#print every second letter in sentence starting from the end
    #print(i)
NewSentence = sentence[::-2]#save output into a new string
print (NewSentence)#print new string


