#! /usr/bin/env python3

import aoc


# There are two types of operands; each instruction specifies the type of its operand. The value of a literal operand is the operand itself. For example, the value of the literal operand 7 is the number 7. The value of a combo operand can be found as follows:

#     Combo operands 0 through 3 represent literal values 0 through 3.
#     Combo operand 4 represents the value of register A.
#     Combo operand 5 represents the value of register B.
#     Combo operand 6 represents the value of register C.
#     Combo operand 7 is reserved and will not appear in valid programs.
def combo(operand):
    match operand:
        case 0 | 1 | 2 | 3:
            return operand
        case 4:
            return A
        case 5:
            return B
        case 6:
            return C
        case 7 | _:
            raise SyntaxError(f"bad combo value {operand}")

# The eight instructions are as follows:
opcodes = [None] * 8

# The adv instruction (opcode 0) performs division. The numerator is the value in the A register.
# The denominator is found by raising 2 to the power of the instruction's combo operand. (So, an operand of 2 would
# divide A by 4 (2^2); an operand of 5 would divide A by 2^B.) The result of the division operation is truncated to an
# integer and then written to the A register.
def adv(operand):
    global A
    if (value := combo(operand)) == 0:
        return
    A = A // (2 << (value-1))
opcodes[0] = adv

# The bxl instruction (opcode 1) calculates the bitwise XOR of register B and the instruction's literal operand,
# then stores the result in register B.
def bxl(operand):
    global B
    B = B ^ operand
opcodes[1] = bxl

# The bst instruction (opcode 2) calculates the value of its combo operand modulo 8 (thereby keeping only its lowest
# 3 bits),
# then writes that value to the B register.
def bst(operand):
    global B
    B = combo(operand) % 8
opcodes[2] = bst

# The jnz instruction (opcode 3) does nothing if the A register is 0. However, if the A register is not zero, it jumps
# by setting the instruction pointer to the value of its literal operand; if this instruction jumps, the instruction
# pointer is not increased by 2 after this instruction.
def jnz(operand):
    global IP
    if A:
        IP = operand
opcodes[3] = jnz

# The bxc instruction (opcode 4) calculates the bitwise XOR of register B and register C, then stores the result in
# register B. (For legacy reasons, this instruction reads an operand but ignores it.)
def bxc(operand):
    global B
    B = B ^ C
opcodes[4] = bxc

# The out instruction (opcode 5) calculates the value of its combo operand modulo 8, then outputs that value.
# (If a program outputs multiple values, they are separated by commas.)
def out(operand):
    output.append(str(combo(operand) % 8))
opcodes[5] = out

# The bdv instruction (opcode 6) works exactly like the adv instruction except that the result is stored in the B
# register. (The numerator is still read from the A register.)
def bdv(operand):
    global B
    if (value := combo(operand)) == 0:
        return
    B = A // (2 << (value-1))
opcodes[6] = bdv

# The cdv instruction (opcode 7) works exactly like the adv instruction except that the result is stored in the C
# register. (The numerator is still read from the A register.)
def cdv(operand):
    global C
    if (value := combo(operand)) == 0:
        return
    C = A // (2 << (value-1))
opcodes[7] = cdv

# Here are some examples of instruction operation:

#     If register C contains 9, the program 2,6 would set register B to 1.
#     If register A contains 10, the program 5,0,5,1,5,4 would output 0,1,2.
#     If register A contains 2024, the program 0,1,5,4,3,0 would output 4,2,5,6,7,7,7,7,3,1,0 and leave 0 in register A.
#     If register B contains 29, the program 1,7 would set register B to 26.
#     If register B contains 2024 and register C contains 43690, the program 4,0 would set register B to 44354.

if aoc.test:
    A = 729
    program = (0,1,5,4,3,0)
else:
    A = 66245665
    A = 35
    program = (2,4, 1,7, 7,5, 1,7, 4,6, 0,3, 5,5, 3,0)
B = C = 0
output = []

if aoc.part == "one":
    IP = 0
    while len(program) > IP:
        instruction = opcodes[program[IP]]
        print(f"{IP}: {A=} {B=} {C=}", end= " ")
        IP += 1
        operand = program[IP]
        IP += 1
        print(f"{instruction.__qualname__}({operand})", end=" -> ")
        instruction(operand)
        print(f"{A=} {B=} {C=}")
    print()
    print(",".join(output))

if aoc.part == "two":
    A=1
    for i in reversed(program):
        A = (A << 3) + i
    print(A)

    print(int("".join(map(str, reversed((*program, 1)))), base=8))

# 18646497102114401565528 too high
# 89057482259288 too low
# 16313173343842 too low
# 130505386750737 no good
# 297788150054498 no good

# bst(4) : B = A % 8     -- last 3 bits of A
# bxl(7) : B = B xor 7
# cdv(5) : C = C / 2**B  -- NOP
# bxl(7) : B = B xor 7   -- restore B to its initial value
# bxc(6) : B = B xor C   -- NOP since C=0
# adv(3) : A = A / 8     -- prepare the next 3 input bits
# out(5) : print B       -- -> the 3 input bits for this turn (2,4,1,7,7,5,1,7,4,6,0,3,5,5,3,0)
# jnz(0) : repeat until A==0


# bst(4) : B = A % 8     -- last 3 bits of A
# adv(3) : A = A / 8     -- prepare the next 3 input bits
# out(5) : print B       -- -> the 3 input bits for this turn (2,4,1,7,7,5,1,7,4,6,0,3,5,5,3,0)
# jnz(0) : repeat until A==0
