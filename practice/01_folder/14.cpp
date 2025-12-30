#include <iostream>
#include <string>
#include <algorithm>
#include <cctype>
using namespace std;

int main()
{
    string test = "kareryak";
    string result = test;

    transform(test.begin(), test.end(), test.begin(), ::tolower);

    reverse(test.begin(), test.end());

    if (result == test)
    {
        cout << "it is palindrome ";
    }
    else
    {
        cout << "Not a palindrome";
    }

    return 0;
}