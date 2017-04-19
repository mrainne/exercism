def is_pangram(sentence):
	""" Determine if all of the alphabets occur at least once in a sentence. """

	# alphabets
	alphabet = set('abcdefghijklmnopqrstuvwxyz')
	
	# remove duplicate letters and non-alphabetic letters from sentence and set it lowercase letters.
	new_sentence = set(sentence.lower())
	
	# if alphabet minus new_sentence returns empty set (False) the sentence is pangram.
	return not alphabet - new_sentence
