#include <iostream>
#include <vector>
using namespace std;

int main()

{
    int n = 7;
    vector<int> A;

    for (int i = 1; i <= n; i++)
    {
        A.push_back(i* 10);
    }

    /* find the middle of element*/

    cout << A.size() << endl;

    int midlement = int(A.size() / 2);
    // cout << "result " << midlement << endl;

    cout << "Middle element" << A[midlement] << endl;

    for (int i = 0; i < n; i++)
    {
        cout << A[i] << endl;
    }
    return 0;
}