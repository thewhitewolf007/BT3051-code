def _Transcribing_DNA_to_RNA(_str):
	""" Given a DNA string tt corresponding to a coding strand,
	its transcribed RNA string uu is formed by replacing all occurrences of 'T' in tt with 'U' in uu."""
	_count_T= 0
	for char in _str:
		if(char == 'T'):
			_count_T+=1
	print(_count_T)
	_str.replace("T","U")  # What's wrong with this?
	print(_str)

_Transcribing_DNA_to_RNA('ACGT')

