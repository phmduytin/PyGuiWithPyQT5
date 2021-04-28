s = "XIX"
dic = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000, "IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400,
       "CM": 900}

sCheck = ["IV", "IX", "XL", "XC", "CD", "CM"]

n = len(s)
s = s + " "

num = 0

i = 0
while i < n:
    ss = s[i] + s[i + 1]
    if sCheck.__contains__(ss):
        num += int(dic[ss])
        i += 2
    else:
        num += int(dic[s[i]])
        i += 1

