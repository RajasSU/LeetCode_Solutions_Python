ROMAN TO INTEGER PYTHON3

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.
Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:
I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.

Example 1:
Input: s = "III"
Output: 3

Example 2:
Input: s = "IV"
Output: 4

############################### START CODE ###############################
class Solution:
    def romanToInt(self, s: str) -> int:
        find={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        r_l= list(s)
        length= len(r_l)
        num=0
        '''
        if r_l[:-1] == r_l[1:]:
            #print("Hi")
            for i in r_l:
                #print("Hello")
                num= num + find[i]
            return num
           '''     
        num= find[r_l[length-1]]
        for i in range(length-1,0,-1):
            current_num= find[r_l[i]]
            pre_num= find[r_l[i-1]]
            if pre_num<current_num:
                num = num - pre_num
            else:
                num= num + pre_num
        return num
############################### END CODE ###############################