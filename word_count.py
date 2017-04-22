from string import punctuation

def word_count(words):
    """Given a phrase, count the occurrences of each word in that phrase."""
        
    # replace punctuation and special characters with whitespace
    # change case to lowercase
    # strip extra whitespace
    # split words to list
    translationTable = words.maketrans(punctuation, " " * len(punctuation))
    word_list = words.translate(translationTable).lower().strip().split()
    
    # dictionary where words are used as keys and values are set to 0.
    counts = {word : 0 for word in set(word_list)}
    
    for word in word_list:
    	counts[word] += 1 
    		
    return counts

			
	
	    
    