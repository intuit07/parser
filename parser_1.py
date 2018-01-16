from google import google
import sys

word = sys.argv[1]
s_res = google.search(word, 2)
count = 0
while count < 10:
    count += 1
    for el in s_res:
        res = str(count) + '.' + str(el)
    print(res)

