# your code goes here!
#class Anagram:
    
     #def constructur(self and word)
         #set self.word = word
     #def match(self, word_list = list())
         #
from collections import Counter
class Anagram:

    def __init__(self, word):
        self.word = word
        pass
    def match(self, word_list):
        anagram_list = list()

        for word_value in word_list:
            if Counter(word_value) == Counter(self.word):
                anagram_list.append(word_value)
            else:
                anagram_list 
        return anagram_list



        pass

listen = Anagram("pay")
print(listen.match(['enlists', 'google', 'inlets', 'yap']))