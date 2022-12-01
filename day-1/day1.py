listNum = []
sumNumber = 0
with open("day1.in",'r') as readfile:
    for line in readfile:
        if line.strip():
            sumNumber += int(line)
            listNum.append(sumNumber)
        else:
            listNum.append(sumNumber)
            sumNumber = 0

print("the highest number is " + str(max(listNum)))

#part 2
#sort from largest to smallest
listNum.sort(reverse=True)
top3sum = listNum[0] + listNum[2] + listNum[4]
print("the sum of the three highest calories is " + str(top3sum))

f = sorted(eval(open(0).read().
    replace('\n\n', ',').replace('\n', '+')))

print(f[-1], sum(f[-3:]))