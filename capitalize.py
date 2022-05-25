#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def first_non_numeric(string):
    for count, letter in enumerate(string):
        if not letter.isnumeric():
            return letter.upper(), count + 1
def solve(s):
    first,last = s.split(" ")
    first_upper,first_splice_indice = first_non_numeric(first)
    last_upper, last_splice_indice = first_non_numeric(last)
    
        
            
    first = first_upper + first[first_splice_indice:]
    last = last_upper + last[last_splice_indice:]
    capitalized = first + " " + last
    return capitalized


print(solve("123edgar 123hernandez"))
