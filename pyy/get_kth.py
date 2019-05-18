

class Solution(object):
    
    def getKth(self, A, B, k):
        lenA = len(A)
        lenB = len(B)
        
        if lenA > lenB: 
            return self.getKth(B, A, k)
        
        if lenA == 0: 
            return B[k - 1]
        
        if k == 1: 
            return min(A[0], B[0])
        
        pa = min(k/2, lenA); 
        pb = k - pa
        
        if A[pa - 1] <= B[pb - 1]:
            return self.getKth(A[pa:], B, pb)
        else:
            return self.getKth(A, B[pb:], pa)
        
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        
        lenA = len(nums1)
        lenB = len(nums2)
        return (self.getKth(nums1, nums2, (lenA + lenB + 1)/2) + self.getKth(nums1, nums2, (lenA + lenB + 2)/2 )) * 0.5
        

