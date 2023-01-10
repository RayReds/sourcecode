/******************************************************************************

                              Online C++ Compiler.
               Code, Compile, Run and Debug C++ program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <bits/stdc++.h>
using namespace std;

int main()
{
    int x, y;
    cout << endl << "Pick one player : Ronaldo, Messi, Mbappe, Pele" << endl;
    cin >> x;


    cout << "What to find out: Height, Goals, Ballon d'or" << endl;

    switch(x) {
        case 1:
            cin >> y;
            switch(y) {
                case 1:
                    cout << "1.87m";
                    break;
                case 2:
                    cout << "815";
                    break;
                case 3:
                    cout << "5";
                    break;
            }
        case 2:
            cin >> y;
            switch(y) {
                case 1:
                    cout << "1.69m";
                    break;
                case 2:
                    cout << "773";
                    break;
                case 3:
                    cout << "7";
                    break;
            }
        case 3:
            cin >> y;
            switch(y) {
                case 1:
                    cout << "1.78m";
                    break;
                case 2:
                    cout << "213";
                    break;
                case 3:
                    cout << "0";
                    break;
            }
        case 4:
            cin >> y;
            switch(y) {
                case 1:
                    cout << "1.73m";
                    break;
                case 2:
                    cout << "1281";
                    break;
                case 3:
                    cout << "0";
                    break;
            }
        default:
            cout << "Didn't know that player";
            break;
    }
    return 0;
}
