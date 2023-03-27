class Solution :
    def reverse_digit(n):
        new_n = str(n)
        reverse_n = new_n[::-1]
        out_n = int(reverse_n)
        print(out_n)
    
    reverse_digit(12345)