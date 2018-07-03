#!/usr/bin/env python
import sys

s = sys.argv[1]

temp_list = []
for i in range(len(s)):
    for j in range(len(s)):
        if len(s[i:j+1])>0:
            temp_list.append(s[i:j+1])

pali_list = []
for item in temp_list:
    to_include = True
    if len(item) == 1:
        pali_list.append(item)
    else:
        if item[0] == item[-1]:
            pass
        else:
            to_include = False

        if len(item)%2 == 0:
            eff_len = len(item)
        else:
            eff_len = len(item) - 1

        count = 1
        while count < (eff_len/2):
            if item[count] == item[-(count+1)]:
                pass
            else:
                to_include = False
            count += 1

        if to_include == True:
            pali_list.append(item)

print pali_list
print len(pali_list)
