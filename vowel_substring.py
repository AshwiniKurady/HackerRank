# Given a string and substring length, we need to find the substring which has maximum number of vowels in it.
# If there are more than one substring, then select the one that starts with the lower index.
# 
# import sys

def findSubstring(s, k):
    vowels = ["a","e","i","o","u"]
    vowel_count= {}
    for i in range(len(s)):
        if i+k<=len(s):
            for char in s[i:i+k]:
                if char in vowels:
                    if i in vowel_count:
                        vowel_count[i]+=1
                    else:
                        vowel_count[i]=1
    for key,val in vowel_count.items():
        if val == max(vowel_count.values()):
            i=key
            return s[i:i+k]
    return "Not found!"

if __name__ == '__main__':
    print("Enter the string")
    s = input()
    print("Enter the substring length")
    k = int(input().strip())
    result = findSubstring(s, k)
    print(result)