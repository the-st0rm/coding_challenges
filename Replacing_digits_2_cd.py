#!/usr/bin/env python
#http://codeforces.com/problemset/problem/169/B
str1 = list(raw_input())
str2 = list(raw_input())

str2.sort(reverse=True)
counter = 0

for i in xrange(len(str1)):
    if counter < len(str2):
        if str1[i]<str2[counter]:
            str1[i]=str2[counter]
            counter+=1
        
print ''.join(str1)
