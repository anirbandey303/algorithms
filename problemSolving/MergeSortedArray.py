######MY Approach (BAD) ########################

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        totalSize = m+n
        n1 = 0
        n2 = 0
        k=0
        while(n1<m and n2<n):
            if(nums1[n1] < nums2[n2]):
                #nums1.insert(k,nums1[n1]) 
                k+=1
                n1+=1
            else: #(nums1[n1] >= nums2[n2])
                nums1.insert(k,nums2[n2])
                k+=1
                n2+=1
                n1+=1
                m+=1
            print(nums1,n1,n2)
        while(n1 < m):
            k+=1
            n1+=1
        while(n2 < n):
            nums1.insert(k,nums2[n2])
            k+=1
            n2+=1
        for i in range(len(nums1) - totalSize):
            nums1.pop()