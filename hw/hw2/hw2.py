# BT3051 Assignment 2
#Roll number : BE14B002
# Collaborators : None
#Time: 2:00
class 	DNA:
	def __init__(self,fasta=None,seq_string=None): 
		if fasta is not None and seq_string is not None:
			raise ValueError("Can't use both fasta file and dna string")
		elif fasta is None and seq_string is None:
			raise ValueError("Use  one of fasta or dna string")
		elif fasta is not None:
			self._dna=self._read_fasta(fasta)
		else:
			self._dna=seq_string
	def __repr__(self):
		return self._dna
	def _read_fasta(self,fname):
		""" (str) -> (str)
		# function body with documentation
		"""
		seq=[]
		sequences=[]
		with open(fname) as file:
			name=file.readline()
			dna=file.readline()
			while dna[0]!=">":    #assuming only first sequence needs to be read
				seq.append(dna.strip()) 
				dna=file.readline()
				if dna=="":
					break
			seq="".join(seq)
			return seq
	def get_comple_strand(self):
		""" (DNA) -> (DNA)
		>>> DNA(seq_string="AAAACCCGGT").get_comple_strand()
		ACCGGGTTTT
		"""
		_cdna=""
		swap={'A':'T','T':'A','G':'C','C':'G'}
		for ichar in "".join(reversed(self._dna)):
			_cdna+=swap[ichar]
		return (DNA(seq_string=_cdna))
	def get_base_counts(self):
		""" (DNA) -> (dict)
		>>> DNA(seq_string="AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC").get_base_counts() == {'A': 20, 'T': 21, 'G': 17, 'C': 12}
		True
		"""
		_acount=self._dna.count("A")
		_tcount=self._dna.count("T")
		_gcount=self._dna.count("G")
		_ccount=self._dna.count("C")
		_countdict={"A":_acount,"T":_tcount,"G":_gcount,"C":_ccount}
		return _countdict
	def transcribe(self):
		""" (DNA) -> (str)
		>>> DNA(seq_string="GATGGAACTTGACTACGTAAATT").transcribe()
		'GAUGGAACUUGACUACGUAAAUU'
		"""
		_mrna=self._dna.replace("T","U")
		return _mrna
	def get_GC(self):
		""" (DNA) -> (float)
		>>> DNA(seq_string="CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGACTGGGAACCTGCGGGCAGTAGGTGGAAT").get_GC()
		60.92
		"""
		_gccount=self._dna.count("G")
		_gccount+=self._dna.count("C")
		_per=_gccount*100/len(self._dna)
		_per=float("%.2f" %_per)
		return _per
	def locate_restriction_sites(self):
		""" (DNA) -> (list of tuples)
		>>> DNA(seq_string="TCAATGCATGCGGGTCTATATGCAT").locate_restriction_sites()
		[(5, 4), (7, 4), (17, 4), (18, 4), (21, 4), (4, 6), (6, 6), (20, 6)]
		>>> DNA(seq_string="TCAATGCA").locate_restriction_sites()
		[(5, 4)]
		>>> DNA(seq_string="TCA").locate_restriction_sites()
		'The DNA size is less than 4'
		"""
		_dnalen=len(self._dna)
		pallist=[]
		if(_dnalen>=12):
			for _ilen in range(4,13):
				for _jlen in range(0,_dnalen-_ilen+1):
					if repr(DNA(seq_string=self._dna[_jlen:_jlen+_ilen]).get_comple_strand()) == self._dna[_jlen:_jlen+_ilen]:
						pallist.append((_jlen+1,_ilen))
		elif(_dnalen>=4):
			for _ilen in range(4,_dnalen+1):
				for _jlen in range(0,_dnalen-_ilen+1):
					if repr(DNA(seq_string=self._dna[_jlen:_jlen+_ilen]).get_comple_strand()) == self._dna[_jlen:_jlen+_ilen]:
						pallist.append((_jlen+1,_ilen))
		else:
			return("The DNA size is less than 4")
		return(pallist)

			

import doctest
if __name__ == '__main__':
	doctest.testmod(verbose = True)

if __name__ == '__main__':
	strand= DNA("hw2_dataset.faa")
	comple_strand=strand.get_comple_strand()
	base_counts=strand.get_base_counts()
	mrna=strand.transcribe()
	gc_content=strand.get_GC()
	restriction_sites=strand.locate_restriction_sites()
	print(strand,comple_strand,base_counts,mrna,gc_content,restriction_sites,sep="\n")