'''
 Longest Common Prefix
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

Constraints:
0 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lower-case English letters.

'''
############################### START CODE ###############################
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        match= []
        strs.sort()
        if len(strs)==0:
            return ''
        if len(strs)==1:
            return "".join(strs)
        for i in range(len(strs[0])):
                if(strs[0][i]==strs[-1][i]):
                    match.append(strs[0][i])
                else:
                    break        
                    
        match= "".join(match)
        return match
############################### END CODE ###############################        