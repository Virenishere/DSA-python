# largest num from list 
# num = [10,25,5,40,15]
# largest = num[0]

# for i in range(len(num)):
#     if(largest <num[i]):
#         largest = num[i]
# print(largest)

#smallest num from list
# numbers = [12, 5, 30, 2, 18]
# smallest = numbers[0]

# for i in numbers: 
#     # print(i)
#     if smallest > i:
#         smallest = i
# print(smallest)



# numbers = [1, 2, 3, 4, 5, 6, 7, 8]
# even = 0
# odd = 0

# for num in numbers:
#     if num % 2 == 0:
#         even += 1
#     else:
#         odd += 1
# print(f'even is : {even} and odd is : {odd}')


# l = ["Harry", "Soham", "Sachin", "Rahul"]

# for name in l:
#     if name.startswith("S"):
#         print(f"Hello {name}")

# i = 0
# while i<len(l):
#     if l[i].startswith("S"):
#         # print(f"hello {name}")
#         print(f"hello {l[i]}")
#     i += 1


# n = int(input("Enter the number: "))
# for i in range(1,n+1):
#     print(" " * (n-i), end="")
#     print("*" * (2*i-1), end="")
#     print("")


# reverse a list 

numbers = [1,2,3,4,5]
rev = []
for i in range(len(numbers)-1,-1,-1):
    rev.append(numbers[i])

print(rev)
