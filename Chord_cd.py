#!/usr/bin/env python
#http://codeforces.com/problemset/problem/88/A
import itertools
NOTES = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'B', 'H', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'B', 'H']    
t = raw_input().split(' ')
for x in  list(itertools.permutations(t)):
    d1 = NOTES[NOTES.index(x[0],):].index(x[1])
    d2 = NOTES[NOTES.index(x[1],):].index(x[2])
    if d1 == 4 and d2 ==3:
        print "major"
        exit()
    elif d1==3 and d2==4:
        print "minor"
        exit()
print 'strange'
