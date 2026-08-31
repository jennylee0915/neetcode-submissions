class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0

        for i in num_set:
            if (i-1) not in num_set:
                current = i
                current_length = 1

                while (current+1) in num_set:
                    current = current +1
                    current_length += 1
                if current_length > longest:
                    longest = current_length

        return longest
