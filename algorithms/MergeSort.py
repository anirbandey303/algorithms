#Merge Sort

#takes an array and returns 2 array by dividing it from middle
def splitArray(array):
    mid = len(array) // 2
    left = array[:mid]
    right = array[mid:]
    return left, right

def mergeTwoArrays(left, right, array):
    i = j = k = 0
    
    while( i < len(left) and j < len(right) ):
        if( left[i] < right[j] ):
            array[k] = left[i]
            i = i + 1
            k = k + 1
        else:
            array[k] = right[j]
            j = j + 1
            k = k + 1
    while( i < len(left) ):
        array[k] = left[i]
        i = i + 1
        k = k + 1
    while( j < len(right) ):
        array[k] = right[j]
        j = j + 1
        k = k + 1
    return array

def mergeSort(array):
    if(len(array) > 1):
        
        #split
        left, right = splitArray(array)
        
        #recursively call for left and right
        mergeSort(left)
        mergeSort(right)
        
        #merge the two list
        array = mergeTwoArrays(left, right, array)

if __name__ == '__main__':
    #array = [20, 1 , 50, 40, 2]
    array = [60, 11 , 250, 340, 21, 9, 27, 900, 64, 99]
    mergeSort(array)
    print(array)