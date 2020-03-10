
print("Input N:")
N = int(input())
arr = []
if (N == 1) :
    arr.append(int(input()))
    print("Only one element.")
    print(arr[0])
elif (N < 1) :
    print("Invalid size.")
else :
    new = []
    for i in range(N):
        arr.append(int(input()))
    for i in range(1, len(arr) +1):
        new.append(arr[-i])
    s = " ".join(str(new))
    print(s)
