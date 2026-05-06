
def reverseArr(arr):
    if len(arr)<= 1:
        return arr
    left = 0
    right = len(arr)-1
    while left < right:
        arr[left],arr[right] = arr[right],arr[left]
        left+=1
        right-=1
    return arr

def isPalindrome(s):
    left =0
    right = len(s)-1
    while left < right:
        if s[left] != s[right]:
            return False
        left+=1
        right-=1
    return True

def twoSum(arr,tar):
    left = 0
    right = len(arr) -1
    total = 0
    while left< right:
        total = arr[left] + arr[right]
        if total == tar:
            return arr[left],arr[right]
        if total<tar:
            left+=1
        if total>tar:
            right-=1
    return -1,-1
        
def removeDuplicates(arr):
    slow =0
    fast =1
    while fast<len(arr):
        if arr[slow] == arr[fast]:
            fast+=1
        else:
            slow+=1
            arr[slow] = arr[fast]
            fast+=1
    return arr

def moveZeros(arr):
    slow = 0
    fast = 0
    while fast<len(arr):
        if arr[fast]!=0:
            arr[slow],arr[fast] = arr[fast], arr[slow]
            slow+=1
            fast+=1
        else:
            fast+=1
    return arr

def sqaureSortMy(arr):
    left = 0
    right = len(arr)-1
    while right>=left:
        if abs(arr[left]) > abs(arr[right]):
            arr[left],arr[right] = arr[right],arr[left]
            arr[right] = arr[right]*arr[right]
            right -=1
        else:
            arr[right] = arr[right]*arr[right]
            right -=1
    return arr

def sqaureSort(arr):
    left =0
    right = len(arr)-1
    position = len(arr)-1
    result = [0] * len(arr)
    while left<=right:
        if abs(arr[left]) > abs(arr[right]):
            result[position] = arr[left]*arr[left]
            left+=1
        else:
            result[position] = arr[right]*arr[right]
            right-=1
        position -=1
    return result


def validPalindromeTry(s):
    left =0
    right =len(s)-1
    count =0
    while left<right:
        if s[left]!=s[right]:
            if s[right] == s[right-1]:
                left+=1
            elif s[left] == s[left+1]:
                right-=1
            elif s[left]!= s[left+1]:
                if count ==0:
                    left+=1
                else:
                    return False
            elif s[right]!= s[right-1]:
                if count==0:
                    right-=1
                else:
                    return False
        else:
            left+=1
            right-=1
    return True

def validPalindrome(s):
    left =0
    right =len(s)-1
    while left<right:
        if s[left]==s[right]:
            left+=1
            right-=1
        else:
            return (
                isPalindrome(s,left,right-1) or isPalindrome(s,left+1,right)
            )
    return True



arr = [1,2,3,4,5,6]
reverseArr(arr)
print(arr)
s = "abba"
if isPalindrome(s):
    print("Palindrome")
else:
    print("Not a Palindrome")
arr1 = [1,2,4,7,11]
tar = 15
ans1 = twoSum(arr1,tar)
print(ans1)
arr2 = [1,1,2,2,2,3,3,3,3,4]
ans2 = removeDuplicates(arr2)
print(ans2)
arr3 = [0,1,0,3,12]
ans3 = moveZeros(arr3)
print(ans3)
arr4= [-5,-4,-2]
ans4 = sqaureSort(arr4)
print(ans4)
s1 = "abcdecba"
if validPalindrome(s1):
    print("Palindrome")
else:
    print("Not a Palindrome")
