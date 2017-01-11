aa_mass = dict(
    A = 71.03711, C = 103.00919, D = 115.02694, E = 129.04259, F = 147.06841, G = 57.02146, H = 137.05891, I = 113.08406,
    K = 128.09496, L = 113.08406, M = 131.04049, N = 114.04293, P = 97.05276, Q = 128.05858, R = 156.10111, S = 87.03203,
    T = 101.04768, V = 99.06841, W = 186.07931, Y = 163.06333
)

prof = open('rosalind_prtm.txt', 'r')
pro = prof.read()

mass = 0
water = 18.01056

for aa in pro:
    if aa != '\n':
        mass += aa_mass[aa]

mass = mass - water * (len(aa) - 1)

print mass