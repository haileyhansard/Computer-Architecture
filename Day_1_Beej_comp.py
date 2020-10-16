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
PUSH = 5
POP = 6
CALL = 7
RET = 8

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

#DAY 3, The Stack 
SP = 7

register[SP] = 0xf4 #Stack Pointer

address = 0

if len(sys.argv) != 2:
    print("Usage: compy.py progname")
    sys.exit(1)

try:
    with open(sys.argv[1]) as f:
        for line in f:
            line = line.strip()

            if line == "" or line[0] == "#":
                continue
            try:
                str_value = (line.split("#")[0])
                value = int(str_value, 10)

            except ValueError:
                print(f"Invalid number: {str_value}")
                sys.exit(1)

            memory[address] = value
            address += 1
except FileNotFoundError:
    print(f"File not found: {sys.argv[1]}")
    sys.exit(2)

#Start execution at address 0

#Keep track of the address of the currently-executing instruction
pc = 0 #Program Counter, pointer to the instruction we're executing

halted = False

#Day 4: Call/Ret Subroutines

def push_val(value):
    #decrement the stack pointer
    register[SP] -= 1
    #copy the value onto the stack
    top_of_stack_addr = register[SP]
    memory[top_of_stack_addr] = value

def pop_val():
    #get value from the top of stack
    top_of_stack_addr = register[SP]
    value = memory[top_of_stack_addr] #want to put this in a reg
    #increment the SP
    register[SP] += 1
    return value



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

    elif instruction == PUSH:
        #decrement the stack pointer
        register[SP] -= 1
        #grab the vaue out of the given register
        reg_num = memory[pc + 1]
        value = register[reg_num] #this is what we want to push
        top_of_stack_addr = register[SP] #copy the value onto the stack
        memory[top_of_stack_addr] = value
        pc += 2
        #print(memory[0xf0:0xf4])

    elif instruction == POP:
        #get the value from top of stack
        top_of_stack_addr = register[SP]
        value = memory[top_of_stack_addr] #want to put this in a reg
        #store in a reg
        reg_num = memory[pc + 1]
        register[reg_num] = value
        #increment the SP
        register[SP] += 1
        pc += 2

    elif instruction == CALL:
        #get the address of the next instruction after the CALL
        return_addr = pc + 2
        #push it on the stack
        push_val(return_addr)
        #get the subroutine address from register
        reg_num = memory[pc + 1]
        subroutine_addr = register[reg_num]
        #jump to it
        pc = subroutine_addr

    elif instruction == RET:
        #get the return addr from the top of stack
        return_addr = pop_val()
        #store it in the pc
        pc = return_addr


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

