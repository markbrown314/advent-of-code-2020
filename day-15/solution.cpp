#include <iostream>
#include <unordered_map>

/*
 * 🎅 Advent of Code 2020 Day #15  Rambunctious Recitation Part 1 & 2
 * by Mark F. Brown <mark.brown314@gmail.com>
 */

using namespace std;

#define MAX_ARRAY 30000000
int main()
{
    unsigned int *puzzle_input = new unsigned int[MAX_ARRAY] {};
    puzzle_input[9] = 1;
    puzzle_input[3] = 2;
    puzzle_input[1] = 3;
    puzzle_input[0] = 4;
    puzzle_input[8] = 5;
    puzzle_input[4] = 6;

    unsigned long turn = 7;
    unsigned long spoken = 4;

    while(true)
    {
        if (puzzle_input[spoken] != 0)
        {
            unsigned long diff = turn - 1 - puzzle_input[spoken];
            puzzle_input[spoken] = turn - 1;
            spoken = diff;
        }
        else
        {
            puzzle_input[spoken] = turn - 1;
            spoken = 0;
        }

        if (turn == 2020)
        {
            cout << "part 1: " << spoken << "\n";
        }

        if (turn == MAX_ARRAY)
        {
            cout << "part 2: " << spoken << "\n";
            break;
        }

        turn++;
    }
}

