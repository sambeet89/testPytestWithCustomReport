


given  = "cassssdddaaaaaasdadaaadsdas"


count = 0
final_longest=""

while count < len(given):
    temp_longest=given[count]
    for i in range(count+1, len(given), 1):
        if given[count]==given[i]:
            temp_longest=temp_longest+given[i]
        else:
            count=i
            if len(final_longest)< len(temp_longest):
                final_longest = temp_longest
            temp_longest=""
    count = count + 1



print(final_longest)

