#!/usr/bin/python3

""" 🎅 Advent of Code 2020 Day #2 Password Philosophy """
""" by Mark F. Brown <mark.brown314@gmail.com> """

""" 
Format of the code
[a]-[b]<space>[letter]:<space>[code ...]

a is minimum
b is maximum
letter is letter checked against password
code is the password to be validated

1. split string by delemiters <space>
2. split [a]-[b] via '-' to obtain minimum and maximum
3. split [letter]: to obtain letter to check
4. take remainder for password
5. iterate through passwords and count letter instances
6. validate that it meets the maximum and minimum requirements
"""

# load puzzle input file
with open('puzzle-input-1.txt') as file_input:
    
    valid_count = 0

    for input_data in file_input:
        # tokenizer
        items = input_data.split(" ")

        min_max = items[0].split("-")
        low = int(min_max[0])
        high = int(min_max[1])

        letter = items[1].split(":")[0]
        password = items[2]

        count = 0
        for check in password:
            if check == letter:
                count += 1
        if count < low or count > high:
            print("password", password, "is invalid count of", letter, "=", count)
        else:
            print ("password", password, "is valid")
            valid_count += 1
    print("valid passwords counted =", valid_count)
