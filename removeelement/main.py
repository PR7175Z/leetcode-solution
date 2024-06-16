# class Solution(object):
#     def removeElement(self, nums, val):
#         for x in range(0, len(nums)):
#             if nums[x] == val:
#                 nums.pop(x)

#         k = len(nums)
#         return k
    
# c = Solution()
# print(c.removeElement([1,1,2,1,2,3,4,5,5], 1))


x=0
nums = [1,1,2,1,2,3,4,5,5]
val = 1
running = True
for x in nums:
    if x == val:
        nums.remove(x)
    print(val)
    
print(nums)
