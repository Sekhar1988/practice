# Problem: https://leetcode.com/problems/merge-sorted-array/

class Solution:
        def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
            """
            Do not return anything, modify nums1 in-place instead.
            """

            if (m + n) < len(nums1):
                raise ValueError("Invalid inputs")

            p1 = 0
            p2 = 0
            mod_m = m - 1
            while p1 < (m + n) and p2 < n:
                print(f"p1: {p1}, p2: {p2}, mod_m: {mod_m}")

                if p1 <= mod_m and nums1[p1] < nums2[p2]:
                    p1 = p1 + 1 # 1
                elif p1 <= mod_m  and nums1[p1] == nums2[p2]:
                    nums1.pop()
                    nums1.insert(p1, nums2[p2])
                    mod_m = mod_m + 1
                    p1 = p1 + 2
                    p2 = p2 + 1
                elif p1 <= mod_m and nums1[p1] > nums2[p2]:
                    nums1.pop()
                    nums1.insert(p1, nums2[p2])
                    mod_m = mod_m + 1
                    p1 = p1 + 1
                    p2 = p2 + 1
                elif p1 > mod_m and nums1[p1] == 0:
                    nums1[p1] = nums2[p2]
                    p1 = p1 + 1
                    p2 = p2 + 1
    
                print(f"num1={nums1}")

