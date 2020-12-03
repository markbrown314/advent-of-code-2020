#!/usr/bin/python3

"""
🎅 Advent of Code 2020 Day #2 Password Philosophy Part 2
   by Mark F. Brown <mark.brown314@gmail.com>

Format of the code
[a]-[b]<space>[letter]:<space>[code ...]

a is position #1
b is position #2
letter is letter checked against password
code is the password to be validated

1. split string by delemiters <space>
2. split [a]-[b] via '-' to obtain position #1 and position #2
3. split [letter]: to obtain letter to check
4. take remainder for password
5. validate that only position #1 or #2 has the letter
"""

def main():
    """ validate passwords """

    with open('puzzle_input_1.txt') as file_input:

        valid_count = 0

        for input_data in file_input:
            # tokenizer
            items = input_data.split(" ")

            positions = items[0].split("-")

            letter = items[1].split(":")[0]
            password = items[2]

            count = 0

            for check_pos in positions:
                index = int(check_pos) - 1
                if password[index] == letter:
                    count += 1

            if count == 1:
                print("password", password, "is valid")
                valid_count += 1
            else:
                print("password", password, "is invalid due to letter:", letter, "count:", count)

        print("valid passwords counted =", valid_count)

if __name__ == "__main__":
    main()
