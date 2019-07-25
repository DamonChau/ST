import sys
import math
words = list()
for line in sys.stdin:
    item = [element for element in line.split(' ')]
    words.append((item[0].upper(), int(item[1])))

totalWords = 0
for k,v in words:
    totalWords += v

words.sort(key=lambda x: x[1], reverse=True)
for word, value in words:
    print(word.ljust(20)+'\t[',end='')
    percentage = math.ceil(value*100/totalWords)
    sign = (percentage+4)//5
    print('*'*sign+'] ', percentage,'%', sep='')