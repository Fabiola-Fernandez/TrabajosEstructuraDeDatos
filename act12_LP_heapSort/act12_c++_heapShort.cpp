#include <iostream>
using namespace std;

void heapify(int arr[], int n, int i) {
    int mayor = i;    
    int izquierda = 2*i + 1; 
    int derecha = 2*i + 2;

    if (izquierda < n && arr[izquierda] > arr[mayor])
        mayor = izquierda;

    if (derecha < n && arr[derecha] > arr[mayor])
        mayor = derecha;

    if (mayor != i) {
        swap(arr[i], arr[mayor]);
        heapify(arr, n, mayor);
    }
}

void heapSort(int arr[], int n) {
    for (int i = n/2 - 1; i >= 0; i--)
        heapify(arr, n, i);

    for (int i=n-1; i>=0; i--) {
        swap(arr[0], arr[i]);
        heapify(arr, i, 0);
    }
}

int main() {
    int arr[] = {12, 11, 13, 5, 6, 7};
    int n = sizeof(arr)/sizeof(arr[0]);

    heapSort(arr, n);

    cout << "Arreglo ordenado: ";
    for (int i=0; i<n; i++)
        cout << arr[i] << " ";
    return 0;
}