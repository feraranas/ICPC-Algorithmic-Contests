#include <iostream>
#include <vector>
using namespace std;

int main() {
     vector<vector<int>> v;
     vector<int> t = {1, 2, 3};
     cout << t.size() << endl;
     int tamanoLista = 0;
     
     for (int i = 0; i < t.size(); i++) {
          vector<int> aux = {};
          for (int j = 0; j < tamanoLista; j++) {
               aux.push_back(t[j]);
          }
          v.push_back(aux);

          
          tamanoLista++;
     }
}