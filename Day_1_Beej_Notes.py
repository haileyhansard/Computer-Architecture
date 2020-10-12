"""
NOTES

Number Bases

Base 2 - Binary
Base 8 - octal
Base 10 - decimal
Base 16 - hexadecimal ("hex")
Base 64 - "base 64"

Decimal, Base 10: Digits 0 - 9
So 10 would mean 0 ones and 1 ten
12 would be 2 ones and 1 ten
100 would be 1 on-hundred, 0 tens, 0 ones
The "place" names are: the ones place, the tens place, the hundreds place _ _ _

---> Binary, Base 2: Digits ("bits"): 0 - 1
   0
   1
  10
  11
 100
 101
 110
 111
1000
||||
|||+----- 1s place     0b1
||+------ 2s place    0b10
|+------- 4s place   0b100
+-------- 8s place  0b1000

The number base is important when you write the number down. Otherwise its not important.
When you write it in code, when its in a file, etc.

Prefix the number with an indicator of the base.

0b for binary
0x for hex
0o for octal (rarely used)

---> Hex, Base 16, Digits 0-9, A-F, then 10
0123456789ABCDEF10,11,12,13,14,15,16,17,18,19,1A,1B,1C,1D,1E,1F,20

RR GG BB
#ff021d

ff hex = what in binary?

0x87 == 0b??? what in binary?

1 hex digit === 4 binary digits

Convert 87 hex to binary:
hex:     8    , 7
         ???? , ????
binary:  1000   0111 (we need the leading 0 here because 1 hex digit is 4 binary digits)

Convert 0x0C hex to decimal to binary:
hex:    0x0C  (C is 12 decimal, so find powers of 2 that add up to 12)
binary: 0b 0000 1100

Convert 0xFF to binary:
0x    F    F (F is 15 decimal)
0b ???? ????
0b 1111 1111

So FF = 255 decimal. 
Because FF hex == 1111111 binary, if you add up the digits you have:
1 one
1 two
1 four
1 eight
1 sixteen
1 thirty two
1 sixty four
1 one hundred twenty eight
128 + 64 + 32 + 16 + 8 + 4 + 2 + 1 = 255 decimal

"""
print(bin(0x87))
print(bin(0x0C))

x = 15 + 35
print(x)

y = 0b110
print(y)

a = 12
print(f'{a}')
print(f'{a:x}')

print(bin(21))
print(hex(21))