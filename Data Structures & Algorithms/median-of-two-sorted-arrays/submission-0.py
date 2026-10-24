class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
            
        A, B = nums1, nums2
        total_len = len(A) + len(B)
        half_len = total_len // 2
        
        low, high = 0, len(A)
        
        while low <= high:
            i = (low + high) // 2
            j = half_len - i

            A_left = A[i - 1] if i > 0 else float('-inf')
            A_right = A[i] if i < len(A) else float('inf')
            
            B_left = B[j - 1] if j > 0 else float('-inf')
            B_right = B[j] if j < len(B) else float('inf')
            
            if A_left <= B_right and B_left <= A_right:
                if total_len % 2 != 0:
                    return float(min(A_right, B_right))

                return (max(A_left, B_left) + min(A_right, B_right)) / 2.0
                
            elif A_left > B_right:
                high = i - 1
            else:
                low = i + 1
                
        return 0.0
