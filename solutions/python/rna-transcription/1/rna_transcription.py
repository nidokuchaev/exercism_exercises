def to_rna(dna_strand):
    transcription = {'G': 'C', 'C': 'G', 'T': 'A', 'A': 'U'}
    return ''.join([transcription[n] for n in dna_strand])