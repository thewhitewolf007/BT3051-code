def read_fasta(fname):
		""" (str) -> (list of strings)
		# function body with documentation
		"""
		seq=[]
		sequences=[]
		with open(fname) as file:
			name=file.readline()
			dna=file.readline()
			while dna[0]!=">":
				seq.append(dna.strip("\n")) 
				dna=file.readline()
			seq="".join(seq)
			return seq

fasta="hw1a_dataset.faa"
print(read_fasta(fasta))