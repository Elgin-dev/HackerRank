#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superReducedString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def superReducedString(s):

    res = list(s)

    i = 0
    while i < len(res)-1:

        if res[i] == res[i+1]:
            del res[i:i+2]

            if i > 0:
                i -= 1
        else:
            i += 1

    if not res:
        return "Empty String"

    return "".join(res)      

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = superReducedString(s)

    fptr.write(result + '\n')

    fptr.close()
