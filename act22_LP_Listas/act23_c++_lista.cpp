#include <iostream>
#include <vector>
using namespace std;

int main() {
    vector<int> lista = {1, 2, 3};

    lista.push_back(4);

    for (int n : lista) {
        cout << n << " ";
    }
    return 0;
}
