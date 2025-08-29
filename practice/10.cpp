#include <iostream>
#include <vector>
using namespace std;

int main()
{

    vector<char> A = {'b', 'h', 'u', 's', 'h', 'a', 'n'};
    cout << A.size() << endl;
    string result = "";
    for (int i = 0; i < A.size(); i++)
    {
        cout << A[i] << endl;
        result = result + A[i];
 
        cout << result << endl;
    }

    cout << result;
    return 0 ;
}