import statistics
import sys
input = sys.stdin.readline

n = int(input())

array = []

for i in range(n):
    array.append(int(input()))

print(round(statistics.mean(array)))
print(statistics.median(array))

li = statistics.multimode(array)
li.sort()
result = li[1] if len(li) > 1 else li[0]
print(result)

print(max(array) - min(array))

########################################################################
# 개수 체크할 때 Counter 라이브러리 사용
import sys
from collections import Counter
n = int(sys.stdin.readline())
nums = []

for i in range(n):
    nums.append(int(sys.stdin.readline()))

nums.sort()
nums_s = Counter(nums).most_common()

print(round(sum(nums) / n))
print(nums[n // 2])

if len(nums_s) > 1:
    if nums_s[0][1] == nums_s[1][1]:
        print(nums_s[1][0])
    
    else:
        print(nums_s[0][0])

else:
    print(nums_s[0][0])

print(nums[-1] - nums[0])