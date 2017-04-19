def is_pangram(sentence):
	""" Determine if all of the alphabets occur at least once in a sentence. """

	# alphabets
	alphabet = set('abcdefghijklmnopqrstuvwxyz')

	# remove duplicates non-alphabetic characters from sentence
	# and make it lowercase
	new_sentence = set(sentence.lower())
	
	# if sentence is pangram alphabet minus new_sentence return empty set
	# (False).
	return not alphabet - new_sentence
