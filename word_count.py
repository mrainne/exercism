from string import punctuation
from collections import Counter
import re

def word_count(words):
    """Given a phrase, count the occurrences of each word in that phrase."""
        
    # replace punctuation and special characters with whitespace
    # change case to lowercase
    # split words to list
    word_list = re.sub("[\W_]+", " ", words).lower().split()
    
<<<<<<< HEAD
    # dictionary where words are used as keys and values are set to 0.
    counts = {word : 0 for word in set(word_list)}
=======
    # create counter variable to count and store words
    counts = Counter() 
>>>>>>> 6c2df20 (Add files via upload)
    
    for word in word_list:
    	counts[word] += 1 
    		
    return counts

			
	
	    
    
