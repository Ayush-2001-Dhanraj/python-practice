// given an m x n integer matrix, if an element is 0
// set its entire row and column as 0 in place

#include <bits/stdc++.h>
using namespace std;

int main(int argc, char *argv[])
{
    int m, n;
    cin >> m >> n;
    vector<vector<int>> matrix(m, vector<int>(n));
    unordered_map<int, int> tracker;
    cout << "Enter matrix elements" << endl;
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            cin >> matrix[i][j];
            if (matrix[i][j] == 0)
                tracker[i] = j;
        }
    }

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
            cout << matrix[i][j] << " ";
        cout << endl;
    }

    for (auto item : tracker)
    {
        for (int i = 0; i < n; i++)
            matrix[item.first][i] = 0;
        for (int i = 0; i < m; i++)
            matrix[i][item.second] = 0;
    }

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
            cout << matrix[i][j] << " ";
        cout << endl;
    }

    return 0;
}