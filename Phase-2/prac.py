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
 