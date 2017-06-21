#!/usr/local/bin python3

import matplotlib.pyplot as plt
water = 18.01056

#Mw of aa below already has one water molecule subtracted
aaMw = dict(
    A = 71.0788, C = 103.1388, D = 115.0886, E = 129.1155, F = 147.1766, G = 57.0519, H = 137.1411, I = 113.1594,
    K = 128.1741, L = 113.1594, M = 131.1926, N = 114.1038, P = 97.1167, Q = 128.1307, R = 156.1875, S = 87.0782,
    T = 101.1051, V = 99.1326, W = 186.2132, Y = 163.1760
)

water = 18.01056
myDic = {}

def calMw(pro):
    mass = 0
    for aa in pro:
        if aa != "\n":
            mass += aaMw[aa]
    
    mass = (mass + water) / 1000
    return mass

f = open("NP_001286412.txt", "r")

for lines in f:
    lines = lines.replace("\n", "")
    if lines.startswith(">"):
        name = "1"
        if name not in myDic.keys():
            myDic[name] = ""
    else:
        myDic[name] += lines

step = 0
length = []
mw1 = []
mw2 = []
while (step + 10) <= len(myDic["1"]):
    step += 10
    length.append(step)
    mw1.append(calMw(myDic["1"][0:step]))
    mw2.append(0.12 * step)
print(mw1)
plt.axis([0, 950, 0, 115])
plt.title("Cumulated Molecular Weight of NP_001286412")
plt.xlabel("Length")
plt.ylabel("Mw(kDa)")
plt.plot(length, mw1, "k-", length, mw2, "k--", lw = 0.6)
plt.legend(["Calculated", "Estimated"])
plt.savefig("protein.png")
