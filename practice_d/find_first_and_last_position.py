

nums = [5,6,7]
target = 7

left = 0
right = len(nums)
found=False
while left!=right:
    mid = (left+right)//2
    if nums[mid]==target:
        found=True
        break
    else:
        if target> nums[mid]:
            left= mid+1

        else:
            right=mid-1
if not found:
    print("not found")
else:
    print("found")







