# Countdown 
def countDown(a) :
    newList = []
    for i in range (a,-1,-1):
       newList.append(i)
    return newList 
print(countDown(10))

# Print and Return
def printAndReturn(a):
    print(a[0])
    return a[1]
print(printAndReturn([5,9]))

# First Plus Length
def firstPlusLenght(a):
    sum = a[0]+ len(a)
    return sum
print(firstPlusLenght([1,2,3,4,5]))

# Values Greater than Second
def greaterThanSecond(a):
    if len(a) < 2:
        return False
    
    newList=[]
    count =0
    for i in range(0,len(a)):
        if a[i]> a[1]:
            newList.append(a[i])
            count+=1
    print(count)
    return newList
print(greaterThanSecond([5,2,3,2,1,4]))

# This Length, That Value
def length_and_value(size,value):   
    list = []
    for i in range (0,size):
        list.append(value)
    return list
print(length_and_value(6,2)) 
