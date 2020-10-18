'''
The Stack

LIFO

Whatever we push last is the first thing we pop.

1. Someplace to store data (main memory)
2. A way to keep track of the top of the stack (the last thing pushed)
 - track the index of the last thing pushed
 - we track that in the Stack Pointer

- Stack Pointer (SP) is stored at R7 in the LS-8 cpu
- Stack will start at hex F3
- Stack pointer is the index of where the top of stack is
- Moving value from register to the stack (PUSH onto stack)
- Or moving value from stack into register (POP value from stack)
- Pointer will point to address at F4 if the stack is empty
- Imagine a stack of plates that is growing DOWN from the ceiling. That's our stack

- If stack gets too big? That is a stack overflow. 


PUSH
1. Decrement SP (R7)
2. Copy the value from the register to top of stack

POP
1. Copy value from top of stack into register
2. Increment SP (R7)
 '''