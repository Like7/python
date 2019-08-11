#se's file
#text files provided for testing

"""
this is the (second draft of the actual project) ui of the initial project that aims to count words in a text and then gradually in time group up words and
common phrases etc.

next idea - group common words (based on frequency of coupling e.g. "how are" : 3)

later idea - basic autofill (google auto-fill - for reference). This will be based on data collected from 1,000,000+ text dumps.
"""

#usage
"""
start: - this is for clearing before entering new words (optional). just type 'clear'. enter to continue
input file : - entire file (text) name. or type "null" to exit
.. - enter to continue. made to pause and not quit automatically
"""



#why not json? pickle is python specific (i only intend to use python) and json can't handle some python stuff etc - see docs 
import pickle
import sys

class UI():

    def __init__(self):
        data = open("word_dump.txt", mode="rb")
        self.word_list = pickle.load(data)

    def clear_dict(self):
        self.word_list.clear()
        with open("word_dump.txt", mode="wb") as data:
                pickle.dump(self.word_list, data)
            

    def run(self):
        y = input("start: ")
        if y == "clear":
            self.clear_dict()
            
        path = input("input file : ")
        if path == "null":
            
            input("..")
            sys.exit(1)
            
        self.file = open(path,'r')
        self.file = self.file.read()
        self.word_counter(self.file)
        
        print(self.word_list)
        input("\n..\n")

            

    def addWord(self, word, counter):
            self.word_list.update({word: counter})

    def word_counter(self,text):
        #basic non-letters
        non_letters = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', ':', ';', '<', '=', '>', '?', '/','\\', '\n',]
        text = text.lower()
        for i in non_letters:
            if i in non_letters:
                 text = text.replace(i, '')
                
        words = text.split(' ')
        for i in words:
            if i in self.word_list:
                self.word_list[i] += 1
            else:
                self.addWord(i,1)

        with open("word_dump.txt", mode="wb") as data:
            pickle.dump(self.word_list, data)
                    
   

x = UI()
x.run()

#this is not my code. added just before upload so didnt really examine it. (last part of program)
listofTuples = sorted(x.word_list.items() , reverse=True, key=lambda x: x[1])
for elem in listofTuples :
    print(elem[0] , " ::" , elem[1] ) 
        
input("\nexit..")
