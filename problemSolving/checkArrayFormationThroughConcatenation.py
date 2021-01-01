class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        positions = dict()
        for i in range(len(arr)):
            positions[arr[i]] = i
        for piece in pieces:
            for i in range(len(piece)):
                if(piece[i] not in positions.keys()):
                    return False
                if(i>0 and positions[piece[i]] - positions[piece[i-1]] != 1):
                    return False
        return True