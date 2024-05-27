nums = list(map(int, input().split()))
target = int(input())
left = 0
right = len(nums) - 1
while left < right:
    mid = (left + right)//2
    if target > nums[mid]:
        left = mid
    elif target < nums[mid]:
        right = mid
    else:
        print(mid)
        break