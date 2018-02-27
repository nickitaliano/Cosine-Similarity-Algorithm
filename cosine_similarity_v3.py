#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 13:51:20 2016

@author: NMAI
"""

"""
# Clear Variables
# "%reset" in console before running each time
"""

import math	
from collections import Counter
from string import punctuation
import os
import subprocess as sp

# Set cwd
cwd = os.getcwd()
os.chdir("/YOUR/FAVORITE/WORKING/DIRECTORY")
    
# Input text
t1 = open('doc1.txt', 'r',encoding='utf8', errors='replace')#function designated for frequency
textwords1=t1.read().split()
t2 = open('doc2.txt', 'r',encoding='utf8', errors='replace')
textwords2=t2.read().split()
stopwords = open('stopWords.txt', 'r').read().split()

# Remove stopwords
resultwords1  = [word for word in textwords1 if word.lower() not in stopwords]
resultwords2  = [word for word in textwords2 if word.lower() not in stopwords]

# count word occurrences
a_vals = Counter(resultwords1)
b_vals = Counter(resultwords2)

# convert to word-vectors
words  = list(a_vals.keys() | b_vals.keys())
a_vect = [a_vals.get(word, 0) for word in words]        
b_vect = [b_vals.get(word, 0) for word in words]        

# find cosine
len_a  = sum(av*av for av in a_vect) ** 0.5             
len_b  = sum(bv*bv for bv in b_vect) ** 0.5             
dot    = sum(av*bv for av,bv in zip(a_vect, b_vect))    
cosinesim = dot / (len_a * len_b) 
print(cosinesim)




# Use Counter to return object of ('K',V) pairs
tenmostfreq=Counter(resultwords1).most_common(10)
print(tenmostfreq)

