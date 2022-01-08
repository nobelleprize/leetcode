# https://leetcode.com/problems/median-of-two-sorted-arrays/

def findMedianSortedArrays(nums1, nums2):
    while nums1 and nums2:
        left_1 = nums1[0]
        left_2 = nums2[0]
        
        right_1 = nums1[-1]
        right_2 = nums2[-1]

        if left_1 <= left_2 and len(nums1) > 0:
            left = nums1.pop(0)
        elif len(nums2) > 0:
            left = nums2.pop(0)
        
        if right_1 >= right_2 and len(nums1) > 0:
            right = nums1.pop()
        elif len(nums2) > 0:
            right = nums2.pop()

    if len(nums1) > 0:
        mid = len(nums1) // 2
        if len(nums1) % 2 == 1: # odd
            return nums1[mid]
        else:
            return (nums1[mid] + nums1[mid-1]) / 2
    elif len(nums2) > 0:
        mid = len(nums2) // 2
        if len(nums2) % 2 == 1: # odd
            return nums2[mid]
        else:
            return (nums2[mid] + nums2[mid-1]) / 2

    return (left + right) / 2


# print(findMedianSortedArrays([1,3], [2]))
print(findMedianSortedArrays([1, 2, 3, 4, 5, 6, 7, 8, 9], [2]))
