#include <iostream>
#include <unordered_map>
using namespace std;

int main(){
     string jewels;
     cin >> jewels;
     string stones;
     cin >> stones;

     unordered_map <char, int> map;
     int sum = 0;
     for (char jewel : jewels) {
          map[jewel]++;
     }
     for (char stone : stones) {
          if (map[stone] > 0) {
               sum++;
          }
     }

     cout << sum << '\n';
     return 0;
}