#!/usr/bin/env python
#http://codeforces.com/problemset/problem/296/A
n = input()
arr = map(int, raw_input().split())
d = {}
for i in arr:
    if i in d: d[i]+=1
    else: d[i]=1       
print 'YES' if max(d.values()) <= ((n+1)/2) else 'NO'
