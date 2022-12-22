res = 0
dic_num = {
    'I':1,
    'V':5,
    'X':10,
    'L':50,
    'C':100,
    'D':500,
    'M':1000
}

def create_array_of_num(s):
    res_arr = []
    for i in s:
        res_arr.append(dic_num[i])
    return res_arr

def result(s):
    res = 0
    res_arr = create_array_of_num(s)
    for i in range(len(res_arr)):
        if i != len(res_arr) - 1:
            if res_arr[i] < res_arr[i + 1]:
                res -= res_arr[i]
            else:
                res += res_arr[i]
        else:
            res += res_arr[i]
    return res

class Solution(object):


    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        res_arr = create_array_of_num(s)
        for i in range(len(res_arr)):
            if i != len(res_arr) - 1:
                if res_arr[i] < res_arr[i + 1]:
                    res -= res_arr[i]
                else:
                    res += res_arr[i]
            else:
                res += res_arr[i]
        return res
