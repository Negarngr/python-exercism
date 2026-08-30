dna_to_rna = {"A": "U", "T": "A", "C": "G", "G": "C"}
def to_rna(dna_strand):
    result = ""
    for i in dna_strand:
       result += dna_to_rna[i]
    return result
