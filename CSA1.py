#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 12:18:06 2016

@author: NMAI
"""

from collections import Counter
from string import punctuation
import os



# Set chrwd
cwd = os.getcwd()
os.chdir("/Users/NMAI/Desktop/NetBeansProjects")

    
# Input text
textwords = open('doc1.txt', 'r').read().split()
stopwords = open('stopWords.txt', 'r').read().split()


# Remove stopwords
resultwords  = [word for word in textwords if word.lower() not in stopwords]
wordlist = ' '.join(resultwords)
print(wordlist)

# Use Counter to return object of ('K',V) pairs
tenmostfreq=Counter(resultwords).most_common(10)
print(tenmostfreq)



# Compute cosine similarity

# Input text
textwords1 = open('doc1.txt', 'r').read().split()
textwords2 = open('doc2.txt', 'r').read().split()


# Remove stopwords
resultwords1  = [x for x in textwords1 if x.lower() not in stopwords]
wordlist1 = ' '.join(resultwords1)

resultwords2  = [y for y in textwords2 if y.lower() not in stopwords]
wordlist2 = ' '.join(resultwords2)

# Use Counter to return object of ('K',V) pairs
mostfreq1=Counter(resultwords1).most_common()
mostfreq2=Counter(resultwords2).most_common()


# Calculate Cosine Similarity

# Dot Product
acol1, acol2 = zip(*mostfreq1)
bcol1, bcol2 = zip(*mostfreq2)


sum(acol2)
sum(bcol2)