# Full
def make_seq(cur: int, cur_nums: set):
    if len(cur_nums) == 0:
        return []
    nums_1 = cur_nums.copy()
    if cur * 2 in nums_1:
        nums_1.remove(cur * 2)
        res1 = make_seq(cur*2, cur_nums=nums_1)
        if res1 is not None:
            return [cur*2] + res1

    nums_2 = cur_nums.copy()
    if cur % 3 == 0 and cur // 3 in nums_2:
        nums_2.remove(cur // 3)
        res2 = make_seq(cur // 3, cur_nums=nums_2)
        if res2 is not None:
            return [cur // 3] + res2
    return None
    



def solution():
    N = input()
    N = int(N)

    if N == 0:
        return None
    
    nums = set(map(int, input().split(' ')))

    for i in nums:
        res =  make_seq(i, nums - {i})
        if res is not None:
            return [i] + res
    

    

print(' '.join(str(item) for item in solution()))