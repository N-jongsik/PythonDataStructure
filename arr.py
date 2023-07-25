str = "t0e0a1c2h0er"
arr = []
for i in str:
    if i.isdigit():
        arr.append(int(i))

if arr and arr[0] == 0:
    arr = arr[1:]
for i in range(len(arr)):
    if arr[i] == 0:
        arr.pop(i)
    else:
        break
arr= str(arr)
answer = "".join(arr)
    
print(answer)



