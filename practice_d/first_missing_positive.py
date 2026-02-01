num = [1, 2, 4, 6]
sum=sum(num)
max=max(num)
min=min(num)




result=0
expectedSum=0
for x in range(min,max+1,1):
    expectedSum=expectedSum+x

if expectedSum==sum:
    if min>1:
        result=1
    else:
        result=max+1
else:
    result= expectedSum-sum

print(result)











