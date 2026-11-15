# problem 1 
age = 27
weight = 95.04 
name = "Virender"
isAdult = True

# print(age, type(age))
# print(weight, type(weight))
# print(name, type(name))
# print(isAdult, type(isAdult))

# problem 2 
a = '10'
b = '20'

a = int(a)
b = int(b)

result = a + b
# print(result)

# problem 3 
numbers = [10,25,5,40,15]

largest = numbers[0]
for i in range(len(numbers)):
    if numbers[i] > largest:
        largest = numbers[i]

# print(largest)

# problem 4 
sum = 0

for i in range(len(numbers)):
    sum += numbers[i]

# print(sum)

# problem 5

even = 0
odd = 0
for i in range(len(numbers)):
    if numbers[i]%2 == 0:
        even = even + 1
    else:
        odd = odd + 1

# print(even)
# print(odd) 

# problem 6
reversed_list = []

for i in range(len(numbers) -1, -1, -1):
    reversed_list.append(numbers[i])
# print(reversed_list)

# problem 7
new= [1,2,2,3,4,4,5] 
# print(new)
unique = []

for i in range(len(new)):
    if new[i] not in unique:
        unique.append(new[i])
# print(unique)

# problem 8
data = (10,20,30,40,50)

# print("first", data[0])
# print("last", data[-1])

a,b,c,d,e = data

# print(a)
# print(b)
# print(c)
# print(d)
# print(e)

# problem 9
occur = (1,2,3,2,4,2,5)
count = 0
for i in range(len(occur)):
    if occur[i] == 2:
        count += 1
# print(count)

# problem 10
list1 = [1,2,3,4,5]
list2 = [3,4,5,6,7]

common = []

for i in range(len(list1)):
    if list1[i] in list2:
        if list1[i] not in common:
            common.append(list1[i])


# print(common)