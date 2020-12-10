#!/usr/bin/python3
""" 🎅 Advent of Code Day 7: Handy Haversacks """
""" Mark F. Brown <mark.brown314@gmail.com> """
import sys
import re
from treelib import Tree, Node

def main():
    filename = "puzzle_test.txt" if len(sys.argv) < 2 else sys.argv[1]
    rules = open(filename).read().splitlines()
    rules = [re.sub(r"bags|bag|\.| |contain no other ", "", rule) for rule in rules]

    luggage_dict = dict()
    tree_dict = dict()
 
    for rule in rules:
        relations = rule.split('contain')
        print("*key:", relations[0])
        if len(relations) > 1:
            members = relations[1].replace(',', ' ')
            data = re.findall(r"(\d+)(\w+)", members)
            print("data:", data)
            luggage_dict[relations[0]] = data
    print(luggage_dict)
    for data in luggage_dict:
        tree_dict[data] = Tree()
        root_node = Node(tag = data, data = data)
        parent_id = root_node.identifier
        tree_dict[data].add_node(root_node)
        print("name:", data, "id:", tree_dict[data].identifier)
        parent_id = root_node.identifier
        for bag in luggage_dict[data]:
            print("data:", data, "bag:", bag[1])
            print(tree_dict[data].identifier)
            tree_dict[data].create_node(tag = bag, data = data, parent = parent_id)

    for data in luggage_dict:
        tree_dict[data].show()
    
    items = ['shinygold']

    # search
    while items:
        print(items)
        item = items.pop()
        if item not in luggage_dict:
            continue
        for data in luggage_dict[item]:
            print("'{}'".format(data[1]))
            items.append(data[1])

    tree = Tree()
    node = Node('shinygold', data=int(1))
    items = [node]
    tree.add_node(node, parent = None)

    while items:
        parent_node = items.pop()
        print(parent_node)
        parent_id = parent_node.identifier
        if parent_node.tag not in luggage_dict:
            continue
        for data in luggage_dict[parent_node.tag]:
            node = Node(tag = data[1], data = int(data[0]))
            tree.add_node(node, parent = parent_id)
            items.append(node)

    tree.show()

    # pre order traversal
    stack = [tree.get_node(tree.root)]
    output = []

    while stack:
        node = stack.pop()
        for child_node in tree.children(node.identifier):
            child_node.data *= node.data
        output.insert(0, node.data)
        print(node.data, ",", end="")

        if tree.children(node.identifier):
            stack += reversed(tree.children(node.identifier))

    print(output)
    print(sum(output)-1)

if __name__ == "__main__":
    main()

