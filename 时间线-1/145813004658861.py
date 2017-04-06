import random
import string
import sys
if sys.version_info[0] == 3:
    print ("Welcome to qlcoder!")
    print ("We find your Python version is python3.X")
    print ("But this script needs to be executed with Python2.X\n")
    exit()

random.seed(10)
limit = 10000000
out = open('timeline.txt', 'w')
for i in range(limit):
    r = random.randint(1, limit)
    if i % 3 == 0:
        out.write('p ' + str(r) + ' ' + ''.join(random.sample(string.ascii_letters, 4)) + '\r\n')
    else:
        out.write('v ' + str(r) + '\r\n')
