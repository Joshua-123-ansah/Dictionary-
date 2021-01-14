import json
from difflib import get_close_matches
data=json.load(open("data.json","r"))
run=True
while run:
    word=input("Enter a word: ").lower()
    if word in data.keys():
        output1=data[word]
        if type(output1)==list:
            for i in output1:
                print(i)
        else:
            print(output1)
    elif len(get_close_matches(word,data.keys()))>0:
        suggested_word=get_close_matches(word,data.keys())[0]
        user_opinion=input("Did you mean %s instead. Enter Y if Yes and N if No: "%suggested_word).lower()
        if user_opinion=="y":
            output2=data[suggested_word]
            if (output2)==list:
                for i in output2:
                    print(i)
            else:
                print(output2)
        else:
            print("Word not found")
    else:
        print("Word not found")
  


