#include <iostream>
#include <iomanip>
#define MAXN 100
#define ORDER 4
using namespace std;

int main()
{

    int n;
    float x;
    cout << "enter he value of n" << endl;
    cin >> n;

    float ax[MAXN + 1], ay[MAXN + 1];
    cout << "Enter The value of Ax and Ay" << endl;
    for (int i = 0; i <= n; i++)
    {
        cin >> ax[i] >> ay[i];
    }

    cout << "enter the value of X "
         << "for which value of y is wanted " << endl;

    cin >> x;
    cout << fixed;
    float h;
    h = ax[1] - ax[0];

    /* now making the difference table */
    float diff[MAXN + 1][ORDER + 1];
    for (int i = 0; i < n - 1; i++)
    {
        diff[i][1] = ay[i + 1] - ay[i];
    }

    /* now the difference table for  2nd order and and higher derivative */
    for (int j = 2; j <= ORDER; j++)
    {
        for (int i = 0; i <= n - j; i++)
        {
            diff[i][j] = diff[i + 1][j - 1] - diff[i][j - 1];
        }
    }

    /* Now finding x0 */
    int i = 0;
    while (!(ax[i] > x))
        i++;
    i--;
    /* now ax[i] is x0 and ay[i] is y0*/
    float p = (x - ax[i]) / h;
    float yp = ay[i];

    float nr, dr =1;
    /* now carrying out interpolation */
    for (int k = 1; k <= ORDER; k++)
    {
        nr *= p - k + 1;
        yp += (nr / dr) * diff[i][k];
    }

    cout << "when x = " << setw(6) << setprecision(1) << x << " y = " << setw(6) << setprecision(2) << yp << endl;
    return 0;
}
