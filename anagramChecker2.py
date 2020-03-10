strInput = str(input("Input string : "))
arrChar = list(strInput)
arrReverse = []
for i in range(1, len(arrChar) +1):
        arrReverse.append(arrChar[-i])

if (arrChar == arrReverse):
    print("%s is an anagram." % (strInput))
else :
    print("%s is not an anagram." % (strInput))