N = int(input()) 
comp = 0
while (10**comp < N):
    comp = comp + 1

print(comp)


i = 0
lulus = 0
charArray = []
for i in range(50) :
    check = input()
    charArray.append(check)
    if (check == 'A') or (check == 'B') or (check == 'C'):
        lulus += 1
print(lulus)


U = []
V = []
W = []

for i in range(5):
    print("Masukan U :")
    U.append(int(input()))
    print("Masukan V :")
    V.append(int(input()))
    W.append(U[i]+V[i])

teksOutU = " ".join(str(U))
teksOutV = " ".join(str(V))
teksOutW = " ".join(str(W))
print("Vektor U :")
print(teksOutU)
print("Vektor V :")
print(teksOutV)
print("Vektor W :")
print(teksOutW)

suhu = []
for i in range(30):
    suhu.append(float(input()))
for i in range(30):
    print("Suhu untuk %s September 2018 adalah : %s celsius." % (str(i+1),str(suhu[i])))