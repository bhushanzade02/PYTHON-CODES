#include <iostream>
#include <algorithm>
#include <string>
#include <cctype> 

using namespace std;

int main()
{
    string str1 = "listen";
    string str2 = "silent";
      

    
    transform(str1.begin(), str1.end(), str1.begin(), ::tolower);
    transform(str2.begin(), str2.end(), str2.begin(), ::tolower);


    sort(str1.begin(), str1.end());
    sort(str2.begin(), str2.end());
    

    if (str1 == str2){
        cout << "Given string is valid anagram";
    }
    else {
        cout <<"Not a valid anagram";
    }

    // cout << str1 << endl;
    // cout << str2 << endl;
}
