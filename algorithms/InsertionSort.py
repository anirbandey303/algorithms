#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def swap(a,b):
    a = a+b
    b = a-b
    a = a-b
    return(a,b)

def insertionSort(arr):
    currentPosition = 0
    key = 0
    for i in range(1,len(arr)):
        key = arr[i]
        currentPosition = i
        while(key<arr[currentPosition-1] and currentPosition>0):
            arr[currentPosition], arr[currentPosition-1] = swap(arr[currentPosition], arr[currentPosition-1])
            currentPosition = currentPosition-1
            print("Swapping Steps : ", arr, "key = ", key)
    return arr


arr = [5,2,4,6,1,3]
print("Initial Array : ", arr)
print("Final Array : ", insertionSort(arr))

