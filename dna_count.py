dna_file = open('rosalind_dna.txt', 'r')
dna = dna_file.read()
a = dna.count('A')
c = dna.count('C')
g = dna.count('G')
t = dna.count('T')
print(a,c,g,t)
dna_file.close()