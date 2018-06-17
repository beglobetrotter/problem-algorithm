class solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        len1, len2 = len(nums1), len(nums2)
        if len1 > len2:
            nums1, nums2, len1, len2 = nums2, nums1, len2, len1
        imin, imax, half = 0, len1, (len1 + len2 + 1) // 2
        while imin <= imax:
            i = (imin + imax) // 2
            j = half - i
            if i < len1 and nums2[j - 1] > nums1[i]:
                imin = i + 1
            elif i > 0 and nums1[i - 1] > nums2[j]:
                imax = i - 1
            else:
                if i == 0:
                    maxLeft = nums2[j - 1]
                elif j == 0:
                    maxLeft = nums1[i - 1]
                else:
                    maxLeft = max(nums1[i -1], nums2[j -1])

                if (len1 + len2) % 2 == 1:
                    return maxLeft

                if i == len1:
                    minRight = nums2[j]
                elif j == len2:
                    minRight = nums1[i]
                else:
                    minRight = min(nums1[i], nums2[j])

                return (maxLeft + minRight) / 2.0

example = solution()
nums1 = []
nums2 = [4]
print(example.findMedianSortedArrays(nums1, nums2))