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
            return mid

arr=[2,3,4,5,10,40]
target=2
result = binary_Search(arr,target)
if result!=None:
    print("Element is present at index ",str(result))
else:print("Element is not present in array")




# Recursive Approach

def binary_Search(arr,target,start,end):

    if start<=end:
        mid=(start+end)//2
        if target>arr[mid]:
            return binary_Search(arr,target,mid+1,end)
        if target< arr[mid]:
            return binary_Search(arr,target,start,mid-1)
        if target==arr[mid]:
            return mid




arr=[2,3,4,5,10,40]
target=400
start=0
end=len(arr)-1
result = binary_Search(arr,target,start,end)
if result!=None:
    print("Element is present at index ",str(result))
else:print("Element is not present in array")