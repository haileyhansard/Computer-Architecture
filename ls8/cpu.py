"""CPU functionality."""
HLT = 0b00000001
LDI = 0b10000010
PRN = 0b01000111
MUL = 0b10100010
ADD = 0b10100000
SP = 0b00000111
POP = 0b01000110
PUSH = 0b01000101
CALL = 0b01010000
RET = 0b00010001
#Sprint#
CMP = 0b10100111
JMP = 0b01010100
JEQ = 0b01010101
JNE = 0b01010110




import sys

class CPU:
    """Main CPU class."""

    #Step 1: Add the Constructor to CPU
    def __init__(self):
        """Construct a new CPU."""
        self.reg = [0] * 8      #register stores information, there are 8 of them, so length is 8
        self.ram = [0] * 256    #ram is the memory array
        self.reg[SP] = 0xF4      #spec says that Reg 7 is the hex value 0xF4, now making this the SP, Step #10
        self.pc = 0             #initialize Program Counter at 0
        self.running = False    #boolean, program is not initially running
        self.fl = 0b00000000    #last 3 bits will change depeneding on CMP comparisons

        #Step 9: Beautify your Run() Loop
        self.branchtable = {}
        self.branchtable[HLT] = self.HLT
        self.branchtable[LDI] = self.LDI
        self.branchtable[PRN] = self.PRN
        self.branchtable[MUL] = self.MUL
        self.branchtable[ADD] = self.ADD
        self.branchtable[PUSH] = self.PUSH
        self.branchtable[POP] = self.POP
        self.branchtable[CALL] = self.CALL
        self.branchtable[RET] = self.RET
        #Sprint#
        self.branchtable[CMP] = self.CMP
        self.branchtable[JMP] = self.JMP
        self.branchtable[JEQ] = self.JEQ
        self.branchtable[JNE] = self.JNE




    #Step 2: Add RAM functions (ram_read() and ram_write())
    def ram_read(self, address): #array that reads argument "address"
        return self.ram[address]

    def ram_write(self, value, address):
        self.ram[address] = value #accept value to write, and write it to address in array
        

