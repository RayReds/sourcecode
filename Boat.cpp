#include <bits/stdc++.h>
using namespace std;
string operator*(string s, int n)
{
    if (n <= 0) {
        return "";
    }
    string output = "";
    while(n--){
        output += s;
    }
    return output;
}
int main()
{
    int x, flag, help;
    string star = "* ", space = "  ", space1= " ";
    cin >> x;
    flag = x-2;
    if ((x%2) != 1 || x == 1){
        cout << endl << "Must be odd number from 3";
        return 0;
    }
    for(int i = 0; i < ((flag/2)+1); i++){
        cout << space*(x/2);
        for(int b = 0; b <= i;b++){
            cout << star;
        }
        cout << endl;
    }
    for(int i = flag/2; i > 0; i--){
        for(int a = 0; a <= flag/2;a++){
            cout << space;
        }
        for(int b = 0; b < i;b++){
            cout << star;
        }
        cout << endl;
    }
    //Print Inside
    help = x-3;
    for(int i = 0; i < (x/2); i++){
        if (i == 0 || i == (x/2)-1){
            cout << space1*i<< star*(x-i) << endl;
        }
        else {
            int a = help * 2;
        https://www.onlinegdb.com/online_c++_compiler#tab-stdin    for(int a = 0; a<i;a++){
                cout << " ";
            }
            cout << star;
            for(int b = 0; b < a; b++){
                cout << " ";
            }
            cout << star << endl;
            help--;
        }

    }
}
