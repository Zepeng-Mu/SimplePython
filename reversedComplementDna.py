dna_file = open('rosalind_revc.txt', 'r')
dna = dna_file.read()
cdna = ''

for letter in dna:
    if letter == 'A':
        cdna += 'T'
    elif letter == 'T':
        cdna += 'A'
    elif letter == 'G':
        cdna += 'C'
    elif letter == 'C':
        cdna += 'G'

dna_file.close()
revcdna = cdna[::-1]
print revcdna