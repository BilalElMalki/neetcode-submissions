class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        
        for i in range(len(arr) - 1, 0, -1):
            if arr[i] > arr[i - 1]:
                arr[i-1] = arr[i]

        for j in range(len(arr)):
            if j == len(arr) - 1:
                arr[j] = -1
            else:
                arr[j] = arr[j + 1]

        return arr        