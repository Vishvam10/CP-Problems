"""
DIFFICULTY : hard
TAGS : math, string, recursion
"""
class Solution:
    # IDEA : Split into groups of 3 (think of addding commas)
    #        Then compute the english version of a group and add
    #        a prefix according to the group number. 
    #        For eg. in 23,123,654, engligh version of group 123 
    #        is "one hundred twenty three". Then add a suffix based
    #        on the group, here it is thousand. 
    #        (For numbers between 10 and 19, have a new map)
    def numberToWords(self, num: int) -> str:
        if(num == 0) :
            return "Zero"

        # s = list(str(num))
        # n = len(s)

        # a = []
        # for i in range(n) :
        #     if(i % 3 == 0 and i != 0) :
        #         a.append(",")    
        #     a.append(s[n-i-1])

        # a.reverse()

        # num_with_commas = "".join(a)

        # print(num_with_commas)

        s = str(num)
        n = len(s)

        rem = n % 3
        quo = n // 3
        temp = ""

        mp1 = {
            "0": "",
            "1": " One",
            "2": " Two", 
            "3": " Three", 
            "4": " Four",
            "5": " Five", 
            "6": " Six", 
            "7": " Seven", 
            "8": " Eight", 
            "9": " Nine"
        }

        mp2 = {
            "0": "",
            "1": "",
            "2": " Twenty", 
            "3": " Thirty", 
            "4": " Forty",
            "5": " Fifty", 
            "6": " Sixty", 
            "7": " Seventy", 
            "8": " Eighty", 
            "9": " Ninety"
        }

        mp3 = {
            0: "", 
            1: " Thousand", 
            2: " Million", 
            3: " Billion", 
            4: " Trillion",
            5: " Quadrillion",
            6: " Quintillion",
            7: " Sextillion",
            8: " Septillion",
            9: " Octillion",
            10: " Nonillion",
            11: " Decillion"
        }

        mp4 = {
            "10" : " Ten",
            "11" : " Eleven",
            "12" : " Twelve",
            "13" : " Thirteen",
            "14" : " Fourteen",
            "15" : " Fifteen",
            "16" : " Sixteen",
            "17" : " Seventeen",
            "18" : " Eighteen",
            "19" : " Nineteen"
        }

        ans = ""

        if(rem != 0) :
            temp = s[0:rem]

        for i in range(rem, n, 3) :
            substr = s[i:i+3]
            hundreds_place = ""
            tenths_place = ""
            ones_place = ""

            hundreds_place = mp1[substr[0]] + " Hundred" if substr[0] != "0" else ""
            if(substr[1] != "0") :
                if(substr[1] != "1") :
                    tenths_place = mp2[substr[1]]
                    ones_place = mp1[substr[2]]
                else :
                    temp_val = substr[1] + substr[2]
                    tenths_place = mp4[temp_val]
            else :
                ones_place = mp1[substr[2]]
            
            val = (hundreds_place + tenths_place + ones_place)
            group = (n-i-1) // 3

            if(len(val) != 0) :
                val += (mp3[group])
                ans += val
                
            # print(hundreds_place, tenths_place, ones_place)  
            # print(val)

        temp_val = ""

        if(len(temp) == 2) :
            if(temp[0] != "1") :
                temp_val = mp2[temp[0]] + mp1[temp[1]]
            else :
                temp_val = mp4[temp]
            temp_val += mp3[quo]
        elif(len(temp) == 1) :
            temp_val = mp1[temp[0]]
            temp_val += mp3[quo]
            
        ans =  temp_val + ans
        ans = ans.strip()

        # print("ANSWER : ", ans)

        return ans