#DAY 2:
#Step 7: Un-hardcode the machine code
    def load(self):
        """Load a program into memory."""
        if len(sys.argv) != 2:
            print("filename error, please supply a filename to load")
            sys.exit(1)

        address = 0
        try:

            with open(sys.argv[1]) as f:
                for line in f:
                    comment_split = line.split('#') #splits line on the # symbol
                    code_value = comment_split[0].strip() # removes whitespace and \n character
                    if code_value == "":
                        continue #moves on if blank line

                    try:
                        num = int(code_value, 2) #base 2 for binary and change from string to int
                    except:
                        print("Cannot find instruction")
                    
                    self.ram[address] = num
                    address += 1
              
        except FileNotFoundError:
            print('file not found')
            sys.exit(2)


    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        if op == "ADD":
            self.reg[reg_a] += self.reg[reg_b]
        #elif op == "SUB": etc
    
        # Step 8: Add the MULT instruction
        elif op == "MUL":
            self.reg[reg_a] *= self.reg[reg_b]
        
        #Sprint#
        #fl bits: 00000LGE        
        #L: less than, set to 1 if regA < regB, otherwise0
        #G: greater than, set to 1 if regA > regB, otherwise 0
        #E: equal, set to 1 if regA == regB, otherwise 0
        elif op == "CMP":
            if self.reg[reg_a] < self.reg[reg_b]:
                self.fl = 0b00000100
            elif self.reg[reg_a] > self.reg[reg_b]:
                self.fl = 0b00000010
            else:
                self.fl = 0b00000001

        else:
            raise Exception("Unsupported ALU operation")

    def trace(self):
        """
        Handy function to print out the CPU state. You might want to call this
        from run() if you need help debugging.
        """

        print(f"TRACE: %02X | %02X %02X %02X |" % (
            self.pc,
            #self.fl,
            #self.ie,
            self.ram_read(self.pc),
            self.ram_read(self.pc + 1),
            self.ram_read(self.pc + 2)
        ), end='')

        for i in range(8):
            print(" %02X" % self.reg[i], end='')

        print()

    # Step 4: Implement the HLT instruction handler
    def HLT(self):
        self.running = False

    # Step 5: Add the LDI instruction
    def LDI(self):
        address = self.ram[self.pc + 1]
        value = self.ram[self.pc + 2]
        self.reg[address] = value
        self.pc += 3

    # Step 6: Add the PRN instruction
    def PRN(self):
        address = self.ram[self.pc + 1]
        print(self.reg[address])
        self.pc += 2

    def MUL(self):
        reg_a = self.ram[self.pc + 1]
        reg_b = self.ram[self.pc + 2]
        self.alu("MUL", reg_a, reg_b)
        self.pc += 3

    def ADD(self):
        reg_a = self.ram[self.pc + 1]
        reg_b = self.ram[self.pc + 2]
        self.alu("ADD", reg_a, reg_b)
        self.pc += 3

    #Step 10: Implement System Stack
    def PUSH(self):
        #Decrement the stack pointer
        #Takes in a register number and saves the value in it onto the stack
        #Store the value in the register onto the top of the stack
        #the topmost value of the stack is self.reg[SP]
        self.reg[SP] -= 1
        addressOfReg = self.ram[self.pc + 1]
        value = self.reg[addressOfReg]
        self.ram[self.reg[SP]] = value
        self.pc += 2

    def POP(self):
        #save the value on top of the stack onto the register given
        #increment the stack pointer
        addressOfReg = self.ram[self.pc + 1]
        value = self.ram[self.reg[SP]]
        self.reg[addressOfReg] = value
        self.reg[SP] += 1
        self.pc += 2

    #Step 11: Implement CALL and RET, Implement Subroutine calls
    def CALL(self):
        #compute the return address
        #push return address onto stack
        #get the value from the operand reg
        #set the self.pc to that value
        address = self.ram[self.pc + 1]
        value = self.reg[address]
        self.reg[SP] -= 1
        self.ram[self.reg[SP]] = self.pc + 2
        self.pc = value

    def RET(self):
        #compute the return address
        #get the top of stack address
        #get the value at the top of the stack
        #increment the SP
        #set it to pc
        address = self.ram[self.reg[SP]]
        self.reg[SP] += 1
        self.pc = address

    #Sprint#
    def CMP(self):
        #conditionals for equal flag handled in the alu
        reg_a = self.ram[self.pc + 1]
        reg_b = self.ram[self.pc + 2]
        self.alu("CMP", reg_a, reg_b)
        self.pc += 3

    def JMP(self):
        #jump to address stored in the given register
        #set pc to the address stored in the given register
        reg_address = self.ram[self.pc + 1]
        self.pc = self.reg[reg_address]

    def JEQ(self):
        #jump if equal
        #if equal flag is set to true, jump to address stored in the given register
        #otherwise, skip these instructions
        if self.fl == 0b00000001:
            reg_address = self.ram[self.pc + 1]
            self.pc = self.reg[reg_address]
        else: self.pc += 2

    def JNE(self):
        #jump if not equal
        #if equal flag is false, 0, jump to address stored in the given register
        #otherwise, skip these instructions
        if self.fl != 0b00000001:
            reg_address = self.ram[self.pc + 1]
            self.pc = self.reg[reg_address]
        else:
            self.pc +=2

    #Step 3: Implement the core of CPU's run() method
    #Execution sequence in the spec
    def run(self):
        """Run the CPU."""
        self.running = True
        
        while self.running:
            ir = self.ram[self.pc]  #IR = The Instruction Register, contains copy of currently executing instruction
            #PC points to the instruction to execute
            if ir in self.branchtable:
                self.branchtable[ir]()
                # self.trace()
            else:
                print(f"Unknown instruction {ir}") #Otherwise, give the program an "out" if an unknown instruction occurs
                sys.exit(3)
            

#Step 3 ALT with Mari's Lecture:
    # def runAlt(self):
    #     self.running = True

    #     while self.running:
    #         instruction_to_execute = self.ram_read(self.pc)
    #         operand_a = self.ram_read(self.pc + 1)
    #         operand_b = self.ram_read(self.pc + 2)
    #         self.execute_instruction(instruction_to_execute, operand_a, operand_b)

    # def execute_instruction(self, instruction, operand_a, operand_b):
    #     if instruction == HLT:
    #         self.running = False
    #         self.pc += 1
    #     elif instruction == LDI:
    #         self.reg[operand_a] = operand_b
    #         self.pc += 3
    #     elif instruction == PRN:
    #         print(self.reg[operand_a])
    #         self.pc += 2


#From Day 1 Hardcoded load(self)
    # def load(self):
    #     """Load a program into memory."""
    #     address = 0

    #     # For now, we've just hardcoded a program:

    #     program = [
    #         # From print8.ls8
    #         0b10000010, # LDI R0,8
    #         0b00000000,
    #         0b00001000,
    #         0b01000111, # PRN R0
    #         0b00000000,
    #         0b00000001, # HLT
    #     ]
        
    #     for instruction in program:
    #         self.ram[address] = instruction
    #         address += 1


# From Day 1 original while loop in run() function:

# if ir == HLT: #If the Instruction Register is at instruction HLT, execute HLT function
#                 self.HLT()
            
#             elif ir == LDI: #If the Instruction Register is at instruction LDI, execute LDI function
#                 self.LDI()

#             elif ir == PRN: #If the Instruction Register is at instruction PRN, execute PRN function
#                 self.PRN()

#             elif ir == MUL:
#                 reg_a = self.ram[self.pc + 1]
#                 reg_b = self.ram[self.pc + 2]
#                 self.alu("MUL", reg_a, reg_b)
#                 self.pc += 3