#!/usr/bin/python3
"""
🎅 Advent of Code 2020 Day #4 Passport Processing Part 1 & 2
   by Mark F. Brown <mark.brown314@gmail.com>
"""

import sys
import re

def chomp(line):
    """ remove end of line """
    line = line.replace('\n', '')
    line = line.replace('\r', '')
    return line

def extract_fields(fields_map, line):
    """ copy line items to dictionary """
    fields = line.split(' ')
    for field in fields:
        field = field.split(':')
        fields_map[field[0]] = field[1]

def validate_fields(fields_map):
    """ validate passport fields """

    check_fields = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
    fields = set(list (fields_map.keys()))

    if len(check_fields & fields) != len(check_fields):
        return False

    eyr = int(fields_map['eyr'])
    iyr = int(fields_map['iyr'])
    byr = int(fields_map['byr'])
    hgt = fields_map['hgt']
    hcl = fields_map['hcl']
    ecl = fields_map['ecl']
    pid = fields_map['pid']

    if not re.match('^#[0-9|a-f]{6}$', hcl):
        return False

    if eyr < 2020 or eyr > 2030:
        return False

    if iyr < 2010 or iyr > 2020:
        return False

    if byr < 1920 or byr > 2002:
        return False

    if not re.match('amb|blu|brn|gry|grn|hzl|oth', ecl):
        return False

    if re.match('^[0-9]*cm', hgt):
        hgt = int(hgt.split('cm')[0])
        if hgt < 150 or hgt > 193:
            return False
    elif re.match('^[0-9]*in$', hgt):
        hgt = int(hgt.split('in')[0])
        if hgt < 59 or hgt > 76:
            return False
    else:
        return False

    if not re.match('^[0-9]{9}$', pid):
        return False

    return True

def main():
    """ Load puzzle data and validate content """
    fields_map = dict()
    valid_passports = 0
    filename = 'puzzle_input_1.txt'

    if len(sys.argv) > 1:
        filename = sys.argv[1]

    with open(filename) as file_input:

        for line in file_input:
            line = chomp(line)

            # next entry
            if line == '':
                if validate_fields(fields_map):
                    fields_map = dict()
                    valid_passports += 1
                    continue
                fields_map = dict()
                continue

            # store contents in dict
            extract_fields(fields_map, line)

    if fields_map:
        if validate_fields(fields_map):
            valid_passports += 1

    print('valid passports:', valid_passports)

if __name__ == '__main__':
    main()
