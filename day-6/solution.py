#!/usr/bin/python3

def intersection(a, b):
    return set(a).intersection(b)

def main():
    groups = [a.replace('\n','') for a in open('puzzle_input_1.txt').read().split('\n\n')]
    counts = sum([len(set(a)) for a in groups])
    print("sum of counts:", counts)

    groups = [a.split('\n') for a in open('puzzle_input_1.txt').read().split('\n\n')]
    print(groups)
    s = 0
    for a in groups:
        if len(a) == 1:
            s+=len(a[0])
            continue
        answers = list()
        for b in a:
            if b == "":
                continue
            build = set()
            for c in b:
                build = build.union(set(c))
            print(build)
            answers.append(build)
        print(answers)
        d = set.intersection(*answers)
        s += len(d)

    print("sum =", s)
if __name__ == "__main__":
    main()
