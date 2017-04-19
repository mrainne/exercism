def distance(dna1, dna2):
	""" Calculate the Hamming difference between two DNA strands. Strands should have equal lenght. Hamming difference is the number of differences is the strands. For equal or empty strands the diffrence is zero."""
	
	# set difference to 0 
	hamming = 0
	
	
	if len(dna1) != len(dna2):
		raise ValueError('Strands should have same length.')
	else:	
		for i in range(0, len(dna1)):	
			if dna1[i] != dna2[i]:
				hamming += 1
					
	return  hamming
