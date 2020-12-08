#!/usr/bin/python3
""" 🎅 Advent of Code Day 7: Handy Haversacks """
""" Mark F. Brown <mark.brown314@gmail.com> """
import sys
import re

def main():
    filename = "puzzle_test.txt" if len(sys.argv) < 2 else sys.argv[1]
    rules = open(filename).read().splitlines()
    rules = [re.sub("bags|bag|\.| |[0-9]|contain no other ", "", rule) for rule in rules]
    #print(rules)

    luggage_dict = dict()

    uniq = set()
    for rule in rules:
        relations = rule.split('contain')
        uniq.add(relations[0])
        #print("key:", relations[0])
        if len(relations) > 1:
            members  = relations[1].split(',')
            #print("members:", members)
            for member in members:
                uniq.add(member)
                luggage_dict.setdefault(member, set()).add(relations[0])
    print(uniq, len(uniq))

    search = {"shinygold"}
    count = 1

    while search != set():
        print(search)
        key = search.pop()
        if key in luggage_dict:
            print(key, "->", luggage_dict[key])
            count += 1
            search |= luggage_dict[key]
    print("count:", count)

if __name__ == "__main__":
    main()

