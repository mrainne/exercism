from string import punctuation
from collections import Counter
import re

def word_count(words):
    """Given a phrase, count the occurrences of each word in that phrase."""
        
    # replace punctuation and special characters with whitespace
    # change case to lowercase
    # split words to list
    word_list = re.sub("[\W_]+", " ", words).lower().split()
    
    # create counter variable to count and store words
    counts = Counter() 
    
    for word in word_list:
    	counts[word] += 1 
    		
    return counts

			
	
	    
    
