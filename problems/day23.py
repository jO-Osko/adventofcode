DAY = 23

def part1(data):
    return solve_part(parse_data(data.split("\n")))["b"]

def part2(data):
    return solve_part(parse_data(data.split("\n")), 1)["b"]

def parse_data(data):
    return [line.strip() for line in data]

def solve_part(data, start_a=0):
    registers = {"a":start_a, "b":0}
    stack = data
    sp = 0 #  Stack pointer
    while sp < len(data):
        sp += execute_command(data[sp], registers)
    return registers

def execute_command(command, registers):
    if "," in command:
        command, offset = command.split(", ")
        command, register = command.split(" ")
        if command == "jie" and registers[register] % 2 == 0:
            return int(offset)
        if command == "jio" and registers[register] == 1:
            return int(offset)
    else:
        command, value = command.split(" ")
        if command == "hlf":
            registers[value] = registers[value] // 2
        if command == "tpl":
            registers[value] = registers[value] * 3
        if command == "inc":
            registers[value] = registers[value] + 1
        if command == "jmp":
            return int(value)
    return 1

DATA = """jio a, +22
inc a
tpl a
tpl a
tpl a
inc a
tpl a
inc a
tpl a
inc a
inc a
tpl a
inc a
inc a
tpl a
inc a
inc a
tpl a
inc a
inc a
tpl a
jmp +19
tpl a
tpl a
tpl a
tpl a
inc a
inc a
tpl a
inc a
tpl a
inc a
inc a
tpl a
inc a
inc a
tpl a
inc a
tpl a
tpl a
jio a, +8
inc b
jie a, +4
tpl a
inc a
jmp +2
hlf a
jmp -7"""


print(part1(DATA))
print(part2(DATA))
