class Solution:
    def romanToInt(self, s: str) -> int:
        
        self.s = s
        dic = {

        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
        
        lst = []
        data_list = []

        prev_num = 0
        current_num = 0
        total = 0

        for i in range(len(s)):
            current_num = dic[s[i]]
            if current_num > prev_num:
                total  = total + current_num - 2* prev_num
            else:
                total += current_num
            prev_num = current_num
        return(total)
