// move all the -ve elements to one side of the array without changing
// order of positive and negative elements

#include <bits/stdc++.h>
using namespace std;

int main(int argc, char *argv[])
{
    vector<int> arr, pos, neg;
    int n;
    for (int i = 1; i < argc; i++)
    {
        arr.push_back(atoi(argv[i]));
        n++;
    }

    for (int e : arr)
    {
        if (e < 0)
            neg.push_back(e);
        else
            pos.push_back(e);
    }

    int i = 0;
    while (i < pos.size())
    {
        arr[i] = pos[i];
        i++;
    }
    int j = 0;
    while (j < neg.size())
    {
        arr[j + pos.size()] = neg[j];
        j++;
    }

    for (int e : arr)
        cout << e << " ";
}