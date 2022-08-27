class Solution:
    def __init__:

    def number_of_steps(self, n, steps):
        one, two = 1, 1
        for i in range(n-1):
            temp = one
            one = one + two
            two = temp
        return one
        
            