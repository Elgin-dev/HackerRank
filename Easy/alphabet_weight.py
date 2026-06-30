#!/bin/python3

import os

def weightedUniformStrings(s, queries):
    # Store all possible uniform substring weights
    weights = set()

    current_weight = 0
    previous = ''

    for ch in s:
        value = ord(ch) - ord('a') + 1

        if ch == previous:
            current_weight += value
        else:
            current_weight = value

        weights.add(current_weight)
        previous = ch

    ans = []

    for q in queries:
        if q in weights:
            ans.append("Yes")
        else:
            ans.append("No")

    return ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries.append(int(input().strip()))

    result = weightedUniformStrings(s, queries)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()