codonTable = dict(
UUU = 'F', CUU = 'L', AUU = 'I', GUU = 'V', UUC = 'F', CUC = 'L', AUC = 'I', GUC = 'V',
UUA = 'L', CUA = 'L', AUA = 'I', GUA = 'V', UUG = 'L', CUG = 'L', AUG = 'M', GUG = 'V',
UCU = 'S', CCU = 'P', ACU = 'T', GCU = 'A', UCC = 'S', CCC = 'P', ACC = 'T', GCC = 'A',
UCA = 'S', CCA = 'P', ACA = 'T', GCA = 'A', UCG = 'S', CCG = 'P', ACG = 'T', GCG = 'A',
UAU = 'Y', CAU = 'H', AAU = 'N', GAU = 'D', UAC = 'Y', CAC = 'H', AAC = 'N', GAC = 'D',
UAA = 'Stop', CAA = 'Q', AAA = 'K', GAA = 'E', UAG = 'Stop', CAG = 'Q', AAG = 'K', GAG = 'E',
UGU = 'C', CGU = 'R', AGU = 'S', GGU = 'G', UGC = 'C', CGC = 'R', AGC = 'S', GGC = 'G',
UGA = 'Stop', CGA = 'R', AGA = 'R', GGA = 'G', UGG = 'W', CGG = 'R', AGG = 'R', GGG = 'G',
)

rnaf = open('rosalind_prot.txt', 'r')
codon = ''
pro = ''

rna = rnaf.read()
rnaf.close()
if '\n' in rna:
    rna = rna.replace('\n', '')

i = 0
while i in range(0,len(rna)):
    for count in range(0,3):
        codon += rna[i]
        i += 1
    if not (codon == 'UAA' or codon == 'UGA' or codon == 'UAG'):
        pro += codonTable[codon]
    codon = ''
print pro
