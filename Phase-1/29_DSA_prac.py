# arr= [1, 2, 3, 4, 5]
# k = 3
# for i in range(0, len(arr), k):
#     arr[i:i+k] = arr[i:i+k][::-1]

# print(arr)

# class Solution:
#     def printElement(self, arr):
#         for i in range(len(arr)):
#             print(arr[i])
# arr = [10, 20, 30, 40, 50]        
# new_print = Solution()
# new_print.printElement(arr)


# class Solution:
#     def evenIndexes(self,arr):
#         for i in range(0, len(arr),2):
#             print(arr[i])

# arr = [10, 20, 30, 40, 50, 60]
# new_print = Solution()
# new_print.evenIndexes(arr)

# class Solution:
#     def reverseArr(self, arr):
#         for i in range(len(arr)-1,-1,-1):
#             print(arr[i])

# arr = [1, 2, 3, 4, 5]
# new_print = Solution()
# new_print.reverseArr(arr)

# class Solution:
#     def reveseArr(self, arr):
#         for i in range(len(arr)//2):
#             arr[i] , arr[len(arr)-1 -i] = arr[len(arr)-1-i] , arr[i]
#         print(arr)

# arr = [1, 2, 3, 4, 5]
# new_print = Solution()
# new_print.reveseArr(arr)

# class Solution:
#     def reverseInGroup(self,arr,k):
#         for i in range(0,len(arr),k):
#             arr[i:i+k] = arr[i:i+k][::-1]
#         print(arr)

# arr = [1, 2, 3, 4, 5, 6, 7, 8]
# k = 3
# new_print = Solution()
# new_print.reverseInGroup(arr,k)


# class Solution:
#     def reverseArr(self, arr):
#         for i in range(len(arr)//2):
#             arr[i],arr[len(arr)-1-i] = arr[len(arr)-1-i] , arr[i]
#         print(arr)

# arr = [1, 2, 3, 4, 5, 6, 7, 8]
# new_print = Solution()
# new_print.reverseArr(arr)


class Solution:
    def convertFive(self, n):
        # code here
        result = 0
        place = 1
        if n == 0: return 5
        while n > 0:
            last_digit = n % 10
            
            if last_digit == 0:
                last_digit = 5
                
            result = result + last_digit * place
            
            n = n // 10
            place = place * 10
            
        return result

new_print = Solution()
print(new_print.convertFive(0))