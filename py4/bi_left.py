def bi_left(nums, target, lo=0, hi=None):
    if lo < 0: 
        return -1

    if hi == None: 
        hi = len(nums) 
    
    while lo < hi: 
        mid = (lo + hi) // 2
        if nums[mid] < target: 
            lo = mid + 1
        else: 
            hi = mid 

    return lo 

def bi_right(nums, target, lo=0, hi=None): 
    if lo < 0: 
        return -1

    if hi == None: 
        hi = len(nums) 
    
    while lo < hi: 
        mid = (lo + hi) // 2
        if nums[mid] > target: 
            #hi = mid - 1 #wrong, [7] 
            hi = mid 
        else: 
            lo = mid + 1

    return lo 

input = [ 3, 4, 7, 7, 7, 8, 10, 11]

result = bi_left(input, 7, 0) 
print("the result is ", result)

result = bi_left(input, 5, 0) 
print("the result is ", result)

result = bi_right(input, 7, 0) 
print("the result is ", result)

input = [6, 7] 
result = bi_right(input, 7, 0) 
print("the result is ", result)

input = [5,7,7,8,8,10]
result = bi_right(input, 8, 0) 
print("the result is ", result)
