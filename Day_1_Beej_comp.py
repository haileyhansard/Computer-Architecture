import sys

# Program consists of multiple instructions to do ...something.
# We store these instructions in memory.
#To get or set data in memory, you need the index in the array

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

memory = [
    1, #Print Beej
    3, #Save a value in register: Store value 37 in register 1 : r[1] = 37
    1, #R1, The register number (How does cpu know the diff between instruction 1 and this 1? Timing. We’re telling it to grab 1 and put it as the register and then have pc skip it. Because we added +=3 to pc in the elif instruction == 3)
    37, #The value we want to store there
    4, #Print register 1 : print(r[1])
    1, #We need register number here, R1
    1, #Print Beej
    2  #Halt
]

#Variables are called "registers"
    # there are a fixed number of them 
    # and they have fixed names

#Registers can each hold a single byte.

register = [0] * 8 #[0,0,0,0,0,0,0,0]
    
#Start execution at address 0

#Keep track of the address of the currently-executing instruction
pc = 0 #Program Counter, pointer to the instruction we're executing

halted = False

while not halted:
    instruction = memory[pc]

    if instruction == 1: #Print Beej
        print("Beej!")
        pc += 1  #this moves the pc (program counter) to the next instruction, otherwise it will get stuck in an infinite loop!

    elif instruction == 2: #Halt
        halted = True
        pc += 1

    elif instruction == 3: #Save_Reg
        reg_num = memory[pc + 1]
        value = memory[pc + 2]
        register[reg_num] = value
        print(register)
        pc += 3

    elif instruction == 4: #Print_Reg
        reg_num = memory[pc + 1]
        print(register[reg_num])
        pc += 2
    
    else:
        print(f"unknown instruction {instruction}")
        sys.exit(1)

