# ransomNote – the word you want to create.
# magazine – the letters available to create that word.

magazine = "aab"
count = {}

for char in magazine:
    if char in count:
        count[char] += 1
    else:
        count[char] = 1
print(count)

ransomNote = "aa"
for char in ransomNote:
    if char in count:
        print("Yes found")
    else:
        print("No not here")


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count = {}

        for char in magazine:
            if char in count: 
                count[char] += 1
            else:
                count[char] = 1

        for char in ransomNote:
            if char in count:
                count[char] -= 1

                if count[char] < 0:
                    return False 
            else:
                return False
        return True

arr = [1,3,4,5]
k = 2
found = False
for i in range(len(arr)):
  # print("1", arr[i])
  for j in range(i, len(arr)):
    if k == arr[i] + arr[j]:
      print(arr[i], arr[j])
      found = True
if not found:
    print("no logic")
 