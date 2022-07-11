class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i, j =0,0
        li,lj=len(nums1),len(nums2)
        tt_l=li+lj
        l=[]
        while (i<li and j<lj):
            if nums1[i]<nums2[j] :
                l.append(nums1[i])
                i+=1
            else:
                l.append(nums2[j])
                j+=1
        l+=nums1[i:]+nums2[j:]
        if tt_l%2==0:
            print(l,tt_l,l[(tt_l//2)-1],l[(tt_l)//2 ])
            return (l[(tt_l//2)-1]+l[(tt_l)//2 ])/2
        else:
            return l[(tt_l//2)]