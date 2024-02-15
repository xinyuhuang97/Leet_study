class Solution:
        
    def merge(self, nums1, m, nums2, n):
        i, j = 0, 0
        if n==0:
            return
        elif n!=0:                
            if m==0:
                if n==1:
                    nums1[0]=nums2[0]
                else:
                    for index in range(0, m+n):
                        nums1[index]=nums2[index]
                        
            else:
                for index in range(m, m+n):
                    nums1[index]=nums2[n-1]+1
                    print(index)
                print(nums1,nums2)
                while i<=m+n-1:
                    while nums1[i]<nums2[j]:
                        i+=1
                    else:
                        print(i,j)
                        for index in range(m+n-1,i-1,-1):
                            nums1[index]=nums1[index-1]
                        nums1[i]=nums2[j]
                        print(nums2[j])
                        j+=1
                        if j==n:
                            return
                        print(i,j)
                    print(i,j,nums1)

