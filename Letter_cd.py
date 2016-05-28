#!/usr/bin/env python

h, m = map(int, raw_input().split(' '))

graph = [0]*h
for i in range(h):
    graph[i]=[0]*w

h_indices = list()
w_indices = list()
for i in range(h):
    l = raw_input()
    graph[i]=l
    s = l.find('*')
    e = l.rfind('*')
    if s!= -1:
        w_indices.append(s);w_indices.append(e)
        h_indices.append(i)

h_limits=[min(h_indices), max(h_indices)]
w_limits=[min(w_indices), max(w_indices)]
for i in range(h_limits[0], h_limits[1]+1):
    print graph[i][w_limits[0]:w_limits[1]+1]