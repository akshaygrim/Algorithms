class Solution:
    def palidrome(n):
        temp = n
        rev = 0
        while(n>0):
           digit = n%10
           rev = rev*10+digit
           num = num//10
        if temp == rev:
            print("the number is palindrome")
        else :
            print("not a palindrome")
            
      
          
            
        
        
