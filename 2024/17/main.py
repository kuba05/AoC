
memory = []

regs = []
pointer = 0
output = []

def comboArg(arg):
    if 0 <= arg <= 3:
        return arg
    if 4 <= arg <= 6:
        return regs[arg-4]
    raise NotImplementedError("Combo arg 7")

def evaluate(cmd, arg):
    global pointer

    match cmd:
        case 0:
            regs[0] = regs[0] >> comboArg(arg)
        
        case 1:
            regs[1] = regs[1] ^ arg

        case 2:
            regs[1] = comboArg(arg) % 8
        
        case 3:
            if regs[0] == 0:
                return
            pointer = arg-2
        
        case 4:
            regs[1] = regs[1] ^ regs[2]
        
        case 5:
            output.append(str(comboArg(arg)%8))

        case 6:
            regs[1] = regs[0] >> comboArg(arg)

        case 7:
            regs[2] = regs[0] >> comboArg(arg)



regs.append(int(input().split(": ")[1]))
regs.append(int(input().split(": ")[1]))
regs.append(int(input().split(": ")[1]))
input()
memory = list(map(int,input().split(": ")[1].split(",")))

print("regs:")
print(regs)
print("memory")
print(memory)
regs[0] = 1618853666836816//8
print(regs)
while 0 <= pointer < len(memory)-1:
    evaluate(memory[pointer], memory[pointer+1])
    pointer += 2

print(",".join(output))