// sort and array of 0, 1 and 2

#include <bits/stdc++.h>
using namespace std;

int main(int argc, char *argv[])
{
    int n = 0;
    vector<int> arr;
    for (int i = 1; i < argc; i++)
    {
        arr.push_back(atoi(argv[i]));
        n++;
    }

    for (int e : arr)
        cout << e << " ";

    cout << endl
         << n << endl;

    int temp, low = 0, mid = 0, high = n - 1;

    while (mid <= high)
    {
        switch (arr[mid])
        {
        case 0:
            temp = arr[low];
            arr[low] = arr[mid];
            arr[mid] = temp;
            mid++;
            low++;
            break;
        case 1:
            mid++;
            break;
        case 2:
            temp = arr[high];
            arr[high] = arr[mid];
            arr[mid] = temp;
            mid++;
            high--;
            break;
        default:
            break;
        }
    }

    for (int e : arr)
        cout << e << " ";

    return 0;
}