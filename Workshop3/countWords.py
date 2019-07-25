import sys

dropChars = "!@#$%^_+-={}()[]|\\:;\"'<>,.?/1234567890"
dropDict = dict([(c, ' ') for c in dropChars])
dropTable = str.maketrans(dropDict)

count = {} 
if len(sys.argv) > 1:
    for i in range(1,len(sys.argv)):
        for line in open(sys.argv[i]):
            words = line.upper().translate(dropTable).split()
            for word in words:
                if word in count:
                    count[word] += 1
                else:
                    count[word] = 1
# else:
#     for line in sys.stdin:
#         words = line.upper().translate(dropTable).split()
#         for word in words:
#             if word in count:
#                 count[word] += 1
#             else:
#                 count[word] = 1


for word in sorted(count, key=count.get, reverse=True):
    print(word, count[word])