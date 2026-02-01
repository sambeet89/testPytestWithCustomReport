

candidates = [2,3,6,7]
target = 27
focus=list()
found= False

for i in range(0,len(candidates),1):
    sum= candidates[i]
    focus.append(sum)
    while sum<= target:
        sum= sum*candidates[i]
        focus.append(candidates[i])
        if sum == target:
            found=True
            break
if found:
    print("found")
    print(focus)
else:
    print("not found")








