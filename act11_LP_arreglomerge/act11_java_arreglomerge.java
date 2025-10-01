import java.util.*;

class MergeSort {
    static void merge(int[] arr, int l, int m, int r) {
        int[] L = Arrays.copyOfRange(arr, l, m+1);
        int[] R = Arrays.copyOfRange(arr, m+1, r+1);
        int i=0,j=0,k=l;
        while(i<L.length && j<R.length)
            arr[k++] = (L[i] <= R[j]) ? L[i++] : R[j++];
        while(i<L.length) arr[k++] = L[i++];
        while(j<R.length) arr[k++] = R[j++];
    }

    static void mergeSort(int[] arr, int l, int r) {
        if(l<r){
            int m=(l+r)/2;
            mergeSort(arr,l,m);
            mergeSort(arr,m+1,r);
            merge(arr,l,m,r);
        }
    }

    public static void main(String[] args){
        int[] arr={38,27,43,3,9,82,10};
        mergeSort(arr,0,arr.length-1);
        System.out.println(Arrays.toString(arr));
    }
}
