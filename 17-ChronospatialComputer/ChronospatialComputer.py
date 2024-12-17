#! /usr/bin/env python3

import contextlib

import aoc


class Computer:
    def run(self, program, *, A=0, B=0, C=0, debug=False):
        self.A = A
        self.B = B
        self.C = C
        self.IP = 0
        self.output = []
        while len(program) > self.IP:
            instruction = Computer.opcodes[program[self.IP]]
            if debug:
                print(f"{self.IP}: {self.A=:b} {self.B=:b} {self.C=:b}", end= " ")
            self.IP += 1
            operand = program[self.IP]
            self.IP += 1
            if debug:
                print(f"{instruction.__qualname__} {operand}", end=" -> ")
            instruction(self, operand)
            if debug:
                print(f"{self.A=:b} {self.B=:b} {self.C=:b}")
        return ",".join(self.output)
    #     Combo operands 0 through 3 represent literal values 0 through 3.
    #     Combo operand 4 represents the value of register A.
    #     Combo operand 5 represents the value of register B.
    #     Combo operand 6 represents the value of register C.
    #     Combo operand 7 is reserved and will not appear in valid programs.
    def combo(self, operand):
        match operand:
            case 0 | 1 | 2 | 3:
                return operand
            case 4:
                return self.A
            case 5:
                return self.B
            case 6:
                return self.C
            case 7 | _:
                raise SyntaxError(f"bad combo value {operand}")
    # The eight instructions are as follows:
    opcodes = [None] * 8
    # The adv instruction (opcode 0) performs division. The numerator is the value in the A register.
    # The denominator is found by raising 2 to the power of the instruction's combo operand. (So, an operand of 2
    # would divide A by 4 (2^2); an operand of 5 would divide A by 2^B.) The result of the division operation is
    # truncated to an integer and then written to the A register.
    def adv(self, operand):
        self.A = self.A >> self.combo(operand)
    opcodes[0] = adv
    # The bxl instruction (opcode 1) calculates the bitwise XOR of register B and the instruction's literal operand,
    # then stores the result in register B.
    def bxl(self, operand):
        self.B = self.B ^ operand
    opcodes[1] = bxl
    # The bst instruction (opcode 2) calculates the value of its combo operand modulo 8 (thereby keeping only its
    # lowest 3 bits), then writes that value to the B register.
    def bst(self, operand):
        self.B = self.combo(operand) % 8
    opcodes[2] = bst
    # The jnz instruction (opcode 3) does nothing if the A register is 0. However, if the A register is not zero,
    # it jumps by setting the instruction pointer to the value of its literal operand; if this instruction jumps,
    # the instruction pointer is not increased by 2 after this instruction.
    def jnz(self, operand):
        if self.A:
            self.IP = operand
    opcodes[3] = jnz
    # The bxc instruction (opcode 4) calculates the bitwise XOR of register B and register C, then stores the result
    # in register B. (For legacy reasons, this instruction reads an operand but ignores it.)
    def bxc(self, _):
        self.B = self.B ^ self.C
    opcodes[4] = bxc
    # The out instruction (opcode 5) calculates the value of its combo operand modulo 8, then outputs that value.
    # (If a program outputs multiple values, they are separated by commas.)
    def out(self, operand):
        self.output.append(str(self.combo(operand) % 8))
    opcodes[5] = out
    # The bdv instruction (opcode 6) works exactly like the adv instruction except that the result is stored in the
    # B register. (The numerator is still read from the A register.)
    def bdv(self, operand):
        self.B = self.A >> self.combo(operand)
    opcodes[6] = bdv
    # The cdv instruction (opcode 7) works exactly like the adv instruction except that the result is stored in the
    # C register. (The numerator is still read from the A register.)
    def cdv(self, operand):
        self.C = self.A >> self.combo(operand)
    opcodes[7] = cdv

if aoc.test:
    A = 729
    program = (0,1,5,4,3,0)
else:
    A = 66245665
    program = (2,4, 1,7, 7,5, 1,7, 4,6, 0,3, 5,5, 3,0)


if aoc.part == "one":
    print(Computer().run(program, A=A))


if aoc.part == "two":
    # The decoded input program is:
    # bst A : B = A % 8     -- last 3 bits of A -> B
    # bxl 7 : B = B xor 7
    # cdv 5 : C = A >> B
    # bxl 7 : B = B xor 7   -- restore B to its initial value
    # bxc C : B = B xor C
    # adv 3 : A = A / 8     -- delete the last 3 bits of A
    # out B : print B
    # jnz 0 : repeat until A==0

    # Finding the initial A value requires to work on the program instructions from end to start
    # because for each loop, output depends on the 3 last bits A and some bits before, that is
    # bits that will be used in the future, but not bits from A already used
    # for each step all values are tested from 0 to 7
    #  - appending this to the end of A
    #  - computing B and C and testing if output equals the value
    # the function is a recursive DFS because some values lead to impossible solution
    def findA(reversedprogram, A=0):
        if not reversedprogram:
            return A
        expectedvalue = reversedprogram[0]
        for a in range(8):
            nextA = (A << 3) + a
            shift = a ^ 7
            C = (nextA >> shift) % 8
            B = a ^ C
            if expectedvalue == B:
                with contextlib.suppress(RuntimeError):
                    return findA(reversedprogram[1:], nextA)
        raise RuntimeError

    print(A := findA(list(reversed(program))))
    assert Computer().run(program, A=A) == ",".join(map(str, program))  # noqa: S101
