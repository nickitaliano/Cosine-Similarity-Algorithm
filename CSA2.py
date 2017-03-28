#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 13:44:42 2016

@author: NMAI
"""

# Calculate Cosine Similarity
import math	
from collections import Counter


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
cosine = dot / (len_a * len_b)                         
