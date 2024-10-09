# def check_if_palindrome(s):
#     left = 0
#     right = len(s) - 1
#     if right%2==1:
#        return False

#     while left <= right:
#         if s[left] != s[right]:
#             return False
#         left += 1
#         right -= 1
    
#     return True

# print(check_if_palindrome("abxba"))



def kiemtra(s):
    sum=0
    dem=0
    average=0
    for num in s:
        if num.isdigit():
            sum+=int(num)
            dem+=1
    average=sum/dem
    return sum,average
print(kiemtra("Yafuo3@fa9qua321"))


