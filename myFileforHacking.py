import sys
import csv
import nltk
from nltk.corpus import wordnet
import re
import codecs
import pprint
'''
# return true if a string ia a stopword
def is_stopword(string):
    if string.lower() in nltk.corpus.stopwords.words('english'):
        return True
    else:
        return False

    # return true if a string is punctation    
def is_punctuation(string):
    for char in string:
        if char.isalpha() or char.isdigit():
            return False
    return True

# Translation from nltk to Wordnet (words tag) (code)
def wordnet_pos_code(tag):
    if tag.startswith('NN'):
        return wordnet.NOUN
    elif tag.startswith('VB'):
        return wordnet.VERB
    elif tag.startswith('JJ'):
        return wordnet.ADJ
    elif tag.startswith('RB'):
        return wordnet.ADV
    else:
        return ''

    
# Translation from nltk to Wordnet (words tag) (label)
def wordnet_pos_label(tag):
    if tag.startswith('NN'):
        return "Noun"
    elif tag.startswith('VB'):
        return "Verb"
    elif tag.startswith('JJ'):
        return "Adjective"
    elif tag.startswith('RB'):
        return "Adverb"
    else:
        return tag
    

""" input -> a sentence 
    otput -> sentence in which each words is enriched of -> lemma, wordnet_pos, wordnet_definitions 

"""
def wordnet_definitions(sentence):
    wnl = nltk.WordNetLemmatizer()
    for token in sentence:
        word = token['word']
        wn_pos = wordnet_pos_code(token['pos'])
        if is_punctuation(word):
            token['punct'] = True
        elif is_stopword(word):
            pass
        elif len(wordnet.synsets(word, wn_pos)) > 0:
            token['wn_lemma'] = wnl.lemmatize(word.lower())
            token['wn_pos'] = wordnet_pos_label(token['pos'])
            defs = [sense.definition for sense in wordnet.synsets(word, wn_pos)]
            token['wn_def'] = "; \n".join(defs) 
        else:
            pass
    return sentence

'''
#Tokenization

def tag_tweet(tweet):    
    sents = nltk.sent_tokenize(tweet)
    sentence = []
    for sent in sents:
        tokens = nltk.word_tokenize(sent)
        print (tokens)
        tag_tuples = nltk.pos_tag(tokens)
        print (tag_tuples)
        for (string, tag) in tag_tuples:
            token = {'word':string, 'pos':tag}            
            sentence.append(token)    
    return sentence

path = nltk.data.find('c:/doc.txt',)

#f = open(path,'rU',encoding='latin2')
#f = open(path,'rU',encoding='utf-8')

f = open(path,'r')
for line in f:
    line = line.strip()
    #line  = line.encode('unicode_escape')
    #line  = line.encode('utf8')
    print (tag_tweet (line))
    
'''
sentences = ['The movie was the worst movie', 'It was the worst acting by the actors']

for sentence in sentences:
    final = tag_tweet (sentence)
    print (final)
    
'''