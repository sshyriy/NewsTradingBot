
"""
News Trading Bot
"""

import pandas
from nltk.tokenize import word_tokenize
import nltk
import os
from nltk.parse import stanford
import nltk.corpus
from nltk.corpus import brown
from nltk import ne_chunk

from nltk.chunk import *
from nltk.chunk.util import *
from nltk.chunk.regexp import *
from nltk import Tree

# read data and create a dictionary with date = key and headline = value
df = pandas.read_csv('guardian_headlines.csv', header=None, index_col=0, squeeze=True).to_dict()
amazon = "Concerns over safety at Amazon warehouses as accident reports rise"
#words for further parsing
good = open("WORDS/PositiveWords.txt", "r")
bad = open("WORDS/NegativeWords.txt", "r")

#companies to search for in the articles
tickers = ['amazon', 'apple', 'yahoo', 'tesla', 'cvs']

#read the txt files with words and put them into lists
good_words = good.read()
good_list = good_words.split()

bad_words = bad.read()
bad_list = bad_words.split()

#tokenize the values in the dictionary and make them all lower case
for key in df:
   df[key] = word_tokenize(str(df[key]).lower())


bad_list_dict = {}
good_list_dict = {}


#loop through dictionary
for k,v in df.items():
    for token in v:
        if token in tickers : #if the value contains a tocken with the ticker
            for token2 in v:
                if token2 in bad_list: # and if the value contains a tocken with a word from bad_list
                    bad_list_dict.update({k:v}) #add to the dictionary 
                elif token2 in good_list:
                    good_list_dict.update({k:v})#add to the other dictionary
   
new_tokens = nltk.pos_tag(word_tokenize(amazon))                    
grammer_np = r"NP: {<DT>?<JJ>*<NN>}"
chunk_parser = nltk.RegexpParser(grammer_np)  

chunk_result = chunk_parser.parse(new_tokens)
print(chunk_result)
#print("bad list", bad_list_dict)
#print("\ngood list", good_list_dict)



    
  

