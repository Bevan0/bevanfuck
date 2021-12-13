import sys

# Memory
MEMORY_SIZE = 65536
memory = []
ptr_instruction = 0
ptr_mem = 0

for i in range(MEMORY_SIZE):
    memory.append(0)

loops = []

# Read program
program = list(open(sys.argv[1]).read())

# Run program
while ptr_instruction != len(program):
    instruction = program[ptr_instruction]
    if instruction == "+":
        memory[ptr_mem] += 1
    elif instruction == "-":
        memory[ptr_mem] -= 1
    elif instruction == "<":
        ptr_mem -= 1
    elif instruction == ">":
        ptr_mem += 1
    elif instruction == ".":
        print(chr(memory[ptr_mem]), end="")
    elif instruction == ",":
        memory[ptr_mem] = int(ord(input("")[0]))
    elif instruction == "[":
        loops.append(ptr_instruction)
    elif instruction == "]":
        if memory[ptr_mem] == 0:
            loops.pop()
        else:
            ptr_instruction = loops[-1]
    ptr_instruction += 1