#!/usr/bin/python3
""" 🎅 Advent of Code Day 7: Handy Haversacks """
""" Mark F. Brown <mark.brown314@gmail.com> """
import sys
import re
from treelib import Tree, Node

def search_luggage(luggage_dict, key, find):
    stack = [(1, key)]
    while stack:
        item = stack.pop()
        if item[1] == find:
            return True
        if item[1] not in luggage_dict:
            continue
        stack += luggage_dict[item[1]]
    return False

def main():
    filename = "puzzle_test.txt" if len(sys.argv) < 2 else sys.argv[1]
    rules = open(filename).read().splitlines()
 
    # parse input file into a dictionary
    # (bag count, bag name)

    rules = [re.sub(r"bags|bag|\.| |contain no other ", "", rule) for rule in rules]

    luggage_dict = dict()
 
    for rule in rules:
        relations = rule.split('contain')
        if len(relations) > 1:
            members = relations[1].replace(',', ' ')
            data = re.findall(r"(\d+)(\w+)", members)
            luggage_dict[relations[0]] = data

    # generate a dictionary of trees mapping each luggage relationship
    # (bag count, bag name)

    tree_dict = dict()

    for data in luggage_dict:
        tree_dict[data] = Tree()
        root_node = Node(tag = ('1', data), data = data)
        parent_id = root_node.identifier
        tree_dict[data].add_node(root_node)
        parent_id = root_node.identifier
        for bag in luggage_dict[data]:
            tree_dict[data].create_node(tag = bag, data = data, parent = parent_id)

    # count every tree that contains a shiny gold bag
    print("part #1:", sum([(search_luggage(luggage_dict, key, "shinygold")) for key in luggage_dict]) - 1)

    # build tree of luggage containing shiny gold

    items = ['shinygold']
    tree = Tree()
    node = Node('shinygold', data=int(1))
    items = [node]
    tree.add_node(node, parent = None)

    while items:
        parent_node = items.pop()
        parent_id = parent_node.identifier
        if parent_node.tag not in luggage_dict:
            continue
        for data in luggage_dict[parent_node.tag]:
            node = Node(tag = data[1], data = int(data[0]))
            tree.add_node(node, parent = parent_id)
            items.append(node)

    # preorder traversal to distribute the luggage multiplier
    stack = [tree.get_node(tree.root)]
    output = []

    while stack:
        node = stack.pop()
        for child_node in tree.children(node.identifier):
            child_node.data *= node.data
        output.insert(0, node.data)

        if tree.children(node.identifier):
            stack += reversed(tree.children(node.identifier))

    # produce bag total
    print("part #2:", sum(output)-1)

if __name__ == "__main__":
    main()

