#!/usr/bin/python3

import sys

def nop(pos, acc, arg):
    pass
def acc(pos, acc, arg):
    return acc + arg
def jmp(pos, acc, arg):
    return pos + arg
def list_program(program):
    line_no = 0
    for line in program:
        print(line_no, ": ", line[0], line[1], sep="")
        line_no += 1

def exec_program(program):
    acc = 0
    line_no = 0
    while True:
        print(program[line_no])
        if program[line_no][2]:
            print("repeated line at:", line_no, "acc", acc)
            break
        if program[line_no][0] == "nop":
            program[line_no][2] = True 
            line_no += 1
            continue
        if program[line_no][0] == "jmp":
            program[line_no][2] = True 
            line_no += int(program[line_no][1])
            continue
        if program[line_no][0] == "acc":
            program[line_no][2] = True 
            acc += int(program[line_no][1])
            line_no += 1
            continue

def main():
    filename = "puzzle_test.txt" if len(sys.argv) < 2 else sys.argv[1]
    file_input = open(filename).read().splitlines()
    program = [data.split() + [False] for data in file_input]

    #list_program(program)
    exec_program(program)
    
if __name__ == "__main__":
    main()