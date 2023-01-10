#include <bits/stdc++.h>

using namespace std;
string reverse(string word){
    string coba= "";
    for(int i=0;i<word.size();i++){
        coba = word[i] + coba;
    }
    return coba;
}
int main()
{


    string x, temp;
    cin >> x;
    int p1 = 0, p2, count = 0;
    while(p1 != x.size()){
        p2 = 2;
        while(p1+(p2-1)<x.size()){
            temp = reverse(x.substr(p1, p2));
            if (x.substr(p1, p2) == temp){
                cout << x.substr(p1, p2) << ' ' << p1 << ' ' << p2 << endl;
                count++;
            }
        p2++;
        }
        p1++;
    }
    cout << endl << count;
}
