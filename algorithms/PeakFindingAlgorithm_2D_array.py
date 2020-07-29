#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import math
def globalMax(arr,end):
    maxPOS = arr[0][end]
    pos = 0
    for k in range(len(arr[0])):
        if(arr[k][end]>=maxPOS):
            maxPOS = arr[k][end]
            pos=k
    return pos

def peak(arr,start,end):
    mid = math.floor( (start+end)/2 ) #binary search technique to eleminate columns
    maxPOS = globalMax(arr,mid)
    #so on column mid, arr[maxPOS][mid] is the max value
    #we got vertical max, so now we will see if it's horizaontally greater than its neighbours
    if( mid>0 and arr[maxPOS][mid-1] > arr[maxPOS][mid] ):
        #move left for a peak and eliminate all right columns 
        return(peak(arr,start,mid-1))
    elif( mid<end and arr[maxPOS][mid+1] > arr[maxPOS][mid] ):
        #move twords right for a peak and eleminate all left side columns
        return(peak(arr,mid+1,end))
    else:
        return arr[maxPOS][mid]

arr = [[1,20,60,25],[10,9,5,6],[16,11,3,1],[9,6,2,1]]
print(peak(arr,0,len(arr)-1))

