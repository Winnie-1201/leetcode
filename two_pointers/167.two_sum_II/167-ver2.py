from ast import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # define two pointers
        start, end = 0, len(numbers) - 1
        # start comparing the sum of num in index start and end
        while start < end:
            if numbers[start] + numbers[end] == target:
                return [start+1, end+1]
            elif numbers[start] + numbers[end] < target:
                start += 1
            else:
                end -= 1
