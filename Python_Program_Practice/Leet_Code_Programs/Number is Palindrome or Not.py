##Palindrome Number
#Given an integer x, return true if x is a palindrome, and false otherwise.

class solution:
    def ispalindrome(self,num):
        num = str(num)
        if num == num[::-1]:
            return True
        else:
            return False


num = int(input("Enter the Number : "))
sol = solution()

print(sol.ispalindrome(num))


