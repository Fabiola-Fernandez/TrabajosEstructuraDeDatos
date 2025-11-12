#include <iostream>
#include <set>
using namespace std;

int main() {
    int arr[] = {4, 2, 7, 1, 3, 7, 2};
    set<int> hashSet(arr, arr + 7); // elimina duplicados y mantiene orden

    cout << "Arreglo ordenado sin duplicados: ";
    for (int num : hashSet)
        cout << num << " ";
    cout << endl;
    return 0;
}
