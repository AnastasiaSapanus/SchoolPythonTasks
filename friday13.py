fridays13th = [0] * 2011

#for i in range(2011):
 #frides13th.append(0)

day = 5
month = 1
year = 1990

while year < 2011:
 day += 7

 limit = [0,31,28,31,30,31,30,31,31,30,31,30,31]

 if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
  limit[2] += 1

 if day > limit[month]:
  day -= limit[month]
  month += 1

 if month > 12:
  year+=1
  month=1

 if day==13:
  fridays13th[year]+=1

#count = 0
#for k in fridays13th:
 #count += k

count = 0

k = int(input())

for i in range(k):
 begin,end = [int(s) for s in input().split()]
 count +=sum(fridays13th[begin : end + 1])

fridays13th.clear()

print(count)
