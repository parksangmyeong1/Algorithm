import sys
input = sys.stdin.readline

nums = input().rstrip()
nums = [int(n) for n in nums]

ordered_nums = sorted(nums, reverse=True)

for n in ordered_nums: 
    print(n, end = '')