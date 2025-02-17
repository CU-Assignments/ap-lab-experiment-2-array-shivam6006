# Find the Duplicate Number 

class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slow, fast = nums[0], nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow

solution = Solution()
print(solution.findDuplicate([1,3,4,2,2]))  
print(solution.findDuplicate([3,1,3,4,2])) 
print(solution.findDuplicate([3,3,3,3,3]))  
