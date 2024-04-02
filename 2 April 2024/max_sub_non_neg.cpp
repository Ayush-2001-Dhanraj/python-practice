// maximum sub array of non negative numbers from an array

#include <bits/stdc++.h>
using namespace std;

int main(int argc, char *argv[])
{
    vector<int> numbers;

    for (int i = 1; i < argc; i++)
        numbers.push_back(atoi(argv[i]));

    int max_left = -1, max_right = -1, current_left = 0, current_right = 0, max_sum = 0, current_sum = 0;

    for (current_right = 0; current_right < numbers.size(); current_right++)
    {
        if (numbers[current_right] < 0)
        {
            current_left = current_right + 1;
            current_sum = 0;
        }
        else
        {
            current_sum += numbers[current_right];

            if ((current_sum > max_sum) ||
                (current_sum == max_sum && current_right - current_left > max_right - max_left))
            {
                max_left = current_left;
                max_right = current_right;
                max_sum = current_sum;
            }
        }
    }

    if (max_left == -1 || max_right == -1)
    {
        return 0;
    }

    for (int i = max_left; i < max_right + 1; i++)
    {
        cout << numbers[i] << " ";
    }

    return 0;
}