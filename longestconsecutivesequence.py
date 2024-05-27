nums = [0,3,7,2,5,8,4,6,0,1]
set_of_nums = set(nums)
for i in nums:
    if i-1 not in set_of_nums:
        length = 0
        while i+length in set_of_nums:
            length += 1
print(length)