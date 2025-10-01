using System;

class Program {
    static void Merge(int[] arr, int l, int m, int r) {
        int[] L = new int[m-l+1], R = new int[r-m];
        Array.Copy(arr, l, L, 0, m-l+1);
        Array.Copy(arr, m+1, R, 0, r-m);
        int i=0,j=0,k=l;
        while(i<L.Length && j<R.Length)
            arr[k++] = (L[i] <= R[j]) ? L[i++] : R[j++];
        while(i<L.Length) arr[k++] = L[i++];
        while(j<R.Length) arr[k++] = R[j++];
    }

    static void MergeSort(int[] arr, int l, int r) {
        if (l < r) {
            int m = (l+r)/2;
            MergeSort(arr, l, m);
            MergeSort(arr, m+1, r);
            Merge(arr, l, m, r);
        }
    }

    static void Main() {
        int[] arr = {38, 27, 43, 3, 9, 82, 10};
        MergeSort(arr, 0, arr.Length-1);
        Console.WriteLine(string.Join(" ", arr));
    }
}