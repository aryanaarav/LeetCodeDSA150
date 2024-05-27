nums = [2,2,1,2,2]
numsset = set(nums)
for i in numsset:
    count = 0
    while i in nums:
        count += 1
        if count > len(nums)//2:
            print(i)
            break
        else:
            continue
print(len(nums))