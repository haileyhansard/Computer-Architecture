import sys

# Program consists of multiple instructions to do ...something.
# We store these instructions in MEMORY.
# Memory holds bytes.  abig array of bytes.
# To get or set data in memory, you need the index in the array

# These terms are equivalent:
# Index into the memory array
# Address
# Location
# Pointer

#opcode == the instruction byte
#operands == arguments to the instruction

#memory can only hold numbers

#You can assign your numbers in memory to what the instruction is so that the program is easier to read
PRINT_BEEJ = 1
HALT = 2
SAVE_REG = 3
PRINT_REG = 4
PRINT_NUM = 5
#ADD = 6

#Add takes TWO registers, adds their values
# and stores the result in the first register given


#DAY 1
# memory = [
# #     1,  # PRINT_BEEJ  
# #     3,  # SAVE_REG R1, 37: Save a value in register AKA Store value 37 in register 1 : r[1] = 37
# #     1,  # R1, The register number (How does cpu know the diff between instruction 1 and this 1? Timing. We’re telling it to grab 1 and put it as the register and then have pc skip it. Because we added +=3 to pc in the elif instruction == 3)
# #     37, # The value we want to store there
# #     4,  # PRINT_REG R1 : Print register 1 : print(r[1])
# #     1,  # R1, We need register number here, R1
# #     1,  # PRINT_BEEJ
# #     2   # HALT
# ]

#DAY 2
memory = [0] * 256

#Variables are called "registers"
    # there are a fixed number of them 
    # and they have fixed names: R0, R1, R2, R3, ... R7

#Registers can each hold a single byte.

register = [0] * 8 #[0,0,0,0,0,0,0,0] 8 because 8-bit CPU

#DAY 2 
#Read program data

address = 0

with open("prog1.py") as f:
    for line in f:
        line = line.strip()
        value = int(line.split("#")[0])
        print(line)

sys.exit(0)

#Start execution at address 0

#Keep track of the address of the currently-executing instruction
pc = 0 #Program Counter, pointer to the instruction we're executing

halted = False

while not halted:
    instruction = memory[pc]

    if instruction == PRINT_BEEJ: #Print Beej
        print("Beej!")
        pc += 1  #this moves the pc (program counter) to the next instruction, otherwise it will get stuck in an infinite loop!

    elif instruction == HALT: #Halt
        halted = True
        pc += 1

    elif instruction == SAVE_REG: #Save_Reg
        #Ssave some value to some register
        reg_num = memory[pc + 1]
        value = memory[pc + 2]
        register[reg_num] = value
        print(register)
        pc += 3

    elif instruction == PRINT_REG: #Print_Reg
        reg_num = memory[pc + 1]
        print(register[reg_num])
        pc += 2

    # elif instruction == ADD:
    #     # get reg 1
    #     # get reg 2
    #     # add them, and store the result in the first reg given
    #     reg_1 = memory[pc + 1]
    #     reg_2 = memory[pc + 2]
    #     register[reg_1] += register[reg_2]
    #     pc += 3

    
    else:
        print(f"unknown instruction {instruction} at address {pc}")
        sys.exit(1)

