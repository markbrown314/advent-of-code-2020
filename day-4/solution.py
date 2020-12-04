#!/usr/bin/python3
import re

def chomp(line):
    line = line.replace('\n', '')
    line = line.replace('\r', '')
    return line

def extract_fields(fields_map, line):
    fields = line.split(' ')
    for field in fields:
        field = field.split(':')
        fields_map[field[0]] = field[1]
    return

def enhanced_fields_validation(fields_map):
    eyr = int(fields_map['eyr'])
    iyr = int(fields_map['iyr'])
    byr = int(fields_map['byr'])
    hgt = fields_map['hgt']
    hcl = fields_map['hcl']
    ecl = fields_map['ecl']
    pid = fields_map['pid']
    
    if eyr < 2020 or eyr > 2030:
        print('passport expiration date invalid:', eyr)
        return False

    if iyr < 2010 or iyr > 2020:
        print('passport issue date invalid:', iyr)
        return False

    if byr < 1920 or byr > 2002:
        print('passport birth year invalid:', byr)
        return False

    print("ecl:", ecl)
    if not re.match('amb|blu|brn|gry|grn|hzl|oth', ecl):
        print('eye color is invalid:', ecl)
        return False

    print("hgt:", "'{}'".format(hgt))
    if re.match('^[0-9]*cm', hgt):
        hgt = int(hgt.split('cm')[0])
        if hgt < 150 or hgt > 193:
            print('height in cm. is invalid:', hgt)
            return False
    elif re.match('^[0-9]*in$', hgt):
        hgt = int(hgt.split('in')[0])
        if hgt < 59 or hgt > 76:
            print('height in in. is invalid:', hgt)
            return False
    else:
        print('height units are invalid:', hgt)
        return False

    print("hcl:", hcl)
    if not re.match('^#[0-9|a-f]{6}$', hcl):
        print('hair color invalid:', hcl)
        return False

    print('pid:',pid)
    if not re.match('^[0-9]{9}$', pid):
        print('passport id invalid:', pid)
        return False

    return True

def validate_fields(fields_map):
    check_fields = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid'}
    optional_fields = {'cid'}
    req_fields = check_fields ^ optional_fields
    
    print('fields:', req_fields)

    req_union = set(list(fields_map.keys())) & req_fields
    print('union:', req_union)
    print('# fields', len(fields_map.keys()))
    if len(req_union) < len(req_fields):
        print('missing required diff:', req_union ^ req_fields)
        return False
    
    """
    eyr = int(fields_map['eyr'])
    iyr = int(fields_map['iyr'])
    byr = int(fields_map['byr'])

    if eyr < 2020:
        print('passport expired:', eyr)
        return False

    if iyr > 2020:
        print('passport issue date incorrect:', iyr)
        return False

    if byr > 2020:
        print('passport birth year incorrect:', byr)
        return False
    """

    return enhanced_fields_validation(fields_map)

def main():
    fields_map = dict()
    valid_passports = 0
    total_passports = 0
    with open('puzzle_input_1.txt') as file_input:
        for line in file_input:
            line = chomp(line)
            if line == '':
                total_passports += 1
                if validate_fields(fields_map):
                    print('ok!\n')
                    fields_map = dict()
                    valid_passports += 1
                else:
                    print('fail!\n')
                continue

            print("'{}'".format(line))
            extract_fields(fields_map, line)
    
    if fields_map:
        total_passports += 1
        if validate_fields(fields_map):
            print('ok\n')
            valid_passports += 1
        else:
            print('fail!\n')

    print('valid passports:', valid_passports, 'out of', total_passports)

if __name__ == '__main__':
    main()
