def getLeftChildPosition(i):
    return i*2 +1 #+1 since array starts from 0 in python

def getRightChildPosition(i):
    return (i*2)+1 +1 #+1 since array starts from 0 in python

#Function to swap two numbers in an array
def swap(array,i,largestPos):
    temp = array[i]
    array[i] = array[largestPos]
    array[largestPos] = temp

def max_heapify(array,i):
    heap_size = len(array)
    
    #getting left child and right child of ith position from the array.
    leftChildPos = getLeftChildPosition(i)
    rightChildPos = getRightChildPosition(i)
    
    if(leftChildPos < heap_size and array[leftChildPos] > array[i]):
        largestPos = leftChildPos
    else:
        largestPos = i
    if(rightChildPos < heap_size and array[rightChildPos] > array[largestPos]):
        largestPos = rightChildPos
    
    if(largestPos != i):
        swap(array,i,largestPos)
        max_heapify(array, largestPos)

def build_max_heap(array):
    n = len(array)-1
    for i in range(n//2,-1,-1):
        max_heapify(array,i)
    

#array = [16,14,10,8,7,9,3,2,4,1]
array = [7,10, 20, 3, 4, 49, 50]
build_max_heap(array)
print(array)