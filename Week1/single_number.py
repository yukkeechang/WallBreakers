class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        sortedNums = nums.sort()
        i = 0
        p1 = 1 #pointer
        while p1 < len(nums)+1 :
           if i == len(nums)-1 :
            return(nums[i])
           if nums[p1] == nums[i] :
            print("nums[p1] == nums[p2]: ", p1, i)
            i = i+2
            p1 = i+1
            print("after increment: ", p1, i)
           else:
            print(nums[p1], nums[i])
            return nums[i]
