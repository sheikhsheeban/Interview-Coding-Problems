# Count the number of element in an sorted array

# Iterative Approach

def first_occurrence(arr,target):
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

def last_occurrence(arr,target):
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
target=2
first = first_occurrence(arr,target)
last=last_occurrence(arr,target)
print(last-first+1)

