class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
            lg1=len(nums1)
            lg2=len(nums2)
            if lg1==0 or lg2==0:
                return -1
            c1=0
            c2=0
            while c1!=lg1 and c2!=lg2:
                v1=nums1[c1]
                v2=nums2[c2]
                if v1==v2:
                    return v1
                else:
                    if v1>v2:
                        c2+=1
                    else:
                        c1+=1
            return -1