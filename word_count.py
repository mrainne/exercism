from string import punctuation

def word_count(words):
    """Given a phrase, count the occurrences of each word in that phrase."""
        
    # replace punctuation and special characters with whitespace
    # change case to lowercase
    # strip extra whitespace
    # split words to list
    translationTable = words.maketrans(punctuation, " " * len(punctuation))
    word_list = words.translate(translationTable).lower().strip().split()
    
    # dictionary variable for saving words and word counts
    counts = {}
    
    for word in word_list:
    	if word not in counts:
    		counts[word] = 1
    	else:
    		counts[word] += 1 
    		
    return counts

			
	
	    
    