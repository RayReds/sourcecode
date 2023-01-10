#include <bits/stdc++.h>
using namespace std;

int main()
{
    int x;
    cin >> x;
    int temp;
    vector<int> arr = {3, 2, 19, 4, 52};
    vector<int> li;
    for(int i = arr.size()-1; i >= 0; i--){
        if (x < arr[i]){
            temp = i;
            break;
        } else if (i == 0){
            temp = i;
        }
    }

    for(int i = 0; i<arr.size(); i++){
        if(i == temp){
            li.push_back(x);
            li.push_back(arr[i]);
        } else {
            li.push_back(arr[i]);
        }
    }
    for(int i: li){
        cout<< i << " ";
    }
    return 0;
}
