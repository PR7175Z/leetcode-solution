class Solution(object):
    def merge(self, nums1, m, nums2, n):
        while len(nums1)>m:
            nums1.pop()

        for x in nums2:
            nums1.append(x)

        nums1.sort()

c = Solution()
c.merge([1,2,3,0,0,0], 3, [2,5,6], 3)