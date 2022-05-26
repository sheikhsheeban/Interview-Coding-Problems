

# Iterative Approach

def binary_Search(arr,target):
    start = 0
    end = len(arr)-1
    while start<=end:
        mid=(start+end)//2
        if target>arr[mid]:
            start=mid+1
        if target<arr[mid]:
            end=mid-1
        if target==arr[mid]:
            result=mid
            end=mid-1
    return result


arr=[ 1, 2, 2, 2, 2, 3, 4, 7, 8, 8 ]
target=8
result = binary_Search(arr,target)
if result!=None:
    print("Element is present at index ",str(result))
else:print("Element is not present in array")

def binary_Search(arr,target):
    start = 0
    end = len(arr)-1
    while start<=end:
        mid=(start+end)//2
        if target>arr[mid]:
            start=mid+1
        if target<arr[mid]:
            end=mid-1
        if target==arr[mid]:
            result=mid
            start=start+1
    return result


arr=[ 1, 2, 2, 2, 2, 3, 4, 7, 8, 8 ]
target=8
result = binary_Search(arr,target)
if result!=None:
    print("Element is present at index ",str(result))
else:print("Element is not present in array")
