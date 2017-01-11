gcf = open('rosalind_gc.txt', 'r')
lines = ''
lens = 0
gc = 0
b = True
while b:
    lines = gcf.readline()
    if lines == '':
        b = False
        print (float(gc) / float(lens)) * 100
    if '>' in lines:
        if lens != 0:
            print (float(gc) / float(lens)) * 100
        print lines,
        gc = lens = 0
    else:
        lens = lens + len(lines) - lines.count('\n')
        gc = gc + lines.count('G') + lines.count('C')

gcf.close()