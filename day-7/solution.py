#!/usr/bin/python3
""" 🎅 Advent of Code Day 7: Handy Haversacks """
""" Mark F. Brown <mark.brown314@gmail.com> """
import sys
import re

def depth(luggage_dict, key):
    tree = [key]
    print("key:", key)
    count = 0
    while tree:
        item = tree.pop()
        print("item", item)
        count += 1
        if item not in luggage_dict:
            continue
        tree += luggage_dict[item]
    return count

def search(luggage_dict, key, find):
    tree = [key]
    print("key:", key)
    count = 0
    while tree:
        item = tree.pop()
        print("item", item)
        if item == find:
            print("found!")
            return True
        if item not in luggage_dict:
            continue
        tree += luggage_dict[item]
    return False

def main():
    filename = "puzzle_test.txt" if len(sys.argv) < 2 else sys.argv[1]
    rules = open(filename).read().splitlines()
    rules = [re.sub("bags|bag|\.| |[0-9]|contain no other ", "", rule) for rule in rules]

    luggage_dict = dict()

    for rule in rules:
        relations = rule.split('contain')
        print("*key:", relations[0])
        if len(relations) > 1:
            members  = relations[1].split(',')
            print("*members:", members)
            luggage_dict[relations[0]] = members
    #for key in luggage_dict:
    print(sum([(search(luggage_dict, key,"shinygold")) for key in luggage_dict]) - 1)

if __name__ == "__main__":
    main()

