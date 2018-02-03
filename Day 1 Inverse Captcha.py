def joinstr (arr):
    string = arr # String
    newstring = [] # Array of new string
    #print (s)
    for i in string: 
        newstring.append(int(i)) # add to array i-1
    #print (a)
    return newstring


def summident(arr):
    sum=0
    for i in range(len(arr)):
        if arr[i-1] == arr[i]:
            sum=sum+arr[i]
              
    print(arr)
    return sum

arr=joinstr("91212129")
res=summident(arr)
print(res)
