#include <iostream>
using namespace std;


float CtoF(float c)
{
    return (1.8 * c) + 32;
}

int main()
{
    float c;
    float fahrenheit;

    cout << "Enter the temperature in Celsius: " << endl;
    cin >> c;

    fahrenheit = CtoF(c);

    cout << "Temperature in Fahrenheit: " << fahrenheit << endl;

    return 0;
}


// OUTPUT:-
// Enter the temperature in Celsius: 25
// Temperature in Fahrenheit: 77