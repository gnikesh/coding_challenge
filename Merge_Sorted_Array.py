# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array. Note: You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2. The number of elements initialized in nums1 and nums2 are m and n respectively.


def merge(nums1, m, nums2, n):
    # Initialize pointers for nums1 and nums2
    p1 = m - 1
    p2 = n - 1
    
    # Initialize a pointer for the end of nums1
    end = m + n - 1
    
    # Merge nums2 into nums1
    while p2 >= 0:
        # Compare the elements at p1 and p2
        if p1 >= 0 and nums1[p1] > nums2[p2]:
            # Move the larger element to the end of nums1
            nums1[end] = nums1[p1]
            p1 -= 1
        else:
            # Move the larger element to the end of nums1
            nums1[end] = nums2[p2]
            p2 -= 1
        end -= 1

# Time complexity: O(m+n) 
# Space complexity: O(1)
