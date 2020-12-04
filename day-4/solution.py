#!/usr/bin/python3

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
    
    eyr = int(fields_map['eyr'])
    iyr = int(fields_map['iyr'])
    byr = int(fields_map['byr'])

    if eyr < 2020:
        print('passport expired')
        return False

    if iyr > 2020:
        print('passport issue date incorrect')
        return False

    if byr > 2020:
        print('passport birth year incorrect')
        return False



    return True

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
        if validate_fields(fields_map):
            print('ok\n')
            valid_passports += 1
        else:
            print('fail!\n')

    print('valid passports:', valid_passports, 'out of', total_passports)

if __name__ == '__main__':
    main()
