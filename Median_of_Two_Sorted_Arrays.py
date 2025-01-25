# There are two sorted arrays nums1 and nums2 of size m and n respectively. Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)). Example 1: nums1 = [1, 3] nums2 = [2] The median is 2.0 Example 2: nums1 = [1, 2] nums2 = [3, 4] The median is (2 + 3)/2 = 2.5


def findMedianSortedArrays(nums1, nums2):
    # Merge two sorted arrays
    merged = []
    i = j = 0
    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            merged.append(nums1[i])
            i += 1
        else:
            merged.append(nums2[j])
            j += 1
    merged += nums1[i:]
    merged += nums2[j:]

    # Find the median
    n = len(merged)
    if n % 2 == 1:
        return merged[n // 2]
    else:
        return (merged[n // 2 - 1] + merged[n // 2]) / 2

# However, this approach has a time complexity of O(m+n) which is not acceptable. 
# The problem requires a time complexity of O(log(m+n))

# Binary Search approach
def findMedianSortedArrays2(nums1, nums2):
    if len(nums1) > len(nums2):
        return findMedianSortedArrays2(nums2, nums1)

    x, y = len(nums1), len(nums2)
    start = 0
    end = x

    while start <= end:
        partitionX = (start + end) // 2
        partitionY = ((x + y + 1) // 2) - partitionX

        maxLeftX = float('-inf') if partitionX == 0 else nums1[partitionX - 1]
        minRightX = float('inf') if partitionX == x else nums1[partitionX]

        maxLeftY = float('-inf') if partitionY == 0 else nums2[partitionY - 1]
        minRightY = float('inf') if partitionY == y else nums2[partitionY]

        if maxLeftX <= minRightY and maxLeftY <= minRightX:
            if (x + y) % 2 == 0:
                return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2
            else:
                return max(maxLeftX, maxLeftY)
        elif maxLeftX > minRightY:
            end = partitionX - 1
        else:
            start = partitionX + 1

# Time complexity: O(log(min(m, n)))
# Space complexity: O(1)
