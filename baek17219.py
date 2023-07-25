str = input()
str_ = str.split()
N=int(str_[0])
M=int(str_[1])

arr =[]
arr_split =[]
index = []
for i in range(N+M):
    arr.append(input())
for i in arr:
    arr_split.append(i.split()[0])
for i in range(N):
    if arr[N:N+M:1] in arr_split:
        index.append(arr[i])
print(index)
