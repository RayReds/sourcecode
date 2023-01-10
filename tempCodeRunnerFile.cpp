/******************************************************************************

                              Online C++ Compiler.
               Code, Compile, Run and Debug C++ program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <bits/stdc++.h>
using namespace std;

int main()
{
    int x;
    cin >> x;
    int temp;
    vector<int> arr = {3, 2, 19, 4, 52};
    for(int i = arr.size()-1; i >= 0; i--){
        if (x < arr[i]){
            temp = i;
            break;
        }
    }
    for (int i = 0; i < temp; i++){
        cout << arr[i] << ", ";
    }
    cout << x << ", ";
    for (int i = temp; i<arr.size(); i++){
        cout << arr[i] << ", ";
    }
    return 0;
}
