# Biggie Size
def biggie_size(a):
    for i in range (len(a)):
        if a[i]>0 :
            a[i]="big"
    return a
print(biggie_size([-1, 3, 5, -5]))

# Count Positives 
def count_positive(list):
    count =0
    for i in range(len(list)):
        if list[i] > 0 :
            count += 1
    list[len(list)-1] = count
    return list
print(count_positive([1,6,-4,-2,-7,-2]))

# Sum Total 
def sum_total(list):
    sum = 0
    for i in range(len(list)):
        sum += list[i]
    return sum
print(sum_total([6,3,-2]))

# Average
def average(list):
    sum = 0
    avg = 0
    for i in range(len(list)):
        sum += list[i]
    avg = sum/len(list)
    return avg
print(average([1,2,3,4]) )

# Length
def length(list):
    return len(list)
print( length([37,2,1,-9]))

# Minimum
def minimum(list):    
    if len(list) == 0 :
            return False
    min = list[0]
    for i in range(len(list)):
        if list[i]< min :
            min = list[i]
    return min
print(minimum([37,2,1,-9]))

# Maximum
def maximum(list):
    if len(list) == 0:
        return False
    
    max = list[0]
    for i in range (len(list)):
        if list[i] >max :
            max = list[i]
    return max
print(maximum([37,2,1,-9]))

# Ultimate Analysis
def ultimate_analysis(list):
    dictionary = {"sumTotal":sum_total(list), "average":average(list), "minimum":minimum(list), "maximum":maximum(list), "length":length(list)}
    return dictionary
print(ultimate_analysis([37,2,1,-9]))

# Reverse List 
def reverse_list(list):
    for i in range(len(list)-1,-1,-1):
        list.append(list[i])
        list.pop(i)
    return list
print(reverse_list([37,2,1,-9]))     



