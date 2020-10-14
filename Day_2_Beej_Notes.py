'''
Bitwise Operators 

A  B  A and B  &
----------------
0  0    0
0  1    0
1  0    0
1  1    1

Use 'and' like a stencil, that lets the numbers shine through...

A  B    A or B |
----------------
0  0    0
0  1    1
1  0    1
1  1    1

A    not A ~
-------------
1    0
0    1

0b1010101
& 0b1111000
------------
0b1010000

'''

print(bin(0b1010101 & 0b1111000))