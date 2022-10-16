from typing import List
class Solution():
    def __init__(self) -> None:
        pass
    def longest_Consecutive(nums: List[int]) -> int:
        number_set = set(nums)
        sequence_size = 0

        for n in nums:
            start_of_sequence = n - 1

            if start_of_sequence not in number_set: 
                length = 1 
                next_value = n + 1 #traverse to the right of value
                while next_value in number_set:
                    next_value+=1
                    length+=1
                sequence_size = max(length, sequence_size)
        return sequence_size

solution = Solution.longest_Consecutive([100,4,200,1,3,2])
