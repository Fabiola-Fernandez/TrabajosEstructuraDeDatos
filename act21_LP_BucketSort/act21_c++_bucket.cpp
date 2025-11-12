#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

void bucketSort(float arr[], int n) {
    vector<float> buckets[n];

    // Colocar elementos en cubetas
    for (int i = 0; i < n; i++) {
        int index = n * arr[i];
        buckets[index].push_back(arr[i]);
    }

    // Ordenar cada cubeta
    for (int i = 0; i < n; i++)
        sort(buckets[i].begin(), buckets[i].end());

    // Unir cubetas
    int idx = 0;
    for (int i = 0; i < n; i++)
        for (float num : buckets[i])
            arr[idx++] = num;
}

int main() {
    float arr[] = {0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21, 0.12, 0.23, 0.68};
    int n = sizeof(arr) / sizeof(arr[0]);

    bucketSort(arr, n);

    cout << "Arreglo ordenado: ";
    for (int i = 0; i < n; i++)
        cout << arr[i] << " ";
    cout << endl;

    return 0;
}
