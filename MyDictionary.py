import json
from difflib import get_close_matches
from os import name
from tkinter import *

#Creating a window for the dictionary
window=Tk()
window.title("Dictionary")
#Loading data from json file to a variable data
data=json.load(open("data.json","r"))

#Building an entry widget where a user can type a word 
e=Entry(window,bg="#ABB8B8",width=50,borderwidth=5,font=("Times New Roman",13))

#Building a text widget in which users will see the meaning to the word they entered 
t1=Text(window,height=15,width=48,borderwidth=2,bg="#ABB8B8",font=("Times New Roman",15))

#This function get the meaning of a word a users enters from the json file 
def word_meaning():
    global word 
    #This get the word a user enters from the GUI pass it as a String and store it in the variable word 
    word=str(e.get()).lower()
    if word in data.keys():
        list_to_sentence()

    #Suggest likely word to a user should he/she enter a wrong word in the entry widget    
    elif len(get_close_matches(word,data.keys()))>0: #Get all words that have close match with word a user enters
        t1.delete(1.0,END)
        suggested_word=get_close_matches(word,data.keys())[0]  #Get closest word similer to a word a user input and store it in the variable
        global suggested_word_
        suggested_word_=str(suggested_word)
        word=suggested_word_
        t1.insert(END,"Did you mean %s. If Yes press the Yes Button if No press the No Button: "%suggested_word_)


#Because the json file is in a dictionary form, if a word has two or more meaning, the meaning of the word is displayed in a list form.
# So this fuction changes the meaning of the word from a list to a sentence form
def list_to_sentence():
    output=data[word]
    if type(output)==list:
        for line in output:
            #Display meaning of word in the text widget/window
            t1.insert(END,line+"\n")
    else:
        t1.insert(END,output)

  #The meaning of a word is searched when a user click on the Yes Button
def yes_button():
        t1.delete(1.0,END)
        list_to_sentence()

def no_button():  #Display Word not found if a user click on the No button
    t1.delete(1.0,END)
    t1.insert(END, "Word not found")





enter_button=Button(window,text="Enter",bg="#A9CCCC",padx=25,pady=6,command=word_meaning) #Design's the Enter button
yes_button=Button(window,text="Yes",bg="#A9CCCC",padx=25,pady=6,command=yes_button) #Design's the Yes button
no_button=Button(window,text="No",bg="#A9CCCC",padx=25,pady=6,command=no_button)  #Design's the No button

#Arrange all the widgets on the GUI
e.grid(row=0,column=0,columnspan=3,padx=15)
enter_button.grid(row=2,column=0)
yes_button.grid(row=2,column=1)
no_button.grid(row=2,column=2)
t1.grid(row=1,column=0,columnspan=3)

window.mainloop()




