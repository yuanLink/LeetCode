"""
use i and j like two bank:
we put two array into on set, and use i and j to seperate them
left_group    | right_group
a[0]...a[i-1] | a[i],a[i+1]..a[m]
b[0]...b[i-1] | b[j],b[j+1]..b[n]

in this case ,we can find:
a[i-1] < b[j]
b[j-1] < a[i]

and because [median],so has this regular
i + j = m - i + n - j (+ 1 )
so if we know i, j = (m + n + 1)/2  - i(we write in this format so we do not to need 
know m + n is odd or not, and in this condition, n > m)

"""


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m,n = len(nums1),len(nums2)
        if m > n:
            m,n = n,m
            nums1, nums2 = nums2, nums1
        imin,imax = 0,m
        while imin <=  imax:
            # use i as left_group and j as right group
            i = (imax + imin) // 2
            j = (m + n + 1) //2 - i
            # this condition, i is small ,so we should add i
            if i < m and nums1[i] < nums2[j - 1]:
                imin = i + 1
            # this condition, i is big, so we should decrease i
            elif i > 0 and nums1[i - 1] > nums2[j]:
                imax = i - 1
            else:
                # this condition, i is right
                # we just find min and max
                # if i == 0, it means that max_left is b[j-1]
                if i == 0: 
                    max_left = nums2[j - 1]
                elif j == 0:
                    max_left = nums1[i - 1]
                else:
                    # print "i = %d, j = %d"%(i,j)
                    max_left = max(nums1[i - 1], nums2[j - 1])

                if (m + n) % 2 == 1:
                    return max_left
                    
                if i == m:
                    min_right = nums2[j]
                elif j == n:
                    min_right = nums1[i]
                else:
                    min_right = min(nums2[j], nums1[i])
                return (max_left + min_right)/2.0