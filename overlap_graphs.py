import string

file = open('/Users/apple/Documents/Study/ComputerScience/ProgramingLanguage/GitHub/SimplePython/txtFiles\
/rosalind_grph.txt', 'r')

seq_dict = {}
seq = ''
name = ''
b = True

while b:
    line = file.readline()

    if line == '':
        b = False
        seq_dict.keys().append(name)
        seq_dict[name] = seq
    if '>' in line:
        if name != '':
            seq_dict.keys().append(name)

        if seq != '':
            seq_dict[name] = seq
            seq = ''

        name = line.replace('\n', '')

    if '>' not in line:
        seq = seq + line.replace('\n', '')
