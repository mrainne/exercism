def is_pangram(sentence):
	""" Determine if all of the alphabets occur at least once in a sentence. """

	# alphabets
	alphabet = "abcdefghijklmnopqrstuvwxyz"

	for c in alphabet:
		# alphabet must occur either in lowercase or uppercase
		if  (c.lower() not in sentence) and (c.upper() not in sentence):
			return False
			break
	
	return True
