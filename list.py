

















class Solution():
    def threeSum(self, nums):
        res = []
        nums.sort()
        length = len(nums)
        for i in range(length-2): #already checked last 2 elements
            if nums[i]>0: break #will be greater than 0
            if i>0 and nums[i]==nums[i-1]: continue #do not repeat for same element

            l, r = i+1, length-1 
            while l<r:
                total = nums[i]+nums[l]+nums[r]

                if total<0: 
                    l+=1
                elif total>0: 
                    r-=1
                else: #[5]
                    res.append([nums[i], nums[l], nums[r]])
                    while l<r and nums[l]==nums[l+1]: 
                        l+=1
                    while l<r and nums[r]==nums[r-1]: 
                        r-=1
                    l+=1
                    r-=1
        return res
p1 = Solution()
nums = [-1, 0, 1, 2, -1, -4]
print(p1.threeSum(nums))
//[[-1, -1, 2], [-1, 0, 1]]
