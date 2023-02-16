from ast import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2

        if len(A) > len(B):
            A, B = B, A

        # get the total len and the half
        total = len(A) + len(B)
        half = total // 2

        # do the binary search on A
        l, r = 0, len(A) - 1
        while True:
            mid = (l + r) // 2
            # since mid is index, then needs to minus 1
            # and since index starts with 0, then needs to minus 1 again
            # for rest to be an index
            rest = half - mid - 2

            Aleft = A[mid] if mid >= 0 else float("-inf")
            Aright = A[mid + 1] if mid + 1 < len(A) else float("inf")
            Bleft = B[rest] if rest >= 0 else float("-inf")
            Bright = B[rest + 1] if rest + 1 < len(B) else float("inf")

            if Aleft <= Bright and Bleft <= Aright:
                # when is odd:
                if total % 2:
                    return min(Aright, Bright)
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                r = mid - 1
            else:
                l = mid + 1
