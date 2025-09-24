# Basic
for i in range (0,151) :
    print(i)

# Multiples of Five
for j in range (5,1001,5) :
    print(j)

# Counting, the Dojo Way
for k in range (1,101):
    if k % 10 == 0 :
        print("Dojo")
    elif k %5 == 0 : 
        print ("Coding")
    else :
        print(k)

# Whoa. That Sucker's Huge
sum = 0
for x in range (0,500001) :
    if x % 2 ==1 :
        sum = sum+x
print(sum)

# Countdown by Fours
for y in range (2018,0,-4) :
    print(y)

# Flexible Counter
lowNum = 2
heighNum =9
mult=3
for z in range (lowNum,heighNum+1):
    if z % mult ==0:
        print(z)


