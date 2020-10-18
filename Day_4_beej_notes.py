'''
Subroutines

Like simple functions
 - No function arguments
 - No return values

When we call a function:
 - Push the return address on the stack
 - Set the PC to the function address

When we return:
 - Pop the return address off the stack, store it in the PC

'''

def bar():
    print("hello again")
    return

def foo():
    print("hi there") # <-- PC
    bar()
    print("And we're back") #addr_2
    bar()
    print("And we're back again") #addr_3
    return

foo()
print("Done!") #addr_1 <-- PC

#Stack top -->
