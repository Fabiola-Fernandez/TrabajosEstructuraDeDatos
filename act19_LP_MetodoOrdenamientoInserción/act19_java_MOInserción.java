public class Main {
    public static void main(String[] args) {
        int[] arr = {5, 2, 9, 1, 5, 6};
        int n = arr.length;

        for (int i = 1; i < n; i++) {
            int key = arr[i];
            int j = i - 1;

            while (j >= 0 && arr[j] > key) {
                arr[j + 1] = arr[j];
                j--;
            }
            arr[j + 1] = key;
        }

        System.out.print("Arreglo ordenado: ");
        for (int num : arr)
            System.out.print(num + " ");
    }
}
