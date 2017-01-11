dna_file = open('rosalind_rna-2.txt', 'r')
dna = dna_file.read()
rna = ''
for letter in dna:
    if letter == 'T':
        rna += 'U'
    else:
        rna += letter

dna_file.close()
print rna