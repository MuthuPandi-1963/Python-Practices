def missingPositiveNumber(arr,k):
    maximum=max(arr)
    length=len(arr)
    if length==maximum:
        return maximum+k
    else:
        if length<maximum:
            val=maximum-length
            if val<k:
                return maximum+(k-val)
            else:
                array=[]
                for i in range(1,maximum+1):
                    if i not in arr:
                        array.append(i)
                return array[k-1]

    

print(missingPositiveNumber([2,3,4,7,11],5))
print(missingPositiveNumber([1,2,3,4],2))
print(missingPositiveNumber([5,6,7,8,9],9))
print(missingPositiveNumber([1,13,18],17))
        

