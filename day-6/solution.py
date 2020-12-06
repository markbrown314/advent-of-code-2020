#!/usr/bin/python3
"""
🎅 Advent of Code 2020 Day #6 Binary Boarding Part 1 & 2
   by Mark F. Brown <mark.brown314@gmail.com>
"""

import string
import sys

def main():
    """ input answers from customs form and output sums """
    filename = "puzzle_input_1.txt" if len(sys.argv) < 2 else sys.argv[1]
    # Part 1: Number of questions to which anyone answered "yes"
    form = [answers.replace('\n','') for answers in open(filename).read().split('\n\n')]
    counts = sum([len(set(answers)) for answers in form])
    print("sum of counts:", counts)

    # Part 2: Number of questions to which everyone answered "yes"
    identity_set = set(string.ascii_lowercase)
    form = [answer.splitlines() for answer in open(filename).read().split('\n\n')]
    consensus = [set.intersection(*([set(answer) for answer in answers] + [identity_set])) for answers in form]
    count = sum(len(result) for result in consensus)
    print("sum =", count)
if __name__ == "__main__":
    main()
