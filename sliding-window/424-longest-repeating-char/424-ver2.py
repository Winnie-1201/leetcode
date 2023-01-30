class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charSet = {}
        maxLen = 0
        left = 0
        largeCount = 0
        for right in range(len(s)):
            
            # create the dictionary to store the char and its count
            if s[right] not in charSet: charSet[s[right]] = 1
            else: charSet[s[right]] += 1

            # other way for the above:
            # charSet[s[right]] = 1 + charSet.get(s[right], 0)
            
            # store the largest count so far
            largeCount = max(largeCount, charSet[s[right]])
            
            # if the current length of the str - largest count > k
            # which means the difference str count is greater then
            # the times that we can flip the char
            # then we need to remove the left most char from the set
            if right + 1 - left - largeCount > k:
                charSet[s[left]] -= 1
                left += 1
            
            maxLen = max(right - left + 1, maxLen)
        return maxLen
                
                
            
            