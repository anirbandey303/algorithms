#Insertion sort takes O(n) for Comparing and Swapping FOR EACH key
#Here I used a Binary Search for Comparison
#Thus requireing a complexity of only O(log n) FOR EACH key
#However for Swapping our time complexity remains O(n) as we use List Data Structure
#Thus the overall time complexity of Binary Insertion Sort is O(n2)

import math

def binarySearch(array, start, end, key):
    #returns the position where key needs to be inserted
    mid = math.floor( (start+end) / 2 )
    if(mid>start and key<array[mid]):
        if(mid<end and key>array[mid-1]):
            return mid
        else:
            #print("Moving left")
            return binarySearch(array,start,mid-1,key)
    elif(mid<end and key>array[mid]):
        if(mid>start and key<array[mid+1]):
            return mid
        else:
            #print("Moving right")
            return binarySearch(array, mid+1, end, key)
    else:
        return mid
    
def binaryInsertionSort(arr):
    key =0
    position = 0
    for i in range(1,len(arr)):
        key = arr[i]
        position = binarySearch(arr[0:i], 0, i, key)
        arr.insert(position,key)
        arr.pop(i+1)
        print("Swapping List : ",arr, " Key : ", key)
    return arr

arr = [5,2,4,6,1,3]
print("INITIAL Array *** : ", arr)
print("FINAL Array *** : ", binaryInsertionSort(arr))