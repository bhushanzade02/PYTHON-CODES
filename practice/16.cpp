#include <string>
#include <iostream>
using namespace std;

int main()

{

    string mystring = "this line conatin four whitespces";
    int count = 0;

    for (char c : mystring)
    {
        if (c == ' ')
        {
            count++;
        }
    }
    cout << " for loop 1 " << count << endl;

    int counter = 0 ;
    for (int i = 0; i < mystring.length(); i++)
    {
        if (mystring[i] == ' ')
        {
            counter++;
        }
    }
    cout << " for loop 2 " << count << endl;
}