'''this is bit masking example'''

'''INSTRUCTION = 0b10000010 ---> we want to turn it into this ---> 0b00000010 ---> and we can only access the 2 digits on the far right 
 - the operand takes 2 bits, the first 2 bits "AA" in the operand string
 - we want to get those 2 bits all the way to the right, so end result we want is 
 - So & 0b00000011 so that we "turn on" the last 2 bits
'''

# INSTRUCTION = 0b10000010
# PC = 0
# instructionSize = ((INSTRUCTION >> 6) & 0b11) + 1
# PC += instructionSize

import sys
#allows us to access the arguments assed in to the command line
#python3 mari_example.py print8.ls8
# sys.argv[0] = mari_example.py
# sys.argv[1] = print8.ls8
if len(sys.argv) != 2:
    print('womp!')
    sys.exit(1)

try:
    with open(sys.argv[1]) as f:
        for line in f:
            print(line)
            #this will print the file line by line
            comment_split = line.split("#")
            num = comment_split[0]
            
            try:
                x = int(num, 2) #give it base 2 because we want binary
                print(x)
            except:
                print('cannot convert string to number')
                continue

except:
    print('file not found')
    sys.exit(1)