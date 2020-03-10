
def sortArr(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            arr[i],arr[i + 1] = arr[i + 1], arr[i]
    return arr

arrA = []
arrB = []
NA = int(input("Input number of elements in A : "))
for i in range(NA):
    arrA.append(int(input("Input element A number %d : " %(i+1))))
NB = int(input("Input number of elements in B:"))
for i in range(NB):
    arrB.append(int(input("Input element B number %d : " %(i+1))))
if (sortArr(arrA) == sortArr(arrB)) :
    print("B is an anagram of A")
else :
    print("B is not an anagram of A")