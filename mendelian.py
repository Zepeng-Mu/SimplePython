a = 23
b = 15
c = 19

total = a + b + c

D = float(a)/total
H = float(b)/total
H1 = float(b)/(total - 1)
H2 = float(b - 1)/(total - 1)
R = float(c)/total
R1 = float(c - 1)/(total - 1)

print H1 * R * 0.5 * 2

result = 1 - R * R1 - H1 * R * 0.5 * 2 - H * H2 * 0.25
print result

