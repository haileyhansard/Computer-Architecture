"""CPU functionality."""
HLT = 0b00000001
LDI = 0b10000010
PRN = 0b01000111

import sys

class CPU:
    """Main CPU class."""

    #Step 1: Add the Constructor to CPU
    def __init__(self):
        """Construct a new CPU."""
        self.reg = [0] * 8      #register stores information, there are 8 of them, so length is 8
        self.ram = [0] * 256    #ram is the memory array
        self.reg[7] = 0xF4      #spec says that Reg 7 is the hex value 0xF4
        self.pc = 0             #initialize Program Counter at 0
        self.running = False    #boolean, program is not initially running

    #Step 2: Add RAM functions (ram_read() and ram_write())
    def ram_read(self, address): #array that reads argument "address"
        return self.ram[address]

    def ram_write(self, value, address):
        self.ram[address] = value #accept value to write, and write it to address in array
        

    def load(self):
        """Load a program into memory."""
    #RAM
        address = 0

        # For now, we've just hardcoded a program:

        program = [
            # From print8.ls8
            0b10000010, # LDI R0,8
            0b00000000,
            0b00001000,
            0b01000111, # PRN R0
            0b00000000,
            0b00000001, # HLT
        ]

        for instruction in program:
            self.ram[address] = instruction
            address += 1


    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        if op == "ADD":
            self.reg[reg_a] += self.reg[reg_b]
        #elif op == "SUB": etc
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


    #Step 3: Implement the core of CPU's run() method
    #Execution sequence in the spec
    def run(self):
        """Run the CPU."""
        self.running = True
        
        while self.running:
            ir = self.ram[self.pc]  #IR = The Instruction Register, contains copy of currently executing instruction
                                    #PC points to the instruction to execute
            
            if ir == HLT: #If the Instruction Register is at instruction HLT, execute HLT function
                self.HLT()
            
            elif ir == LDI: #If the Instruction Register is at instruction LDI, execute LDI function
                self.LDI()

            elif ir == PRN: #If the Instruction Register is at instruction PRN, execute PRN function
                self.PRN()

            else:
                print(f"Unknown instruction {ir}") #Otherwise, give the program an "out" if an unknown instruction occurs
            

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
