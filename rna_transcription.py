def to_rna(sequence):
	"""Given a DNA strand, return its RNA complement (per RNA transcription)."""
	
	# copy DNA sequence and make it uppercase
	dna_seq = sequence.upper()
	
	# RNA sequence
	rna_seq = ''
	
	# check DNA sequence one by one from first to last 
	for i in range(0, len(dna_seq)):
		if  dna_seq[i] == 'G':
			rna_seq += 'C'
		elif dna_seq[i] == 'C':
			rna_seq += 'G'
		elif dna_seq[i] == 'T':
			rna_seq += 'A'
		elif dna_seq[i] == 'A':
			rna_seq += 'U'
		else:  # sequence is invalid, set rna_seq to empty string and stop
			rna_seq = ''
			break
				
	return rna_seq
   						
	
	
