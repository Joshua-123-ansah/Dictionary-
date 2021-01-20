import json
from difflib import get_close_matches
from os import name
from tkinter import *

window=Tk()
window.title("Dictionary")
data=json.load(open("data.json","r"))

e=Entry(window,bg="#ABB8B8",width=50,borderwidth=5,font=("Times New Roman",13))
t1=Text(window,height=15,width=48,borderwidth=2,bg="#ABB8B8",font=("Times New Roman",15))

def word_meaning():
    global word
    word=str(e.get()).lower()
    if word in data.keys():
        list_to_sentences()
  
    elif len(get_close_matches(word,data.keys()))>0:
        t1.delete(1.0,END)
        suggested_word=get_close_matches(word,data.keys())[0]
        global suggested_word_
        suggested_word_=str(suggested_word)
        word=suggested_word_
        t1.insert(END,"Did you mean %s. If Yes press the Yes Button if No press the No Button: "%suggested_word_)

def list_to_sentences():
    output=data[word]
    if type(output)==list:
        for line in output:
            t1.insert(END,line+"\n")
    else:
        t1.insert(END,output)

def yes_button():
    t1.delete(1.0,END)
    list_to_sentences()

def no_button():
    t1.delete(1.0,END)
    t1.insert(END, "Word not found")


enter_button=Button(window,text="Enter",bg="#A9CCCC",padx=25,pady=6,command=word_meaning)
yes_button=Button(window,text="Yes",bg="#A9CCCC",padx=25,pady=6,command=yes_button)
no_button=Button(window,text="No",bg="#A9CCCC",padx=25,pady=6,command=no_button)

e.grid(row=0,column=0,columnspan=3,padx=15)
enter_button.grid(row=2,column=0)
yes_button.grid(row=2,column=1)
no_button.grid(row=2,column=2)
t1.grid(row=1,column=0,columnspan=3)



window.mainloop()




