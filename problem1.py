class Solution:
    def twosum(self,nums:list[int], target:int):
        seen = {}
        
        for i in range(len(nums)):
            diff = target - nums[i]

            if diff in seen:
                return(i, seen[diff])
            else:
                seen[nums[i]] = i



    

arr = [2,4,5,7,9,11,15]

print(Solution().twosum(arr,7))
