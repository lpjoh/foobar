def recurse_list(nums, l):
    max_nums = nums
    
    for i in range(len(l)):
        next_nums = nums * 10 + l[i]
        
        next_l = l[:]
        del next_l[i]
        
        next_max_nums = recurse_list(next_nums, next_l)
        
        if next_max_nums <= max_nums:
            continue
        
        if next_max_nums % 3 != 0:
            continue
        
        max_nums = next_max_nums
        
    return max_nums

def solution(l):
    return recurse_list(0, l)