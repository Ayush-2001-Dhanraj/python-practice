// check if a string is a valid anagram or not

#include <bits/stdc++.h>
using namespace std;

bool is_valid_anagram(string s, string t)
{
    unordered_map<char, int> tracker;
    int sizeS = s.length();
    int sizeT = t.length();

    if (sizeS != sizeT)
        return false;

    for (int i = 0; i < sizeS; i++)
    {
        tracker[s[i]]++;
    }

    for (int i = 0; i < sizeS; i++)
    {
        if (tracker.find(t[i]) != tracker.end())
            tracker[t[i]] -= 1;
        else
            return false;
    }

    for (auto item : tracker)
    {
        if (item.second != 0)
            return false;
    }

    return true;
}

int main(int argc, char *argv[])
{
    string s = argv[1];
    string t = argv[2];
    if (is_valid_anagram(s, t))
    {
        cout << s << " and " << t << " are valid anagrams" << endl;
    }
    else
    {
        cout << s << " and " << t << " are not valid anagrams" << endl;
    }
    return 0;
}