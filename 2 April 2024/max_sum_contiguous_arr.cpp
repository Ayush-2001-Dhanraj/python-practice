// Largest sum contiguous array

#include <bits/stdc++.h>
using namespace std;

int main(int argc, char *argv[])
{
    vector<int> arr;

    for (int i = 1; i < argc; i++)
    {
        arr.push_back(atoi(argv[i]));
    }

    int max_sum = 0;
    int current_sum = 0;

    for (int ele : arr)
    {
        current_sum += ele;

        if (current_sum > max_sum)
        {
            max_sum = current_sum;
        }

        if (current_sum < 0)
        {
            current_sum = 0;
        }
    }

    cout << "Max sum: " << max_sum << endl;

    return 0;
}