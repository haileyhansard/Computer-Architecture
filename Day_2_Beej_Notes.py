'''
Bitwise Operators 

&  AND will return 1 if BOTH are 1
|  OR will return 1 is EITHER is 1 (also if both are 1, you will return 1)
^  XOR will return 1 ONLY if ONE of the bits is 1, not both
~  NOT will return the opposite value (Not 0 is 1)


A  B  -> A and B   &
----------------
0  0     0
0  1     0
1  0     0
1  1     1

Use 'and' like a stencil, that lets the numbers shine through if both are 1s...

A  B   -> A or B  | 
----------------
0  0      0
0  1      1
1  0      1
1  1      1


A  B  ->  A XOR B  ^
-----------------
0  0      0
0  1      1
1  0      1
1  1      0

A   not A  ~
-------------
1    0
0    1


   0b1010101
&  0b1111000
------------
-> 0b1010000

'''

print(bin(0b1010101 & 0b1111000))

a = 0b01011010
b = 0b10101111

print(bin(a & b))
print(bin(a | b))
print(a | b)

'''
Bit Shifting

Shifting bits to the right or left

A >> 1 : shift A right 1 bit
A << 3 : shift A left 3 bits

0b1110 >> 1 = 0b0111 (scoot to the right, adding a 0 to the front because its now "off" or empty)
'''

print(bin(0b1110 >> 1))

'''
Bit Masking

Used to turn bits on/off to 0/1
Can be used to get status of bits
Can be used to extract the number of arguments in an instruction for our project

'''
instruction = 0b11000010 # LDI
shifted = instruction >> 6
print(bin(shifted)) #returns 0b11  because first 2 digits moved 6 digits right to the last 2 digits

#Now if we want to grab the '11' in the following instruction2, we could use a BITWISE OPERATOR to turn all the digits before 11 to 0
instruction2 = 0b10011010
shifted2 = instruction2 >> 3
mask = 0b00000011 & shifted2 
print(bin(mask)) #prints 0b11 because we shifted the digits of the 4th and 5th digits to the 7th and 8th spots. then masked the bits with the & operator to make all the digits turn to 0 until the last 2 digits, which are "turned on" to 1

print(bin(0b00010001 & 0b11110000))
print(bin(0b01100001 | 0b10000100))

print(hex(0b00001110))