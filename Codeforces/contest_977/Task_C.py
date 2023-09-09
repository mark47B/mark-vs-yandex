# Not full

def solution():
    N, k = input().split(' ')
    k = int(k)
    N = int(N)

    nums = list(map(int, input().split(' ')))
    if k == 0:
        return min(nums) - 1
    if N == k:
        return max(nums)

    nums.sort()

    if  nums[k-1] == nums[k]:
        return -1
    
    return nums[k-1]
    

print(solution())

# 4
# 1 3 3 5 7 10 20
# 5 or 6 -- valid

# 7 4
# 1 3 3 5 6 7 10 20
# -1 ? 6

# 4
# 1 3 3 5 9 10 20
# 6 ? 8

# 7 2
# 1 3 3 5 7 10 20
