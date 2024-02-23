class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        lg=len(nums)
        new_nums=[0]*lg
        for i in range(lg):
            if i+k+1<=lg:
                new_nums[i+k]=nums[i]
            else:
                new_nums[(i+k+1)%(lg)-1]=nums[i]
        for i in range(lg):
            nums[i]=new_nums[i]
        