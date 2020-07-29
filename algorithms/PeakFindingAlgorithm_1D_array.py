#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Bitonic Peak - Peak Finder Algorithm - Recursive Binary Search
import math
def peak(arr,start,end):
    if(end==0):
        return arr[0]
    if(arr[0]>=arr[1]):
        return arr[0]
    if(arr[end]>=arr[end-1]):
        return arr[end]
    
    mid = math.floor((end+start)/2)
    if(arr[mid-1]>arr[mid]):
        return(peak(arr,start,mid-1))
    elif(arr[mid+1]>arr[mid]):
        return(peak(arr,mid+1,end))
    else:
        return arr[mid]  
    
    
#arr=[1,2,3,4,5,3]    
#arr=[1,2,3,4,5,4,3,2,1]
#arr=[4,5,9,6]
arr=[1,2,3,4,5,19,25,20]
#arr=[100,4,3,1,19,20]
#arr=[100,300,600,900]
val = peak(arr, 0, len(arr)-1 )
print(val)

