def is_pangram(sentence):
	""" Determine if all of the alphabets occur at least once in a sentence. """

	# alphabets
	alphabet = set('abcdefghijklmnopqrstuvwxyz')

	new_sentence = set(sentence.lower())
	
	return not alphabet - new_sentence
