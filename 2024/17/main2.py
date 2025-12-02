
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

def evaluate(cmd, arg, regs, output):
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


for i in range(0):
    regs = [i, 0, 0]
    output = []
    pointer = 0
    
    while 0 <= pointer < len(memory)-1:
        evaluate(memory[pointer], memory[pointer+1], regs, output)
        print(regs)
        pointer += 2
    print(output)
    print(((i%8)^1)^4^(i>>((i%8)^1)))
    assert int(output[0]) == (((i%8)^1)^4^(i>>((i%8)^1)))%8

current = []
target = []
sufix = sum(current[i]<<(3*i) for i in range(len(current))) <<3
print("SUFFIX", sufix)
for X in range(2**3):
    X += sufix
    if (((X%8)^1)^4^(X>>((X%8)^1)))%8 == target[-len(current)-1]:
        print(X%8)
        print(X)
