class Solution:

    def myAtoi(s):
        chk = 0
        num = ""
        for i in s:
            if i == '-':
                if num != "":
                    break
                num = '-'
                chk = 1
            elif i == '+':
                if num != "":
                    break
                num = '+'
            elif i == ' ':
                if num!="":
                    break
                else:
                    continue
            elif i >= '0' and i <= '9':
                num += i
            else:
                break

        if num == "" or num=="-" or num=="+":
            return 0
        else:
            if chk == 0:
                if int(num) > (2 ** 31 - 1):
                    return 2 ** 31 - 1
                else:
                    return int(num)
            else:
                if int(num) < (-2 ** 31):
                    return (-2 ** 31)
                else:
                    return int(num)


a = Solution
s = "    +0 32 423423423234423+dfsfsd2"
print(a.myAtoi(s))
